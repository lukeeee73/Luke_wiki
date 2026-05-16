---
title: "Wiki Index"
created: 2026-04-05
updated: 2026-05-16
tags: [index, meta]
sources: []
---

# Wiki Index

위키의 전체 페이지 카탈로그. 새로운 페이지가 추가되거나 수정될 때마다 업데이트된다.

**판단이 필요할 때**: 먼저 [도메인 인덱스](#domains-도메인-진입점)에서 시작해 `weight: foundational` 페이지부터 읽는다.

---

## Domains — 도메인 진입점

판단 보조를 위한 도메인별 큐레이션 목록. 각 도메인의 원칙 → 프레임워크 → 분석 → 내 판단 순으로 정렬되어 있다.

- [Finance](domains/finance.md) — 투자, 포트폴리오, 자산배분, 매크로경제
- [AI](domains/ai.md) — AI/LLM, 에이전트, 프롬프트 엔지니어링, AI 제품
- [Design](domains/design.md) — 디자인 시스템, UI/UX, 디자인 프로세스

---

## Principles — 핵심 원칙 (`weight: foundational`)

의사결정의 1차 근거가 되는 원리. 가장 먼저 참조한다.

### Finance
- [Risk Parity (위험 균형)](principles/risk-parity.md) — 자산 금액이 아닌 위험 기여도를 균등하게 맞추는 자산배분 원리
- [2×2 경제 환경 프레임](principles/economic-quadrants.md) — 성장/인플레 4분면, 시장 기대 대비 서프라이즈가 자산 가격을 결정한다

### AI
- [Generator-Evaluator 루프](principles/generator-evaluator-loop.md) — 생성자와 평가자를 분리하면 반복 피드백으로 품질이 향상된다
- [LLM Wiki 패턴](principles/llm-wiki-pattern.md) — LLM이 유지보수 비용을 대신 처리함으로써 지식이 구조화된 형태로 축적된다

---

## Concepts — 프레임워크·개념 (`type: framework`)

세상을 설명하는 서술적 모델. 판단의 맥락.

### AI
- [에이전트 하니스](concepts/agent-harness.md) — LLM 에이전트 제어 구조 및 설계 패턴
- [Generator-Evaluator 루프](principles/generator-evaluator-loop.md) → `principles/` 참조
- [Managed Agents](concepts/managed-agents.md) — Anthropic의 호스팅 에이전트 인프라, 뇌와 손의 분리
- [에이전트 Eval 방법론](concepts/agentic-evals.md) — 에이전트 코딩 평가 방법론, 인프라 노이즈 문제
- [Claude Code](concepts/claude-code.md) — Anthropic의 AI 코딩 에이전트
- [음성 기반 AI](concepts/voice-based-ai.md) — 음성 UI와 Voice Stack 기술 동향
- [아첨(Sycophancy)](concepts/sycophancy.md) — LLM이 진실 대신 사용자가 듣기 원하는 말을 하는 경향과 대응 방법
- [Muon Optimizer](concepts/muon-optimizer.md) — 2D 행렬 파라미터 직교화 옵티마이저 (Polar Express + NorMuon + Cautious WD)

### Finance
- [Big Cycle (대순환)](concepts/big-cycle.md) — Ray Dalio의 거시적 역사 순환 프레임워크
- [레버리지와 파생상품](concepts/leverage-and-derivatives.md) — 선물·스왑·레버리지 ETF의 메커니즘과 변동성 끌림

### Design
- [디자인 시스템](concepts/design-system.md) — Design Tokens·Components·Guidelines 3요소 표준화 체계
- [Atomic Design](concepts/atomic-design.md) — Brad Frost의 Atoms→Molecules→Organisms→Templates→Pages 5계층 방법론

---

## Entities — 인물·조직·도구

### AI
- [Anthropic](entities/anthropic.md) — Claude, Claude Code 개발사
- [Andrej Karpathy](entities/andrej-karpathy.md) — AI 연구자, LLM Wiki 패턴 제안자
- [Andrew Ng](entities/andrew-ng.md) — DeepLearning.AI 창립자, The Batch 저자
- [OpenAI](entities/openai.md) — ChatGPT, Sora, Codex 개발사
- [Google DeepMind](entities/google-deepmind.md) — Gemini, Lyria 3 개발사
- [World Labs](entities/world-labs.md) — Marble 생성 월드 모델 개발사

### Finance
- [Ray Dalio](entities/ray-dalio.md) — Bridgewater Associates 창립자, Big Cycle·Risk Parity·All Weather 제안자

---

## Topics — 주제별 요약 (`type: fact-set | claim`)

### AI
- [Anthropic 하니스 엔지니어링](topics/anthropic-harness-engineering.md) — Planner-Generator-Evaluator 3-에이전트 하니스, 장기 실행 에이전트 설계 (2026-04)
- [Anthropic Managed Agents](topics/anthropic-managed-agents.md) — Session·Harness·Sandbox 가상화, Claude Agent SDK 출시 (2026-04)
- [Anthropic 에이전트 Eval 인프라 노이즈](topics/anthropic-infrastructure-noise.md) — Terminal-Bench 6pp 격차, 안정성/역량 효과 구분 (2026-02)
- [Claude Code 세션 관리와 1M 컨텍스트](topics/claude-code-session-management.md) — 컨텍스트 롯, 5가지 세션 전략 (2026-04)
- [Claude 개인 조언 연구](topics/claude-personal-guidance.md) — 1M 대화 분석, 9개 도메인 분포, 아첨 실태(관계 25%·영성 38%), Opus 4.7 개선 (2026-05)
- [Karpathy Autoresearch](topics/karpathy-autoresearch.md) — AI 에이전트의 단일 GPU 자율 ML 실험 루프, 630줄 train.py 분석 (2026-05)
- [The Batch Issue 347](topics/the-batch-issue-347.md) — AI 뉴스 스냅샷 (2026-04)

### Finance
- [Ray Dalio All Weather Portfolio](topics/all-weather-portfolio.md) — 상관관계·Risk Parity·4분면 프레임 기반 전략 (2026-04)
- [Ray Dalio - 세계대전과 Big Cycle 분석](topics/ray-dalio-world-war-big-cycle.md) — 세계대전 진입 경고, 13단계 중 9단계 (`confidence: medium`) (2026-04)

### Design
- [디자인 프로세스 기초](topics/design-process-basics.md) — 4D 프로세스, 7단계 실무 흐름, AI 도구의 위치 (2026-04)

---

## Comparisons — 비교 분석

- [RAG vs LLM Wiki 패턴](comparisons/rag-vs-llm-wiki.md) — 질의 시 검색 vs 수집 시 통합의 트레이드오프

---

## Syntheses — 내 판단 (`type: synthesis`)

원칙+사실+의견을 종합해 내린 판단. 출처보다 내 상황이 반영된 페이지.

- [개인 투자자용 All Weather 변형 포트폴리오](syntheses/personal-all-weather-variant.md) — 4분면 커버리지 유지 + 레버리지 포기 + 성장↑ 약한 가중치 (2026-04)

---

## News — 루틴 자동 수집 (`type: claim`, `confidence: low`)

`indicator_dashboard` 의 `daily-market-analysis` 루틴이 매일 누적하는 watchlist 종목 뉴스 로그. **사람-작성 영역과 분리된 별도 폴더**이며, 모든 항목은 `tags: [routine-news, ...]` 로 식별된다. 검증된 사실은 `topics/` 로 promote 가능. 자세한 규칙: [news/README.md](news/README.md).

- [Watchlist News Dashboard](news/_dashboard.md) — watchlist 전 종목 최신 narrative_score / 핵심 한 줄 (섹터별, 요일별 라운드로빈)
- **빅테크 / 소프트웨어**: [AAPL](news/AAPL.md) · [MSFT](news/MSFT.md) · [GOOGL](news/GOOGL.md) · [AMZN](news/AMZN.md) · [META](news/META.md) · [ORCL](news/ORCL.md) · [CRM](news/CRM.md) · [ADBE](news/ADBE.md) · [IBM](news/IBM.md) · [PLTR](news/PLTR.md)
- **반도체**: [NVDA](news/NVDA.md) · [AMD](news/AMD.md) · [INTC](news/INTC.md) · [QCOM](news/QCOM.md) · [TSM](news/TSM.md) · [ASML](news/ASML.md) · [AMAT](news/AMAT.md) · [LRCX](news/LRCX.md) · [AVGO](news/AVGO.md) · [MU](news/MU.md)
- **자동차 / 모빌리티**: [TSLA](news/TSLA.md) · [TM](news/TM.md) · [F](news/F.md) · [GM](news/GM.md) · [STLA](news/STLA.md) · [HMC](news/HMC.md) · [RIVN](news/RIVN.md) · [NIO](news/NIO.md) · [005380.KS](news/005380.KS.md) · [000270.KS](news/000270.KS.md)
- **바이오 / 제약 / 헬스케어**: [LLY](news/LLY.md) · [NVO](news/NVO.md) · [JNJ](news/JNJ.md) · [PFE](news/PFE.md) · [MRK](news/MRK.md) · [ABBV](news/ABBV.md) · [AZN](news/AZN.md) · [UNH](news/UNH.md) · [TMO](news/TMO.md) · [ABT](news/ABT.md)
- **에너지 / 원자재**: [XOM](news/XOM.md) · [CVX](news/CVX.md) · [COP](news/COP.md) · [SHEL](news/SHEL.md) · [OXY](news/OXY.md) · [SLB](news/SLB.md) · [FCX](news/FCX.md) · [NEM](news/NEM.md) · [LIN](news/LIN.md) · [APD](news/APD.md)
- **금융**: [JPM](news/JPM.md) · [BAC](news/BAC.md) · [WFC](news/WFC.md) · [C](news/C.md) · [GS](news/GS.md) · [MS](news/MS.md) · [V](news/V.md) · [MA](news/MA.md) · [AXP](news/AXP.md) · [BRK-B](news/BRK-B.md)
- **소비재**: [WMT](news/WMT.md) · [COST](news/COST.md) · [KO](news/KO.md) · [PEP](news/PEP.md) · [PG](news/PG.md) · [MO](news/MO.md) · [MCD](news/MCD.md) · [HD](news/HD.md) · [NKE](news/NKE.md) · [SBUX](news/SBUX.md)
- **산업재 / 방산**: [CAT](news/CAT.md) · [DE](news/DE.md) · [BA](news/BA.md) · [LMT](news/LMT.md) · [RTX](news/RTX.md) · [NOC](news/NOC.md) · [HON](news/HON.md) · [GE](news/GE.md) · [UPS](news/UPS.md) · [FDX](news/FDX.md)
- **부동산 (REITs)**: [AMT](news/AMT.md) · [CCI](news/CCI.md) · [PLD](news/PLD.md) · [EQIX](news/EQIX.md) · [DLR](news/DLR.md) · [O](news/O.md) · [SPG](news/SPG.md) · [WELL](news/WELL.md) · [PSA](news/PSA.md) · [VICI](news/VICI.md)
- **통신 / 미디어**: [VZ](news/VZ.md) · [T](news/T.md) · [TMUS](news/TMUS.md) · [CMCSA](news/CMCSA.md) · [CHTR](news/CHTR.md) · [NFLX](news/NFLX.md) · [DIS](news/DIS.md) · [SPOT](news/SPOT.md) · [EA](news/EA.md) · [TTWO](news/TTWO.md)
- **유틸리티 / 전력**: [NEE](news/NEE.md) · [SO](news/SO.md) · [DUK](news/DUK.md) · [AEP](news/AEP.md) · [EXC](news/EXC.md) · [CEG](news/CEG.md) · [VST](news/VST.md) · [SRE](news/SRE.md) · [ED](news/ED.md) · [D](news/D.md)
- **조선 (한국)**: [329180.KS](news/329180.KS.md) · [042660.KS](news/042660.KS.md) · [010140.KS](news/010140.KS.md) · [010620.KS](news/010620.KS.md)
