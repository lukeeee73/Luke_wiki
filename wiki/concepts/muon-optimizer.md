---
title: "Muon Optimizer"
created: 2026-05-07
updated: 2026-05-07
domain: ai
type: framework
weight: reference
confidence: medium
tags: [optimizer, muon, adamw, llm-training, polar-express, normuon]
sources: [sources/karpathy-autoresearch-train.py]
---

# Muon Optimizer

신경망의 **2D 행렬 파라미터** 최적화에 특화된 옵티마이저. AdamW가 모든 파라미터에 같은 적응 학습률을 적용하는 것과 달리, Muon은 그래디언트 행렬을 직교화(orthogonalize)하여 업데이트 방향의 conditioning을 개선한다.

## 핵심 아이디어

> [!fact] 사실
> Muon의 핵심은 momentum-처리된 그래디언트 행렬 G에 대해 직교 근사 `G ≈ U Σ V^T` 의 `U V^T`를 계산하여 업데이트로 사용하는 것이다. 이를 통해 모든 특이값을 1로 평탄화하여 큰 특이값에 끌려가는 편향을 제거한다.

> [!fact] 사실
> 직교화를 SVD가 아닌 **Newton-Schulz 반복**(또는 그 변형)으로 근사한다. 행렬 곱셈만 사용하므로 GPU에서 빠르게 실행 가능.

## Karpathy autoresearch 구현 (`sources/karpathy-autoresearch-train.py`)

### Polar Express 직교화

> [!fact] 사실
> 5스텝 Newton-Schulz 변형. 사전 계산된 5쌍의 계수 `(a, b, c)`를 사용:
> ```python
> polar_express_coeffs = [
>     (8.156554524902461, -22.48329292557795, 15.878769915207462),
>     (4.042929935166739, -2.808917465908714, 0.5000178451051316),
>     (3.8916678022926607, -2.772484153217685, 0.5060648178503393),
>     (3.285753657755655, -2.3681294933425376, 0.46449024233003106),
>     (2.3465413258596377, -1.7097828382687081, 0.42323551169305323),
> ]
> ```
> 각 스텝: `X = a·X + X·(b·A + c·A²)` 여기서 `A = X^T X`.

> [!fact] 사실
> 행렬이 wide(`g.size(-2) > g.size(-1)`)일 때와 tall일 때 곱셈 순서를 바꾼다 (`A = X.mT @ X` vs `A = X @ X.mT`). 메모리·계산 효율 최적화.

> [!fact] 사실
> 정규화: `X = X / (X.norm(...) * 1.02 + 1e-6)` — Newton-Schulz 수렴 조건(특이값 ≤ 1)을 만족시키기 위함.

### NorMuon variance reduction

> [!fact] 사실
> 직교화된 그래디언트에 추가로 두 번째 모멘트 추정을 결합. 행 또는 열 방향 평균 제곱(`v_mean`)을 EMA로 추적하고 `rsqrt`로 스텝 크기를 조정.

### Cautious weight decay

> [!fact] 사실
> 표준 weight decay와 달리, 그래디언트와 파라미터의 부호가 일치할 때만 decay 적용:
> ```python
> mask = (g * stacked_params) >= 0
> stacked_params.sub_(lr * g + lr * wd * stacked_params * mask)
> ```
> 직관: 파라미터를 0 방향으로 밀고 있을 때만 decay가 의미 있다.

### Nesterov momentum

> [!fact] 사실
> `lerp_`로 momentum_buffer 갱신 후, grad에 momentum을 더해 lookahead. PyTorch 표준 SGD의 Nesterov와 동등.

## AdamW와의 결합 (MuonAdamW)

> [!fact] 사실
> Karpathy 구현은 단일 옵티마이저 클래스(`MuonAdamW`)에서 파라미터 그룹별로 분기:
> - `kind='adamw'`: 임베딩, lm_head, value embeddings, 스칼라 (resid_lambdas, x0_lambdas)
> - `kind='muon'`: transformer 블록 내 모든 행렬 파라미터 (Q/K/V/proj, MLP fc/proj)

> [!fact] 사실
> Muon 그룹은 같은 shape끼리 묶어 stack하여 배치 처리:
> ```python
> for shape in sorted({p.shape for p in matrix_params}):
>     group_params = [p for p in matrix_params if p.shape == shape]
> ```
> `torch._foreach_copy_`로 일괄 갱신 → 커널 런치 오버헤드 감소.

> [!fact] 사실
> Muon LR 스케일링: `lr * max(1.0, shape[-2] / shape[-1])**0.5` — 비대칭 행렬에서 큰 차원 비율을 보정.

## 다른 옵티마이저와의 위치

> [!judgment] 내 판단
> Muon은 SOTA pre-training에서 점차 표준이 되어가는 추세. AdamW 대비 학습 속도·최종 손실 모두 개선되었다는 보고가 다수. 단, 임베딩이나 1D 파라미터에는 적용하지 않으므로 항상 AdamW와 결합되는 하이브리드 형태로 사용된다.

> [!claim] 주장
> Muon 제안자 Keller Jordan 외: "matrix optimizer는 행렬 파라미터를 행렬로 다뤄야 한다."
> ※ 반론 가능성: 직교화 비용이 증가하므로 작은 모델에서는 이득이 없을 수 있다. 대규모 학습에서 효과 검증됨.

## 관련 페이지

- [Karpathy Autoresearch](../topics/karpathy-autoresearch.md) — Muon이 사용된 단일 GPU 학습 스크립트
- [Generator-Evaluator 루프](../principles/generator-evaluator-loop.md) — 옵티마이저 선택도 자율 실험 루프의 한 변수

## 출처

- [autoresearch/train.py — MuonAdamW 구현부](../../sources/karpathy-autoresearch-train.py) (293–426행)
