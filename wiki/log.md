---
title: "Wiki Log"
created: 2026-04-05
updated: 2026-06-28
tags: [log, meta]
sources: []
---


# Wiki Log

위키의 모든 작업 이력을 시간순으로 기록합니다.

---

## 2026-06-28

### [INGEST] DSpark & Speculative Decoding

- **작업**: DSpark/speculative decoding 연구 노트(Obsidian 형식)를 수집·정제하여 위키 통합
- **원본 유형**: 개인 연구 노트 (Luke) — DeepSeek-V4-Pro-DSpark / DeepSpec 기반 추론 가속 분석 (status: seed)
- **생성된 파일**:
  - `wiki/concepts/speculative-decoding.md` — 정제 페이지 (`type: framework`, `domain: ai, finance`, `confidence: medium`)
- **업데이트된 파일**:
  - `wiki/domains/ai.md` — 프레임워크 섹션에 추가
  - `wiki/domains/finance.md` — 반도체·AI 칩 가치사슬 섹션에 추가 (HBM 수요 연결)
  - `wiki/entities/deepseek.md` — V4 추론 효율(DSpark) 섹션·교차참조 추가
  - `wiki/concepts/hbm.md` — 추론 가속 ↔ 대역폭 병목 백링크 추가
  - `wiki/index.md` — Concepts/AI 에 신규 페이지 추가
- **주요 내용**:
  1. V4-Pro-DSpark = 동일 가중치 + 드래프트 모듈(≈28GB), lossless 가속
  2. Decode = memory-bound — 가중치 1회 운반으로 N토큰 검증이 이득의 원천
  3. DSpark 두 축: ① Semi-AR 드래프트(로컬 latency) ② Confidence-scheduled 검증(프로덕션 throughput)
  4. MoE 메모리 규칙(활성≠총량), 로컬 구동 사양표, tok/s = 대역폭/토큰당 가중치
  5. 투자 연결: MoE 구조 → HBM 용량·대역폭 수요 비선형 폭발 → 전력 인프라 수요 함수
- **인식론적 처리**: 메커니즘(memory-bound, rejection sampling lossless)은 `[!fact]`, V4/DSpark 성능 수치·풋프린트는 `[!claim]`, 투자 프레임은 `[!judgment]`, 수치 신뢰도 주의는 `[!opinion]` 으로 구분

---

## 2026-06-20

### [INGEST] 중국 반도체 격차 — ASML EUV 의혹·SMIC/화웨이·DeepSeek V4 학습 칩

- **작업**: 미·중 AI 반도체 격차 연구 노트(Obsidian 형식)를 수집·정제하여 위키 통합
- **원본 유형**: 개인 연구 노트 (Luke) — 2026-06 시점 뉴스 기반 분석 (status: research)
- **생성된 파일**:
  - `sources/asml-smic-deepseek-v4-chips.md` — 원본 노트 (불변 보존, frontmatter 정규화 외 내용 유지)
  - `wiki/topics/china-chip-gap-deepseek-v4.md` — 정제 페이지 (`type: claim`, `domain: finance, ai`, `confidence: medium`)
  - `wiki/entities/deepseek.md` — DeepSeek 엔티티 (`type: entity`, `domain: ai, finance`)
- **업데이트된 파일**:
  - `wiki/index.md` — Topics > Finance, Entities > 반도체 섹션에 링크 추가
  - `wiki/domains/finance.md` — 반도체 가치사슬 클러스터에 미·중 격차 + DeepSeek 추가
  - `wiki/domains/ai.md` — AI 하드웨어 섹션에 미·중 격차 + DeepSeek 추가
- **주요 내용**:
  1. **ASML EUV 밀반출** = 미확인 의혹 (증거 비공개). ASML: 314대 전량 소재 파악, 중국 0대. SwaySure 건은 별도 회색지대.
  2. **제조가 진짜 병목**: Kirin 9030 = SMIC N+3(=7nm 확장, "5nm 아님" / TechInsights). EUV 부재 → DUV 다중패터닝, 7nm 수율 20~40%. vs TSMC 2nm 양산.
  3. **화웨이 Ascend** = 물량 집적(parity by aggregation): 950PR(128GB)·950DT(144GB), CloudMatrix 384 ~300 PFLOPs BF16. 대가는 전력·와트당 성능 열위.
  4. **DeepSeek V4 학습 칩**: 공식 비공개, 부인 성명은 H800+Ascend 910C 주장. 1,000개 Ascend 작업 = 사후학습. 사전학습은 엔비디아 의존 지속.
  5. **격차 방향**: 단일칩 910C ~40%, 종합 TPP ~5배, 2027 H2 17배 전망, 물량 ~4%. CFR: 2026 950 로드맵 TPP가 910C보다 낮음 + 910B/C 다수 TSMC 불법 제조 의혹.
- **인식론 처리**: TechInsights 노드 실측은 `[!fact]`, 격차 배수·로드맵·수율은 `[!claim]`(업계 추정 명시), EUV 의혹은 `[!claim]`(미확인), 추론≠학습 구분·병목 진단은 `[!judgment]`, 출처 신뢰도 주의는 `[!opinion]`로 구분
- **핵심 프레임**: "추론(inference) ≠ 학습(training)" 경계를 모든 수치 해석의 1차 필터로 명시 — 가치사슬 종합 §3.3 GPU vs ASIC 이분화와 연결
- **후속 추적 (Open threads)**: EUV 증거 공개 여부, SwaySure 실체, SMIC N+3 수율, Ascend 960 블랙웰급 패리티, V4 후속 사전학습 칩 공개

---

## 2026-06-14

### [INGEST] AI 신약 개발 — 발굴은 압축, 임상은 불변

- **작업**: "AI in 신약 개발" 개인 학습 노트(Obsidian 형식)를 수집·정제하여 위키 통합
- **원본 유형**: 개인 학습 노트 (Luke) — AI 바이오 산업 분석 / 투자 판단용
- **생성된 파일**:
  - `sources/ai-drug-discovery.md` — 원본 학습 노트 (불변 보존, Obsidian `[[wikilink]]` 원형 유지)
  - `wiki/topics/ai-drug-discovery.md` — 정제 페이지 (`type: claim`, `domain: ai, finance`, `confidence: medium`)
- **업데이트된 파일**:
  - `wiki/index.md` — Topics > AI 에 신규 페이지 링크 추가
  - `wiki/domains/ai.md` — 사례/분석 섹션에 링크 추가
  - `wiki/domains/finance.md` — 전문가 주장/분석 섹션에 링크 추가 (경제적 함의 측면)
- **주요 내용**:
  1. **핵심 명제**: "발굴은 압축, 임상은 불변" — AI는 초기 발굴(time-to-clinic)을 압축하나 임상 성공 확률은 못 움직임
  2. **두 개의 엔진**: ① 특화 과학 모델(AlphaFold3 구조 예측 → IsoDDE 친화도·포켓·분자 생성) ② 추론·오케스트레이션(GPT-Rosalind)
  3. **AI 경계의 실증**: 임상 1상 80~90%(전통 40~65%) → 2상 ~40%(산업 평균 회귀). 1상=화학·구조 탐색 문제(AI 강점), 2상=인간 생물학 효능(AI 한계)
  4. **경제적 함의**: 50:1 바이오벅스 비율(헤드라인 5B+ 딜의 실제 계약금 2%) — 시장이 임상 미입증을 가격에 반영. 중국 제약 라이선싱 50:1 구조와 동일 논리
  5. **GPT-Rosalind**: OpenAI 생명과학 첫 모델(2026.04.17), 분자 설계가 아닌 추론 레이어, 이중용도 위험 → 제한 접근 + Rosalind Biodefense
- **인식론 처리**: 임상 성공률·2a상 완료는 `[!fact]`, IsoDDE/OpenAI 발표는 `[!claim]`(반론 가능성 명시), 핵심 명제·한계 구조 분석은 `[!judgment]`로 구분
- **후속 페이지 후보 (미작성)**: 중국 제약 라이선싱, AlphaFold2/3, Jevons Paradox, 복잡성 프리미엄

---

## 2026-06-09

### [INGEST] 반도체·AI 칩 가치사슬 종합 학습 노트

- **작업**: "모래에서 AI 칩까지" 반도체 가치사슬 종합 학습 노트를 수집·정제하여 위키 통합
- **원본 유형**: 개인 학습 노트 (Luke) — 산업 분석/투자 판단용 종합
- **생성된 파일**:
  - `sources/semiconductor-ai-chip-value-chain.md` — 원본 학습 노트 (불변 보존)
  - `wiki/syntheses/semiconductor-ai-chip-value-chain.md` — 가치사슬 종합 (synthesis, `domain: finance, ai`)
  - `wiki/entities/tsmc.md` — TSMC (파운드리 1위, 제조+패키징)
  - `wiki/entities/nvidia.md` — 엔비디아 (AI GPU 지배 팹리스)
  - `wiki/entities/broadcom.md` — 브로드컴 (커스텀 ASIC 설계 1위)
  - `wiki/entities/marvell.md` — 마벨 (커스텀 ASIC 설계 2위)
  - `wiki/concepts/euv-lithography.md` — EUV 노광 / ASML 독점
  - `wiki/concepts/cowos.md` — CoWoS 2.5D 패키징
  - `wiki/concepts/hbm.md` — HBM 고대역폭 메모리
  - `wiki/concepts/cuda.md` — CUDA 소프트웨어 해자
  - `wiki/concepts/serdes.md` — SerDes 인터커넥트 IP
  - `wiki/topics/polysilicon.md` — 폴리실리콘 태양광 vs 반도체 분기 (fact-set)
- **업데이트된 파일**:
  - `wiki/domains/finance.md` — 반도체 가치사슬 섹션 + 종합 페이지 링크 추가
  - `wiki/domains/ai.md` — AI 하드웨어/반도체 섹션 추가
  - `wiki/index.md` — 신규 페이지 11개 추가 (syntheses 1, entities 4, concepts 5, topics 1)
- **주요 내용**:
  1. 두 시장 구분: ① 소재(모래→실리콘메탈→폴리실리콘→웨이퍼, "빈 캔버스") ② 공정(증착→EUV노광→식각, "회로 새기기"). ASML EUV는 ②의 노광 단계
  2. 가치사슬 상단일수록 독점 수렴: 소재(과점)→웨이퍼(5사 82%)→장비(ASML 독점)→제조(TSMC)
  3. 폴리실리콘 분기: 같은 물질이 순도 요구치로 중국 주도 태양광(6N) vs 선진국 과점 반도체(9~11N)로 분리
  4. TSMC 해자 = 공정·수율·capex·신뢰·생태계·패키징이 서로 강화하는 플라이휠
  5. CoWoS가 AI 칩 공급의 실질 병목 (엔비디아 50~60% 선점)
  6. 엔비디아 의존 3중 구조(비용 80%+ 마진 / 공급 할당 / CUDA 소프트웨어)
  7. 시장 이분화: 훈련·연구→GPU, 대량·고정 추론→커스텀 ASIC (브로드컴·마벨 설계)
  8. 브로드컴 vs 마벨: 네트워킹 곱셈 효과로 브로드컴 우위(~70% vs ~20~25%)
  9. "곡괭이와 삽": 승패와 무관하게 TSMC·ASML·HBM·SerDes를 파는 자리가 가장 견고
  10. "줄어드는 비중 × 커지는 파이": 점유율 하락 ≠ 매출 하락(엔비디아)
- **위키 관점 판단**:
  - 위키 최초의 반도체/공급망 산업 분석 자료. 기존 finance(자산배분)·ai(에이전트/모델) 축에 **AI 하드웨어 공급단** 축 추가
  - 종합 페이지의 6개 경제학 원리는 [경제 환경 4분면](principles/economic-quadrants.md)처럼 개별 종목 뉴스를 끼워 넣는 체크리스트로 사용
  - 점유율·capex·매출 수치는 대부분 업계 추정(`confidence: medium`), 점유율 예측 등은 `[!claim]`/`[!opinion]` callout으로 명시
- **비고**: ASML은 별도 엔티티 대신 `concepts/euv-lithography.md`에 통합. watchlist 뉴스(`news/NVDA`, `news/TSM`, `news/AVGO` 등)와 교차 연결 가능 — 추후 promote 시 출처 보강.

### [STRUCTURE] Obsidian vault 정리 및 뉴스 격리 규칙 강화

- **작업**: 공부 노트 저장소 본래 목적을 살리기 위해 Capture → Source → Wiki → Routine 구조로 정리
- **생성된 파일**:
  - `README.md` — vault 지도와 추천 사용 흐름
  - `inbox/README.md` — 임시 캡처 처리 규칙
  - `_templates/study-note.md` — 공부 노트 템플릿
  - `_templates/source-ingest.md` — 원문 수집 템플릿
  - `_templates/news-promotion.md` — 뉴스 승격 템플릿
  - `scripts/validate_vault.py` — vault 구조 검증 스크립트
  - `.obsidian/templates.json` — Obsidian Templates 폴더 설정
- **업데이트된 파일**:
  - `CLAUDE.md` — 루틴 뉴스 격리와 공부 노트 저장 흐름 명시
  - `wiki/index.md` — 운영/뉴스 섹션 간소화 및 잘못 깨질 수 있는 종목별 링크 목록 제거
  - `wiki/news/README.md` — 현재 종목 파일명 규칙과 검증 명령 추가
- **삭제된 파일**:
  - `news/010140.KS.md` — 최상위 `news/` 아래 빈 중복 파일
  - `wiki/news/JNJ.md` — frontmatter 없는 빈 중복 뉴스 파일
  - `무제.md` — 루트의 빈 무제 노트

---

## 2026-06-05

### [ROUTINE-NEWS] Daily Market Analysis — 금요일 (에너지 / 원자재 + 유틸리티 / 전력)

- **처리 섹터**: 에너지 / 원자재 (10종목), 유틸리티 / 전력 (10종목)
- **처리 종목 수**: 20종목
- **업데이트된 파일**:
  - `wiki/news/XOM - Exxon Mobil Corporation.md` — 텍사스 이전 확정 + 가이아나 900k bpd
  - `wiki/news/CVX - Chevron Corporation.md` — 싱가포르 정제 매각 + 가스 비중 확대
  - `wiki/news/COP - ConocoPhillips.md` — 생산 가이던스 1.5% 하향 + 포트아서 LNG 임박
  - `wiki/news/SHEL - Shell plc.md` — 자사주 매입 지속 + Q1 배당 $0.3906
  - `wiki/news/OXY - Occidental Petroleum.md` — CEO 교체 + 멕시코만 Bandit 발견
  - `wiki/news/SLB - Schlumberger Limited.md` — Tachyus AI 인수 vs Q2 EPS -28.4% YoY
  - `wiki/news/FCX - Freeport-McMoRan.md` — Grasberg 복구 지연 + UBS 목표주가 $75
  - `wiki/news/NEM - Newmont Corporation.md` — Q1 FCF $31억 기록 + $60억 자사주매입 ★ 사실 누적 추가
  - `wiki/news/LIN - Linde plc.md` — Q1 EPS +10% + 삼성 반도체 팹 최대 딜
  - `wiki/news/APD - Air Products and Chemicals.md` — Q2 EPS +19% + 웰스파고 OW 상향
  - `wiki/news/NEE - NextEra Energy.md` — Dominion $670억 합병 + -13.7% 주가 압박
  - `wiki/news/SO - The Southern Company.md` — 조지아파워 요금 인하 vs Vogtle 운전
  - `wiki/news/DUK - Duke Energy Corporation.md` — AI 데이터센터 원전 공급 협의
  - `wiki/news/AEP - American Electric Power.md` — Q1 +7.3% + $417억 4년 자본투자
  - `wiki/news/EXC - Exelon Corporation.md` — PECO 요금 철회 + 송전 $1.5B 증액
  - `wiki/news/CEG - Constellation Energy.md` — 5,650MW 원전 PPA + YTD -25% 역발상
  - `wiki/news/VST - Vistra Corp.md` — Meta 20년 PPA + 로터스 가스발전 인수
  - `wiki/news/SRE - Sempra.md` — Voss Capital Oncor 분리 촉구
  - `wiki/news/ED - Consolidated Edison.md` — 뉴스 없음 (안정 인컴주)
  - `wiki/news/D - Dominion Energy.md` — NEE 합병 + 130GW AI 파이프라인
  - `wiki/news/_dashboard.md` — 에너지/원자재 + 유틸리티/전력 섹터 행 갱신
- **주요 시그널**:
  - OPEC+ 6/7 증산 결정 시 에너지 5종목 동시 하방 리스크
  - AI 원전 PPA 테마 (CEG, VST, DUK) 유틸리티 섹터 신성장 동력으로 부상
  - NEE-D 합병 (세계 최대 규제 유틸리티) 규제 승인 진행 중
  - NEM Q1 FCF $31억 기록 — 금값 $4,900 고점에서 역대 최고 실적

---

## 2026-05-07

### [INGEST] Karpathy Autoresearch — 자율 ML 실험 루프 train.py

- **작업**: Andrej Karpathy의 `karpathy/autoresearch` 저장소 `train.py` 수집 및 위키 통합
- **원본 URL**: https://github.com/karpathy/autoresearch/blob/master/train.py (master, 630줄)
- **수집 방법**: `curl` raw.githubusercontent.com 직접 다운로드
- **생성된 파일**:
  - `sources/karpathy-autoresearch-train.py` - 원본 Python 코드 (불변, 26KB)
  - `wiki/topics/karpathy-autoresearch.md` - autoresearch 프로젝트 + train.py 구성 분석 (fact-set)
  - `wiki/concepts/muon-optimizer.md` - Muon 옵티마이저 개념 페이지 (framework)
- **업데이트된 파일**:
  - `wiki/entities/andrej-karpathy.md` - autoresearch 섹션 추가, sources 확장
  - `wiki/domains/ai.md` - 신규 2개 페이지 링크 추가
  - `wiki/index.md` - concepts 1개, topics 1개 추가
- **주요 내용**:
  1. Autoresearch 작동 원리: 에이전트가 train.py 수정 → 5분 학습 → val_bpb 측정 → 채택/폐기 → 반복. 하룻밤 50회 자율 실험
  2. train.py 모델 아키텍처: GQA, RoPE, QK-Norm, ResFormer Value Embedding, Sliding Window (SSSL), ReLU² MLP, Logit softcap, per-layer residual scalars
  3. MuonAdamW 옵티마이저: 2D 행렬엔 Muon, 그 외엔 AdamW
  4. Muon 핵심 단계: Polar Express orthogonalization (5스텝 NS 변형) + NorMuon variance reduction + Cautious weight decay + Nesterov momentum
  5. Flash Attention 3 동적 로드 (Hopper vs 비-Hopper)
  6. 학습 루프 특징: 시간 예산 기반 종료, fast fail (loss > 100), GC freeze/disable로 ~500ms stall 제거
  7. `@torch.compile(fullgraph=True)` + 0-D CPU 텐서로 재컴파일 회피
- **위키 관점 판단**:
  - Generator-Evaluator 루프의 또 다른 인스턴스 (평가자를 결정론적 스칼라 지표로 극단 단순화)
  - 단일 파일 LLM 학습 reference implementation으로 가치 높음
- **비고**: 위키 최초의 ML 학습 시스템 코드 자료. 기존 AI 도메인이 에이전트·하니스·평가 중심이었다면, 이번 ingest로 모델 학습·옵티마이저 축이 추가됨.

---

## 2026-05-02

## 2026-05-02

### [RESTRUCTURE] 위키 판단 보조 구조로 확장 — 인식론적 계층 + 도메인 인덱스 도입

- **목적**: 단순 지식 저장에서 **판단 보조** 도구로 위키 진화. 투자·AI 관련 의사결정 시 원칙/사실/의견을 구분하고 중요도에 따라 가중치를 둔 정보 종합이 가능하도록 구조화.

- **변경 사항**:

  1. **CLAUDE.md 전면 개정** — 도메인 정의, 인식론적 분류 규칙(type/weight/confidence), Obsidian callout 문법 추가, Query 시 weight 기반 우선순위 규칙 추가

  2. **신규 폴더 `wiki/principles/`** — 의사결정의 1차 근거가 되는 원칙 페이지 전용 폴더
     - `concepts/risk-parity.md` → `principles/risk-parity.md` (callout 적용)
     - `concepts/economic-quadrants.md` → `principles/economic-quadrants.md` (callout 적용)
     - `concepts/generator-evaluator-loop.md` → `principles/generator-evaluator-loop.md` (callout 적용)
     - `concepts/llm-wiki-pattern.md` → `principles/llm-wiki-pattern.md` (callout 적용)

  3. **신규 폴더 `wiki/domains/`** — 도메인별 진입점 인덱스 (weight 순 정렬)
     - `domains/finance.md` 생성
     - `domains/ai.md` 생성
     - `domains/design.md` 생성

  4. **Obsidian CSS 스니펫** — `.obsidian/snippets/epistemic.css` 생성
     - `[!principle]` 골드, `[!fact]` 블루, `[!claim]` 주황, `[!opinion]` 회색, `[!judgment]` 그린

  5. **Frontmatter 전체 보강** — 기존 31개 위키 페이지 + 머지된 신규 2개 페이지(`sycophancy.md`, `claude-personal-guidance.md`)에 `domain`, `type`, `weight`, `confidence` 필드 추가

  6. **Callout 적용** — 우선순위 페이지:
     - `principles/risk-parity.md`: `[!principle]`, `[!fact]`, `[!claim]` 적용
     - `principles/economic-quadrants.md`: `[!principle]`, `[!judgment]` 적용
     - `principles/generator-evaluator-loop.md`: `[!principle]`, `[!fact]` 적용
     - `principles/llm-wiki-pattern.md`: `[!principle]` 적용
     - `syntheses/personal-all-weather-variant.md`: `[!judgment]` 적용

  7. **내부 링크 일괄 수정** — 이동된 4개 페이지를 참조하는 모든 파일의 경로 업데이트 (약 20개 링크)

  8. **`wiki/index.md` 전면 개정** — 도메인 진입점 섹션 추가, 폴더 구조 반영

- **영향 파일**: 총 40개 이상 (생성 8개, 수정 34개)

### [INGEST] Anthropic 개인 조언 연구 - Claude 아첨 실태 분석

- **작업**: Anthropic Research "How people ask Claude for personal guidance" 수집 및 위키 통합
- **원본 URL**: https://www.anthropic.com/research/claude-personal-guidance
- **발행**: Anthropic Research, 2026년 5월 1일경
- **생성된 파일**:
  - `sources/claude-personal-guidance.md` - 원본 자료 요약
  - `wiki/topics/claude-personal-guidance.md` - 개인 조언 연구 주제 페이지
  - `wiki/concepts/sycophancy.md` - 아첨(sycophancy) 개념 페이지 (신규)
- **업데이트된 파일**:
  - `wiki/entities/anthropic.md` - 개인 조언 연구 섹션 추가
  - `wiki/index.md` - 신규 페이지 2개(topics 1, concepts 1) 추가
- **주요 내용**:
  - 데이터: 2026년 3~4월 claude.ai 1M 대화 → 63만 9천 건(고유 사용자) → 3만 8천 건(개인 조언, 6%)
  - 9개 도메인 분류; 건강(27%)·커리어(26%)·관계(12%)·재정(11%) = 76% 집중
  - 전체 아첨율 9%; 영성 38%, 관계 25%가 이상값
  - 아첨 패턴: 상대방 비난 동조, 로맨틱 의도 과잉 해석
  - Opus 4.7 / Mythos Preview 훈련에 합성 데이터 적용 → 관계 아첨 50%↓, 전 도메인 일반화

---

## 2026-04-19

### [INGEST] Claude Code 세션 관리와 1M 컨텍스트 블로그 포스트

- **작업**: Anthropic 공식 블로그 "Using Claude Code: session management and 1M context" 수집 및 위키 통합
- **원본 URL**: https://claude.com/blog/using-claude-code-session-management-and-1m-context
- **저자**: Thariq Shihipar (Anthropic Claude Code 팀, Member of Technical Staff)
- **원본 발행일**: 2026-04-15
- **생성된 파일**:
  - `sources/claude-code-session-management-1m-context.md` - 원본 자료 요약
  - `wiki/topics/claude-code-session-management.md` - 세션 관리 주제 페이지
- **업데이트된 파일**:
  - `wiki/concepts/claude-code.md` - 세션 관리 섹션 추가, 태그·출처 업데이트
  - `wiki/index.md` - 신규 topics 페이지 1개 추가
- **주요 내용**:
  1. 컨텍스트 롯(Context Rot): 세션이 길어질수록 어텐션 분산 → 성능 저하. 1M 창이 만능이 아님
  2. 5가지 전략: Continue(모두 필요) / /rewind(시점 복귀) / /compact(요약 교체) / /clear(초기화) / Subagents(결론만 위임)
  3. /compact는 방향 지정 가능: `/compact focus on X, drop Y`
  4. 서브에이전트: 자체 깨끗한 컨텍스트로 독립 실행 → 결론만 상위에 반환
  5. 핵심 판단 기준: "이 도구 출력이 다시 필요할까, 아니면 결론만 필요할까?"
  6. /usage 명령어 함께 출시: 세션 컨텍스트 사용량 확인
- **비고**: Claude Code 세션 관리의 공식 레퍼런스. 기존 claude-code.md 개념 페이지와 Managed Agents, 에이전트 하니스 페이지와 교차 연결.

---

## 2026-04-18

### [INGEST] 디자인 프로세스 기초 학습 노트

- **작업**: 디자이너·PM 협업 방식과 UI/UX 핵심 용어를 정리한 개인 학습 노트 수집 및 위키 통합
- **원본 유형**: 개인 학습 노트 (Luke) — Claude Design 같은 AI 디자인 도구 활용을 위한 선행 지식
- **생성된 파일**:
  - `sources/design-process-basics.md` - 원본 학습 노트
  - `wiki/topics/design-process-basics.md` - 디자인 프로세스 기초 주제 페이지
  - `wiki/concepts/design-system.md` - 디자인 시스템 개념 페이지 (Design Tokens·Components·Guidelines)
  - `wiki/concepts/atomic-design.md` - Atomic Design 방법론 개념 페이지 (Brad Frost 5계층)
- **업데이트된 파일**:
  - `wiki/index.md` - 신규 페이지 3개 추가 (concepts 2, topics 1)
- **주요 내용**:
  1. 4D 매크로 프로세스: Discovery → Define → Design → Deliver (경제학의 문제 정의 → 모델링 → 실증 → 정책 제언과 구조적 동형)
  2. 역할 분담: PM(무엇을·왜, PRD) / 디자이너(어떻게, Wireframe·Mockup·Prototype) / 개발자(구현)
  3. 실무 7단계: User Research → Journey/Flow → IA → Wireframe → Mockup → Prototype → Handoff (뒤로 갈수록 수정 비용 기하급수적 증가)
  4. 디자인 시스템 3요소: Design Tokens(변수, CSS 변수와 1:1) / Components(조립식 부품) / Guidelines(사용 규칙). 대표 사례: Material Design, Apple HIG, Polaris
  5. Atomic Design 5계층: Atoms(버튼) → Molecules(검색창) → Organisms(헤더) → Templates(레이아웃) → Pages(실제 화면). Templates까지 추상, Pages부터 구체
  6. 시각 체계: Typography(font family/weight/line-height/scale), Spacing("8-point grid", 4/8px 배수), Color(Primary/Secondary/Neutral/Semantic)
  7. 핵심 용어: Hierarchy, White Space, Affordance(Don Norman), Accessibility(WCAG 4.5:1), Responsive(640/768/1024/1280), State(6종 — Default/Hover/Active/Disabled/Loading/Focus)
  8. AI 디자인 도구의 위치: Wireframe→Mockup→Prototype 구간을 분 단위로 압축. 단, 문제 정의·사용자 관점·비즈니스 정합성 판단은 사람의 영역 — Generator-Evaluator 루프의 또 다른 인스턴스
- **비고**: 위키 최초의 디자인/UX 분야 자료. 기존 AI·매크로 경제 중심에서 주제 다양화. Generator-Evaluator 루프 개념과 교차 연결.

---

## 2026-04-12

### [INGEST] Ray Dalio All Weather Portfolio 개인 학습 노트

- **작업**: Ray Dalio의 All Weather Portfolio 프레임워크 학습 노트 수집 및 위키 통합
- **원본 유형**: 개인 학습 노트 (Luke)
- **생성된 파일**:
  - `sources/ray-dalio-all-weather-portfolio.md` - 원본 학습 노트
  - `wiki/topics/all-weather-portfolio.md` - All Weather Portfolio 주제 페이지
  - `wiki/concepts/risk-parity.md` - Risk Parity (위험 균형) 개념 페이지
  - `wiki/concepts/economic-quadrants.md` - 2×2 경제 환경 프레임 개념 페이지
  - `wiki/concepts/leverage-and-derivatives.md` - 레버리지와 파생상품 개념 페이지
  - `wiki/syntheses/personal-all-weather-variant.md` - 개인 투자자용 변형 포트폴리오 (최초 syntheses 페이지)
- **업데이트된 파일**:
  - `wiki/entities/ray-dalio.md` - All Weather 섹션 추가, 관련 페이지 확장
  - `wiki/index.md` - 신규 페이지 5개 추가 (concepts 3, topics 1, syntheses 1)
- **주요 내용**:
  1. All Weather의 3가지 핵심 아이디어: ① 저상관 자산 결합의 "공짜 점심" ② Risk Parity (위험 기여도 균등) ③ 성장/인플레 2×2 프레임
  2. 4분면별 유리 자산 매핑: 성장↑인플레↑ (원자재·신흥국) / 성장↑인플레↓ (주식) / 성장↓인플레↑ (TIPS·금) / 성장↓인플레↓ (장기국채)
  3. 파생상품 메커니즘: 국채 선물(증거금 5%로 20배 레버리지), 금리 스왑(현금흐름만 교환), 레버리지 ETF의 변동성 끌림(100→110→99 = −1%지만 TQQQ는 −9%)
  4. 개인 투자자용 변형: 레버리지 포기, 채권 55→15%, 금 7.5→15%, 주식 55%로 상향, 4분면 커버리지 유지
  5. 분면 판단 지표: 성장(PMI·장단기 금리차·실업률), 인플레(BEI·CPI·원유). "절대 수준이 아니라 시장 기대 대비 서프라이즈"
  6. 한국 투자자 리밸런싱 팁: 매도 시 세금 발생하므로 추가 납입금으로 부족 자산 매수
- **비고**: 위키의 첫 syntheses 페이지 등록. Ray Dalio 엔티티의 두 번째 자료 (이전 Big Cycle/세계대전 분석에 이어 자산배분 프레임워크 축 추가).

---

## 2026-04-11 (3차 업데이트)

### [INGEST] Ray Dalio "The Big Thing: We Are In A World War" LinkedIn 아티클

- **작업**: Ray Dalio의 LinkedIn/Substack 장문 분석 수집 및 위키 통합
- **원본 URL**: https://www.linkedin.com/pulse/big-thing-we-world-war-isnt-going-end-anytime-soon-ray-dalio-sbrqe
- **Substack URL**: https://raydalio.substack.com/p/the-big-thing-we-are-in-a-world-war
- **원본 발행일**: 2026-04-07 (추정)
- **수집 방법**: LinkedIn 직접 접근 불가(403)로 다수 매체 보도 종합 (Time, Yahoo Finance, Benzinga, IBTimes 등)
- **생성된 파일**:
  - `sources/ray-dalio-world-war-big-thing.md` - 원본 자료 종합 요약
  - `wiki/topics/ray-dalio-world-war-big-cycle.md` - 세계대전과 Big Cycle 분석 주제 페이지
  - `wiki/entities/ray-dalio.md` - Ray Dalio 엔티티 페이지
  - `wiki/concepts/big-cycle.md` - Big Cycle (대순환) 개념 페이지
- **업데이트된 파일**:
  - `wiki/index.md` - 신규 페이지 3개 추가 (concepts 1, entities 1, topics 1)
- **주요 내용**:
  1. 세계는 이미 세계대전 상태: 4개의 실전(러시아-우크라이나, 이스라엘-가자, 예멘-수단, 미국-이란) + 다수의 비실전(무역·경제·기술전)
  2. Big Cycle 13단계 중 9단계(동시다발적 다전역 분쟁)에 위치, 1913-14년·1938-39년과 유사
  3. 동맹 양극화: 중국·러시아·이란·북한 vs 미국·유럽·이스라엘·GCC·일본·호주
  4. 미국 과잉 확장: 750-800개 해외 기지(70-80개국) vs 중국 1개
  5. 확률 평가: 5년 내 주요 분쟁 >50%, 미중 충돌 30-40% (최고 위험: 2028년)
  6. 시장은 이러한 지정학적 리스크를 전혀 가격에 반영하지 않고 있음
- **비고**: 위키 최초의 지정학/매크로 경제 분야 자료. 기존 AI/ML 중심에서 주제 다양화.

---

## 2026-04-11 (2차 업데이트)

### [INGEST] Anthropic 인프라 노이즈 블로그 포스트

- **작업**: Anthropic 엔지니어링 블로그 "Quantifying infrastructure noise in agentic coding evals" 수집 및 위키 통합
- **원본 URL**: https://www.anthropic.com/engineering/infrastructure-noise
- **원본 발행일**: 2026-02
- **생성된 파일**:
  - `sources/anthropic-infrastructure-noise.md` - 원본 자료 요약
  - `wiki/topics/anthropic-infrastructure-noise.md` - 블로그 포스트 통합 분석
  - `wiki/concepts/agentic-evals.md` - 에이전트 Eval 방법론 개념 페이지
- **업데이트된 파일**:
  - `wiki/entities/anthropic.md` - 인프라 노이즈 연구 섹션 추가
  - `wiki/index.md` - 신규 페이지 2개 추가
- **주요 내용**:
  1. Terminal-Bench 2.0을 GKE에서 6가지 자원 구성으로 실행 → 1x 엄격 ~ 무제한 간 6pp 격차 (p < 0.01)
  2. 인프라 오류율: 1x 엄격 5.8% → 무제한 0.5% (단조 감소)
  3. 두 효과 구분: ~3x 이하 = 안정성 효과(spurious failure 제거), ~3x 초과 = 역량 효과(새 문제 풀이 가능)
  4. 최상위 모델 간 리더보드 격차(1~3pp)가 6pp 노이즈 범위 내 → 인프라 통제 없이 순위 신뢰 불가
  5. 권고: 자원 구성을 1등급 실험 변수로 문서화; 3pp 이하 격차는 구성 일치 확인 전 유보

---

## 2026-04-11

### [INGEST] Anthropic Managed Agents 블로그 포스트

- **작업**: Anthropic 엔지니어링 블로그 "Scaling Managed Agents: Decoupling the brain from the hands" 수집 및 위키 통합
- **원본 URL**: https://www.anthropic.com/engineering/managed-agents
- **원본 발행일**: 2026-04-08
- **생성된 파일**:
  - `sources/anthropic-managed-agents.md` - 원본 자료 요약
  - `wiki/topics/anthropic-managed-agents.md` - 블로그 포스트 통합 분석
  - `wiki/concepts/managed-agents.md` - Managed Agents 개념 페이지
- **업데이트된 파일**:
  - `wiki/concepts/agent-harness.md` - 메타-하니스 패턴 섹션 추가
  - `wiki/entities/anthropic.md` - Managed Agents 출시 섹션 추가, 제품 목록 업데이트
  - `wiki/index.md` - 신규 페이지 2개 추가
- **주요 내용**:
  1. Managed Agents = Session·Harness·Sandbox 3요소 가상화 → "뇌(Claude)와 손(실행환경) 분리"
  2. 지연 프로비저닝으로 p50 TTFT 60%↓, p95 TTFT 90%+↓ 성능 개선
  3. Session: append-only 이벤트 로그, `getEvents()`로 위치 기반 컨텍스트 조회
  4. 메타-하니스 철학: 인터페이스(session + sandbox)에만 의견, 특정 하니스에는 무관심
  5. 멀티-에이전트: 서브에이전트(동일 세션) vs 에이전트 팀(독립 컨텍스트)
  6. Claude Code SDK → Claude Agent SDK로 이름 변경
  7. 서비스: 공개 베타, $0.08/세션시간 + 표준 토큰 비용

---

## 2026-04-05 (2차 업데이트)

### [INGEST] Anthropic 하니스 엔지니어링 블로그 포스트

- **작업**: Anthropic 엔지니어링 블로그 2편 수집 및 위키 통합
- **원본 URL 1**: https://www.anthropic.com/engineering/harness-design-long-running-apps
- **원본 URL 2**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **생성된 파일**:
  - `sources/anthropic-harness-design-long-running-apps.md` - 원본 자료 요약
  - `wiki/topics/anthropic-harness-engineering.md` - 두 블로그 포스트 통합 분석
  - `wiki/concepts/agent-harness.md` - 에이전트 하니스 개념 페이지
  - `wiki/concepts/generator-evaluator-loop.md` - Generator-Evaluator 루프 개념 페이지
- **업데이트된 파일**:
  - `wiki/entities/anthropic.md` - 하니스 엔지니어링 섹션 추가
  - `wiki/index.md` - 신규 페이지 3개 추가
- **주요 내용**:
  1. GAN에서 영감받은 Planner-Generator-Evaluator 3-에이전트 하니스 설계
  2. Evaluator가 Playwright MCP로 실행 중인 앱 직접 테스트 (정적 코드 검토 대신)
  3. 프론트엔드 평가 기준 분해: 디자인 품질·독창성·장인정신·기능성
  4. 성능 비교: Solo($9, 20분) vs Full Harness($200, 6시간) — 완성도에서 큰 차이
  5. 멀티 세션 연속성 패턴: claude-progress.txt, feature_list.json, init.sh
  6. 모델 발전에 따른 하니스 단순화 경향 (Opus 4.5 이후)

---

## 2026-04-05

### [INIT] 위키 저장소 초기화

- **작업**: 지식 저장소 초기 구조 생성
- **설명**: Andrej Karpathy의 LLM Wiki 패턴을 기반으로 3계층 구조(Sources/Wiki/Schema) 설정
- **생성된 파일**:
  - `CLAUDE.md` - Schema Layer (위키 운영 규칙)
  - `wiki/index.md` - 위키 인덱스
  - `wiki/log.md` - 작업 이력 (이 파일)
  - `sources/.gitkeep` - 원본 자료 디렉토리
  - 위키 하위 디렉토리: concepts, entities, topics, comparisons, syntheses

---

### [INGEST] The Batch Issue 347

- **작업**: DeepLearning.AI The Batch 347호 수집 및 위키 통합
- **원본 URL**: https://www.deeplearning.ai/the-batch/issue-347/
- **이슈 제목**: Claude Code's Source Leaks, OpenAI Exits Video Generation, Gemini Adds Music Generation, and more...
- **생성된 파일**:
  - `sources/the-batch-issue-347.md` - 원본 자료 요약
  - `wiki/topics/the-batch-issue-347.md` - 이슈 전체 요약
  - `wiki/concepts/claude-code.md` - Claude Code 아키텍처 및 소스 유출 사건
  - `wiki/concepts/voice-based-ai.md` - 음성 기반 AI 동향 (Andrew Ng 관점)
  - `wiki/entities/anthropic.md` - Anthropic 엔티티 페이지
  - `wiki/entities/openai.md` - OpenAI 엔티티 페이지 (Sora 종료 포함)
  - `wiki/entities/google-deepmind.md` - Google DeepMind 엔티티 페이지 (Lyria 3 포함)
  - `wiki/entities/world-labs.md` - World Labs 엔티티 페이지 (Marble, Chisel)
  - `wiki/entities/andrew-ng.md` - Andrew Ng 엔티티 페이지
- **업데이트된 파일**:
  - `wiki/index.md` - 신규 페이지 9개 추가
- **주요 내용**:
  1. Claude Code 소스 유출 (Kairos, autoDream, 언더커버 모드 등 미공개 기능 노출)
  2. OpenAI Sora 종료 (2026-04-26 웹/앱, 2026-09-24 API)
  3. Google Lyria 3 출시 (텍스트/이미지 → 음악, 잠재 확산 기반)
  4. World Labs Marble + Chisel 공개 (영구적 편집 가능 3D 세계 생성)
  5. Andrew Ng의 음성 UI 부상 전망
