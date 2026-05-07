---
title: "Karpathy Autoresearch — AI 에이전트의 자율 ML 실험 루프"
created: 2026-05-07
updated: 2026-05-07
domain: ai
type: fact-set
weight: important
confidence: high
tags: [karpathy, autoresearch, nanochat, generator-evaluator, muon, llm-training]
sources: [sources/karpathy-autoresearch-train.py]
---

# Karpathy Autoresearch

Andrej Karpathy가 2026년 공개한 단일 GPU 자율 ML 연구 루프 프로젝트.
"AI 에이전트에게 작지만 진짜인 LLM 학습 환경을 주고, 밤새 실험을 돌리게 한다"는 아이디어를 실제로 구현한 630줄짜리 단일 파일.

> [!fact] 사실
> 저장소: `karpathy/autoresearch` (GitHub). 핵심 파일은 `prepare.py`(불변), `train.py`(에이전트가 편집), `program.md`(에이전트 지침서) 3개.

## 작동 원리

> [!fact] 사실
> 에이전트는 `train.py`를 수정 → 5분 학습 → `val_bpb`(validation bits per byte) 측정 → 좋아졌으면 유지, 아니면 폐기 → 반복. 아침에 일어나면 실험 로그와 (운 좋으면) 더 나은 모델이 남아 있다.

> [!fact] 사실
> 평가 지표 `val_bpb`는 어휘 크기에 독립적이라 아키텍처 변경 시에도 공정한 비교가 가능하다. 시간 예산은 wall-clock 5분 (컴파일·웜업 제외).

> [!fact] 사실
> Karpathy의 보고에 따르면 630줄 스크립트가 하룻밤 동안 인간 개입 없이 50회 실험을 수행했다 (출처: The New Stack 보도, 2026).

## train.py 구성 요소

`sources/karpathy-autoresearch-train.py` (630줄)에 포함된 주요 기술:

### 모델 아키텍처

> [!fact] 사실
> - **GQA (Grouped Query Attention)** — `n_head`와 `n_kv_head` 분리, KV 헤드 수 줄여 메모리 절감
> - **RoPE (Rotary Position Embedding)** — 사전 계산된 cos/sin 버퍼, bf16
> - **QK-Norm** — Q·K에 RMSNorm 적용 후 어텐션 (수치 안정)
> - **ResFormer Value Embedding** — 짝/홀 레이어에 입력 의존적 게이트로 value embedding 주입
> - **Sliding Window Attention** — `SSSL` 패턴 (short-short-short-long), 마지막 레이어는 항상 full
> - **ReLU² MLP** — `F.relu(x).square()` (GeLU/SiLU 대신)
> - **Logit softcap** — `softcap * tanh(logits / softcap)` (softcap=15) 로짓 폭주 방지
> - **Per-layer residual scalars** — `resid_lambdas`, `x0_lambdas` 학습 가능 (Hyper-Connection 아이디어)

### 옵티마이저 (MuonAdamW)

> [!fact] 사실
> 2D 행렬 파라미터에는 [Muon optimizer](../concepts/muon-optimizer.md), 그 외(임베딩·스칼라)에는 AdamW를 적용하는 단일 옵티마이저 클래스.

> [!fact] 사실
> Muon 핵심 단계:
> 1. **Polar Express orthogonalization** — Newton-Schulz 5스텝 변형, 사전 계산된 5쌍 계수 `(a, b, c)` 사용
> 2. **NorMuon variance reduction** — 행/열 평균 제곱으로 두 번째 모멘트 추정, `rsqrt`로 스텝 크기 조정
> 3. **Cautious weight decay** — `(g * params) >= 0` 마스크로 부호 일치할 때만 decay 적용
> 4. **Nesterov momentum** — `lerp_`로 momentum_buffer와 grad 보간

> [!fact] 사실
> AdamW 단계는 `@torch.compile(fullgraph=True)`로 fused. 0-D CPU 텐서로 하이퍼파라미터를 보관하여 값 변경 시 재컴파일을 피한다.

### Flash Attention 3

> [!fact] 사실
> Hopper(`cap=(9,0)`)에서는 `varunneal/flash-attention-3` 커널, 그 외에서는 `kernels-community/flash-attn3`을 동적 로드.

### 학습 루프

> [!fact] 사실
> - 시간 예산 기반 종료 (`step > 10 and total_training_time >= TIME_BUDGET`)
> - 첫 10 스텝은 컴파일·웜업으로 시간 측정에서 제외
> - LR 스케줄: `WARMUP_RATIO=0`, `WARMDOWN_RATIO=0.5`, `FINAL_LR_FRAC=0` (절반은 평탄, 절반은 0까지 cosine-like 감쇠)
> - Muon momentum: 300 스텝까지 0.85→0.95 선형 증가
> - Weight decay: `WEIGHT_DECAY * (1 - progress)` 선형 감쇠
> - Fast fail: loss NaN 또는 >100이면 즉시 `exit(1)` (실험 시간 낭비 방지)
> - Python GC를 첫 스텝 이후 `gc.disable() + gc.freeze()` (~500ms stall 제거), 5000스텝마다 수동 호출

### 핵심 하이퍼파라미터 (기본값)

> [!fact] 사실
> | 항목 | 값 |
> |---|---|
> | `DEPTH` | 8 |
> | `ASPECT_RATIO` | 64 (model_dim = depth × 64) |
> | `HEAD_DIM` | 128 |
> | `WINDOW_PATTERN` | "SSSL" |
> | `TOTAL_BATCH_SIZE` | 2^19 (~524K tokens) |
> | `EMBEDDING_LR` | 0.6 (Adam) |
> | `UNEMBEDDING_LR` | 0.004 (Adam) |
> | `MATRIX_LR` | 0.04 (Muon) |
> | `WEIGHT_DECAY` | 0.2 (Muon) |
> | `ADAM_BETAS` | (0.8, 0.95) |

## 위키 관점에서의 의의

> [!judgment] 내 판단
> Autoresearch는 [Generator-Evaluator 루프](../principles/generator-evaluator-loop.md)의 또 다른 인스턴스이다. 차이는 평가자(`val_bpb` 측정)가 인간이 아닌 결정론적 지표라는 점, 그리고 생성자(에이전트)가 코드 자체를 수정한다는 점. [Anthropic 하니스 엔지니어링](anthropic-harness-engineering.md)의 Planner-Generator-Evaluator 패턴과 비교하면, Autoresearch는 평가자를 단일 스칼라 지표로 극단적으로 단순화한 사례.

> [!judgment] 내 판단
> 실용적 가치: 단일 파일 학습 코드의 모범 사례. 최신 LLM 학습 기법(Muon, GQA, RoPE, sliding window, ResFormer Value Embedding, ReLU², logit softcap)이 모두 한 파일에 응축되어 있어 reference implementation으로 가치가 높다.

> [!claim] 주장
> Karpathy: "AI 에이전트가 자율적으로 ML 연구를 수행하는 시대의 시작점."
> ※ 반론 가능성: 5분 단일 GPU 학습이라는 극단적 시간 제약은 실제 SOTA 연구와 거리가 멀다. 발견된 개선은 작은 규모에서만 유효할 수 있다.

## 관련 페이지

- [Generator-Evaluator 루프](../principles/generator-evaluator-loop.md) — 자율 실험 루프의 일반적 원리
- [Muon Optimizer](../concepts/muon-optimizer.md) — train.py에서 사용된 행렬 파라미터 옵티마이저
- [에이전트 하니스](../concepts/agent-harness.md) — 자율 에이전트 설계 패턴
- [Andrej Karpathy](../entities/andrej-karpathy.md) — 프로젝트 저자

## 출처

- [autoresearch/train.py 원본 (sources)](../../sources/karpathy-autoresearch-train.py)
- GitHub: `karpathy/autoresearch` (master 브랜치)
- The New Stack 보도: "Karpathy's 630-line Python script ran 50 experiments overnight"
