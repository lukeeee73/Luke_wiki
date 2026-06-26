---
title: "Finance Domain Index"
created: 2026-05-02
updated: 2026-06-26
domain: finance
type: index
weight: foundational
confidence: high
tags: [도메인, 투자, 포트폴리오, 매크로, 금융]
sources: []
---

# Finance — 도메인 인덱스

투자, 포트폴리오, 자산배분, 매크로경제 관련 모든 페이지의 진입점.
**판단이 필요할 때 이 페이지에서 시작한다** — 원칙 → 프레임워크 → 데이터 → 내 판단 순으로 읽는다.

---

## 핵심 원칙 (최우선 참조)

의사결정의 1차 근거. 이것이 틀리면 결론이 바뀐다.

- [Risk Parity (위험 균형)](../principles/risk-parity.md) — 자산 금액이 아닌 위험 기여도를 균등하게 맞추는 자산배분 원리
- [2×2 경제 환경 프레임](../principles/economic-quadrants.md) — 성장/인플레 4분면, 시장 기대 대비 서프라이즈가 자산 가격을 결정한다

---

## 프레임워크 / 개념

세상을 설명하는 서술적 모델. 원칙을 이해하는 맥락.

- [Big Cycle (대순환)](../concepts/big-cycle.md) — Ray Dalio의 제국 흥망 500년 역사 패턴
- [레버리지와 파생상품](../concepts/leverage-and-derivatives.md) — 선물·스왑·레버리지 ETF의 메커니즘과 위험

---

## 전문가 주장 / 분석 (출처 기반, 검증 필요)

- [Ray Dalio - 세계대전과 Big Cycle 분석](../topics/ray-dalio-world-war-big-cycle.md) — 현재 세계 질서가 대전환점에 있다는 분석 (`confidence: medium`)
- [Ray Dalio All Weather Portfolio](../topics/all-weather-portfolio.md) — All Weather의 설계 원리와 실제 구성
- [AI 신약 개발 — 발굴은 압축, 임상은 불변](../topics/ai-drug-discovery.md) — AI 신약 투자의 50:1 바이오벅스 비율, 임상 미입증을 시장이 가격에 반영 (`domain: ai, finance`, 2026-06)

---

## 내 판단 / 종합

내가 원칙+사실+의견을 종합해 내린 판단.

- [개인 투자자용 All Weather 변형](../syntheses/personal-all-weather-variant.md) — 레버리지 없이 4분면을 커버하는 개인용 포트폴리오
- [반도체·AI 칩 가치사슬 종합](../syntheses/semiconductor-ai-chip-value-chain.md) — 모래에서 AI 칩까지, 어디에 협상력·마진·해자가 집중되는가 (`domain: finance, ai`)
- [AI 전력 병목과 변압기 가치사슬 종합](../syntheses/ai-power-transformer-value-chain.md) — 발전→송전→변압기→데이터센터, 진짜 병목은 GOES·OLTC·부싱·인력 (`domain: finance, ai`)

---

## 반도체·AI 칩 가치사슬 (`domain: finance, ai`)

AI 반도체 투자 판단을 위한 가치사슬 지도. 진입점은 위 [종합 페이지](../syntheses/semiconductor-ai-chip-value-chain.md).

- **기업**: [TSMC](../entities/tsmc.md) · [엔비디아](../entities/nvidia.md) · [브로드컴](../entities/broadcom.md) · [마벨](../entities/marvell.md) · [DeepSeek](../entities/deepseek.md)
- **기술/개념**: [EUV 노광(ASML)](../concepts/euv-lithography.md) · [CoWoS](../concepts/cowos.md) · [HBM](../concepts/hbm.md) · [CUDA](../concepts/cuda.md) · [SerDes](../concepts/serdes.md)
- **소재 시장**: [폴리실리콘 — 태양광 vs 반도체 분기](../topics/polysilicon.md)
- **미·중 격차**: [중국 반도체 격차 — ASML EUV 의혹·SMIC/화웨이·DeepSeek V4 학습 칩](../topics/china-chip-gap-deepseek-v4.md) — 추론은 화웨이로, 사전학습은 엔비디아 의존 (2026-06)

---

## AI 전력 인프라 / 변압기 (`domain: finance, ai`)

AI 데이터센터의 전력 병목 지도. 반도체 가치사슬의 자매편 — "칩"이 아니라 "그 칩을 돌릴 전기"가 어디서 막히는가. 진입점은 [AI 전력 병목과 변압기 가치사슬 종합](../syntheses/ai-power-transformer-value-chain.md).

- **핵심 병목**: 발전→송전→**변압기(765kV)**→데이터센터 사슬 중 변압기가 가장 느림. 진짜 진앙은 완성품이 아니라 소재(GOES)·부품(MR의 OLTC, Trench의 부싱)·숙련 인력.
- **기업 층위**: 한국 4사(효성중공업·HD현대일렉트릭·LS일렉트릭·일진전기)는 "조립·통합" 층의 미국 시장 강자이나, 구조적 해자는 상류(Cleveland-Cliffs/POSCO·MR·Trench)에 있음.

---

## 관련 인물

- [Ray Dalio](../entities/ray-dalio.md) — Bridgewater 창립자, All Weather·Risk Parity·Big Cycle 제안자

---

## Watchlist 뉴스 로그 (루틴 자동 수집, `confidence: low`)

`indicator_dashboard` 의 `daily-market-analysis` 루틴이 매일 누적한다. **검증되지 않은 raw 상태이므로 `news/` 폴더로 격리**되어 있으며, 굳어진 사실만 사람이 직접 `topics/` 로 promote 한다. 자세한 규칙: [news/README.md](../news/README.md).

- [Watchlist News Dashboard](../news/_dashboard.md) — watchlist 전 종목 한눈에 보기 (섹터별, 요일별 라운드로빈)
- **빅테크 / 소프트웨어**: [AAPL](../news/AAPL.md) · [MSFT](../news/MSFT.md) · [GOOGL](../news/GOOGL.md) · [AMZN](../news/AMZN.md) · [META](../news/META.md) · [ORCL](../news/ORCL.md) · [CRM](../news/CRM.md) · [ADBE](../news/ADBE.md) · [IBM](../news/IBM.md) · [PLTR](../news/PLTR.md)
- **반도체**: [NVDA](../news/NVDA.md) · [AMD](../news/AMD.md) · [INTC](../news/INTC.md) · [QCOM](../news/QCOM.md) · [TSM](../news/TSM.md) · [ASML](../news/ASML.md) · [AMAT](../news/AMAT.md) · [LRCX](../news/LRCX.md) · [AVGO](../news/AVGO.md) · [MU](../news/MU.md)
- **자동차 / 모빌리티**: [TSLA](../news/TSLA.md) · [TM](../news/TM.md) · [F](../news/F.md) · [GM](../news/GM.md) · [STLA](../news/STLA.md) · [HMC](../news/HMC.md) · [RIVN](../news/RIVN.md) · [NIO](../news/NIO.md) · [005380.KS](../news/005380.KS.md) · [000270.KS](../news/000270.KS.md)
- **바이오 / 제약 / 헬스케어**: [LLY](../news/LLY.md) · [NVO](../news/NVO.md) · [JNJ](../news/JNJ.md) · [PFE](../news/PFE.md) · [MRK](../news/MRK.md) · [ABBV](../news/ABBV.md) · [AZN](../news/AZN.md) · [UNH](../news/UNH.md) · [TMO](../news/TMO.md) · [ABT](../news/ABT.md)
- **에너지 / 원자재**: [XOM](../news/XOM.md) · [CVX](../news/CVX.md) · [COP](../news/COP.md) · [SHEL](../news/SHEL.md) · [OXY](../news/OXY.md) · [SLB](../news/SLB.md) · [FCX](../news/FCX.md) · [NEM](../news/NEM.md) · [LIN](../news/LIN.md) · [APD](../news/APD.md)
- **금융**: [JPM](../news/JPM.md) · [BAC](../news/BAC.md) · [WFC](../news/WFC.md) · [C](../news/C.md) · [GS](../news/GS.md) · [MS](../news/MS.md) · [V](../news/V.md) · [MA](../news/MA.md) · [AXP](../news/AXP.md) · [BRK-B](../news/BRK-B.md)
- **소비재**: [WMT](../news/WMT.md) · [COST](../news/COST.md) · [KO](../news/KO.md) · [PEP](../news/PEP.md) · [PG](../news/PG.md) · [MO](../news/MO.md) · [MCD](../news/MCD.md) · [HD](../news/HD.md) · [NKE](../news/NKE.md) · [SBUX](../news/SBUX.md)
- **산업재 / 방산**: [CAT](../news/CAT.md) · [DE](../news/DE.md) · [BA](../news/BA.md) · [LMT](../news/LMT.md) · [RTX](../news/RTX.md) · [NOC](../news/NOC.md) · [HON](../news/HON.md) · [GE](../news/GE.md) · [UPS](../news/UPS.md) · [FDX](../news/FDX.md)
- **부동산 (REITs)**: [AMT](../news/AMT.md) · [CCI](../news/CCI.md) · [PLD](../news/PLD.md) · [EQIX](../news/EQIX.md) · [DLR](../news/DLR.md) · [O](../news/O.md) · [SPG](../news/SPG.md) · [WELL](../news/WELL.md) · [PSA](../news/PSA.md) · [VICI](../news/VICI.md)
- **통신 / 미디어**: [VZ](../news/VZ.md) · [T](../news/T.md) · [TMUS](../news/TMUS.md) · [CMCSA](../news/CMCSA.md) · [CHTR](../news/CHTR.md) · [NFLX](../news/NFLX.md) · [DIS](../news/DIS.md) · [SPOT](../news/SPOT.md) · [EA](../news/EA.md) · [TTWO](../news/TTWO.md)
- **유틸리티 / 전력**: [NEE](../news/NEE.md) · [SO](../news/SO.md) · [DUK](../news/DUK.md) · [AEP](../news/AEP.md) · [EXC](../news/EXC.md) · [CEG](../news/CEG.md) · [VST](../news/VST.md) · [SRE](../news/SRE.md) · [ED](../news/ED.md) · [D](../news/D.md)
- **조선 (한국)**: [329180.KS](../news/329180.KS.md) · [042660.KS](../news/042660.KS.md) · [010140.KS](../news/010140.KS.md) · [010620.KS](../news/010620.KS.md)
