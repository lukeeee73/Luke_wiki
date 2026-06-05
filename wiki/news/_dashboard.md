---
title: "Watchlist News Dashboard"
created: 2026-05-16
updated: 2026-06-05
domain: finance
type: index
weight: reference
confidence: low
tags: [routine-news, watchlist, dashboard]
sources: []
---

# Watchlist News Dashboard

루틴이 매일 갱신한다. **요일별 라운드로빈** 으로 한 번에 하나의 섹터(또는 묶음)만 처리하여 부담을 분산한다 — 아래 "요일별 처리 일정" 참고. 섹터 그룹별로 watchlist 종목들의 가장 최근 narrative_score 와 핵심 이슈 한 줄을 모아서 폰에서 한눈에 보기 위한 페이지.

> [!info] 마지막 업데이트
> 루틴이 다음 실행에 자동으로 갱신한다.

## 요일별 처리 일정

| 요일 | 처리 섹터 | 종목 수 |
|---|---|---|
| 월요일 | 빅테크 / 소프트웨어 | 10 종목 |
| 화요일 | 반도체 | 10 종목 |
| 수요일 | 자동차 / 모빌리티 + 조선 (한국) | 14 종목 |
| 목요일 | 바이오 / 제약 / 헬스케어 | 10 종목 |
| 금요일 | 에너지 / 원자재 + 유틸리티 / 전력 | 20 종목 |
| 토요일 | 금융 + 부동산 (REITs) | 20 종목 |
| 일요일 | 소비재 + 산업재 / 방산 + 통신 / 미디어 | 30 종목 |

> 루틴은 실행되는 요일을 자동 감지해 그날 처리할 섹터만 뉴스 수집 → narrative_score → wiki/news 업데이트를 수행한다.

## 최신 스냅샷 (섹터별)

### 빅테크 / 소프트웨어

| Ticker                                          | as_of      | score  | 핵심 한 줄                                         | open claims |
| ----------------------------------------------- | ---------- | ------ | ----------------------------------------------- | ----------- |
| [AAPL](AAPL - Apple Inc.md)                     | 2026-06-01 | +0.13  | Q3 가이던스 +14~17% 컨센서스 대폭 상회, WWDC 6/8 AI 발표 기대  | 3           |
| [MSFT](MSFT - Microsoft Corporation.md)         | 2026-06-01 | +0.18  | AI 사업 $37B 연환산(+123%), Build 2026 자체 AI 코딩 모델   | 2           |
| [GOOGL](GOOGL - Alphabet Inc.md)                | 2026-06-01 | +0.24  | Q1 순이익 +81%, $800억 AI 자본 조달, 목표주가 $427.89      | 1           |
| [AMZN](AMZN - Amazon.com Inc.md)                | 2026-06-01 | -0.13  | AWS EU 규제+ACCC 소송으로 -3.5%, $200B capex 부담      | 3           |
| [META](META - Meta Platforms Inc.md)            | 2026-06-01 | +0.03  | EU DSA 조사·UK 조사 (-), Q1 +33%·Q2 가이던스 강세 (+)    | 1           |
| [ORCL](ORCL - Oracle Corporation.md)            | 2026-06-01 | +0.20  | +5.56% (Project Jupiter+정부 AI 계약), 백로그 $5530억    | 1           |
| [CRM](CRM - Salesforce, Inc.md)                 | 2026-06-01 | +0.24  | Q1 FY27 +13% 서프라이즈·+9.7%, Contentful 인수·Anthropic $5B | 1           |
| [ADBE](ADBE - Adobe Inc.md)                     | 2026-06-01 | +0.05  | Nvidia AI 협업·+5.7% 반등, Q2 실적 6/11 예정          | 2           |
| [IBM](IBM - International Business Machines.md) | 2026-06-01 | +0.18  | Nvidia 파트너십·Barclays 상향·5월 +32% (24년래 최고)      | 1           |
| [PLTR](PLTR - Palantir Technologies Inc.md)     | 2026-06-01 | +0.28  | Q1 $1.63B(+85%)·주간 +13%, 12개월 목표 $200          | 2           |

### 반도체

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [NVDA](NVDA - NVIDIA Corporation.md) | 2026-06-02 | +0.50 | COMPUTEX Vera Rubin CPU·RTX Spark 발표, 주주환원 FCF 50%+, TSMC 파트너십 심화 | 2 |
| [AMD](AMD - Advanced Micro Devices.md) | 2026-06-02 | +0.16 | NVDA RTX Spark 발표로 4% 급락, Q2 가이던스 $11.2B(+45% YoY) TD Cowen $600 상향 | 3 |
| [TSM](TSM - Taiwan Semiconductor Mfg.md) | 2026-06-02 | +0.41 | NVDA 대만 투자 확대로 4.8% 급등, 3nm 공정 가격 15% 인상, 직원 보너스 30%+ | 4 |
| [AVGO](AVGO - Broadcom Inc.md) | 2026-06-02 | +0.39 | 6/3 Q2 실적 발표·AI 수주잔고 $73B, 알파벳 $80B 인프라 투자 수혜, WF $545 상향 | 3 |
| [INTC](INTC - Intel Corporation.md) | 2026-06-02 | -0.20 | COMPUTEX Xeon 6+ 발표 → 4.67% 급락, NVDA RTX Spark AI PC 직격탄 | 3 |
| [QCOM](QCOM - QUALCOMM Incorporated.md) | 2026-06-02 | -0.22 | NVDA RTX Spark(100+ TOPS)으로 Snapdragon 위협 → 8.78% 급락, 6/24 인베스터 데이 | 4 |
| [ASML](ASML - ASML Holding NV.md) | 2026-06-02 | +0.33 | 4.7% 상승·연초 +53%, Q1 €103억·마진 53%, UBS €1,900 상향 | 3 |
| [AMAT](AMAT - Applied Materials.md) | 2026-06-02 | +0.39 | 사상 최대 매출·25년 최고 마진, 연간 장비 성장률 30%+ 상향, ASMPT NEXX $120M 인수 | 3 |
| [LRCX](LRCX - Lam Research Corp.md) | 2026-06-02 | +0.40 | COMPUTEX 후 4.8% 급등·52주 신고가, Q3 FY26 사상 최대 $5.84B, WFE $1,400억 상향 | 3 |
| [MU](MU - Micron Technology.md) | 2026-06-02 | +0.47 | HBM4 2026년 전량 매진·시총 $1조 돌파, 주가 +231% YTD, 6/24 Q3 실적 발표 | 3 |

### 자동차 / 모빌리티

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [TSLA](TSLA - Tesla Inc.md) | 2026-06-03 | +0.10 | 유럽 5월 판매 급증·Q1+17%, 텍사스 로보택시 규제 강화 | 2 |
| [TM](TM - Toyota Motor Corporation.md) | 2026-06-03 | -0.09 | 인증 위반으로 日 3개 차종 판매 중단, FY2026 실적 양호 | 2 |
| [F](F - Ford Motor Company.md) | 2026-06-03 | -0.07 | 4월 판매 -14.4%, EV -31.1% — CMO 퇴임 겹침 | 2 |
| [GM](GM - General Motors Company.md) | 2026-06-03 | +0.17 | 관세 대법원 수혜 가이던스 상향, Q1 EBIT $4.3B 견고 | 1 |
| [STLA](STLA - Stellantis NV.md) | 2026-06-03 | -0.30 | 증권사기 집단소송 마감 임박 — 법적 리스크 최고조 | 2 |
| [HMC](HMC - Honda Motor Co.md) | 2026-06-03 | +0.02 | 5월 미국 판매 +9.9%, Q4 FY2026 대규모 순손실 혼조 | 1 |
| [RIVN](RIVN - Rivian Automotive.md) | 2026-06-03 | +0.30 | R2 배송 6/9 시작 + VW 15.9% 지분 — 10거래일 연속 상승 | 3 |
| [NIO](NIO - NIO Inc.md) | 2026-06-03 | +0.20 | 5월 인도 +62.3%, ONVO L80 출시, Q2 110k-115k 가이던스 | 2 |
| [005380.KS](005380.KS - Hyundai Motor Company.md) | 2026-06-03 | -0.05 | 5월 판매 -7.7% 내수 약세, $200억 미국 투자 발표 예정 | 2 |
| [000270.KS](000270.KS - Kia Corporation.md) | 2026-06-03 | +0.07 | U.S. News 최우수 EV 3종 수상, NVIDIA 자율주행 협력 | 1 |

### 바이오 / 제약 / 헬스케어

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [LLY](LLY - Eli Lilly and Company.md) | 2026-06-04 | +0.22 | M&A $10B+ 가속화·독일 투자 절반 삭감 — 미국 우선 전략 선명화 | 2 |
| [NVO](NVO - Novo Nordisk AS.md) | 2026-06-04 | -0.07 | 경구형 위고비 UAE 론칭, 주가 1년 -38.9% 하락 지속 | 2 |
| [JNJ](JNJ - Johnson and Johnson.md) | 2026-06-04 | +0.13 | 닙포칼리맙 Phase 2 SLE·쇼그렌증 성공, 64년 연속 배당 3.1% 인상 | 2 |
| [PFE](PFE - Pfizer Inc.md) | 2026-06-04 | -0.02 | 350번째 연속 분기 배당, 2026년 20개 피벗 임상 계획 | 2 |
| [MRK](MRK - Merck and Co.md) | 2026-06-04 | +0.11 | ASCO 흑색종 5년 데이터 긍정·$6.7B 인수, LITESPARK-012 실패 | 3 |
| [ABBV](ABBV - AbbVie Inc.md) | 2026-06-04 | +0.15 | 아퀴프타 EU 편두통 승인, 골드만삭스 컨퍼런스 6/9 참가 | 2 |
| [AZN](AZN - AstraZeneca PLC.md) | 2026-06-04 | -0.09 | 카미제스트란트 FDA 결정 연기·안셀라미맙 Phase 3 실패 | 2 |
| [UNH](UNH - UnitedHealth Group.md) | 2026-06-04 | +0.09 | BofA·MS·Truist 동시 목표주가 $450+ 상향, 소송 재부상 | 2 |
| [TMO](TMO - Thermo Fisher Scientific.md) | 2026-06-04 | -0.03 | Q1 컨센서스 초과·미생물학 사업부 $1.075B 매각, 가이던스 보수적 | 2 |
| [ABT](ABT - Abbott Laboratories.md) | 2026-06-04 | +0.03 | 이중 CGM EU CE 마크·Exact Sciences 인수 완료, 주가 +4.4% | 3 |

### 에너지 / 원자재

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [XOM](XOM - Exxon Mobil Corporation.md) | 2026-06-05 | +0.10 | 텍사스 본거지 이전 + 가이아나 900k bpd 기록 + OPEC+ 6/7 증산 경계 | 2 |
| [CVX](CVX - Chevron Corporation.md) | 2026-06-05 | -0.05 | 싱가포르 정제 매각 $21.7억 + 가스 비중 확대 vs 호르무즈 직격탄 | 2 |
| [COP](COP - ConocoPhillips.md) | 2026-06-05 | -0.03 | 생산 가이던스 1.5% 하향 + 포트아서 LNG 첫 생산 임박 | 2 |
| [SHEL](SHEL - Shell plc.md) | 2026-06-05 | +0.01 | 자사주 매입 지속 + Q1 배당 $0.3906 + Buy 컨센서스 목표가 $99 | 2 |
| [OXY](OXY - Occidental Petroleum.md) | 2026-06-05 | +0.05 | CEO 교체(Hollub→Jackson) + 멕시코만 Bandit 광구 석유 발견 | 2 |
| [SLB](SLB - Schlumberger Limited.md) | 2026-06-05 | -0.05 | Tachyus AI 인수 + 30일 +15% vs Q2 EPS -28.4% YoY 예상 | 2 |
| [FCX](FCX - Freeport-McMoRan.md) | 2026-06-05 | +0.04 | Grasberg 복구 지연 (-) + $3B 신용한도 + UBS $75 상향 (구리 낙관론) | 2 |
| [NEM](NEM - Newmont Corporation.md) | 2026-06-05 | +0.24 | Q1 FCF $31억 기록 (금 $4,900/oz) + $60억 자사주매입 | 2 |
| [LIN](LIN - Linde plc.md) | 2026-06-05 | +0.17 | Q1 EPS +10% + 배당 33년 연속 + 삼성 반도체 팹 최대 딜 | 2 |
| [APD](APD - Air Products and Chemicals.md) | 2026-06-05 | +0.17 | Q2 EPS +19% YoY + 웰스파고 OW 상향 + 삼성 반도체 팹 계약 | 2 |

### 금융

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [JPM](JPM - JPMorgan Chase and Co.md) | 2026-05-17 | +0.00 | JLTXX 토큰 펀드 출시, 체이스 지점 52개, Dimon 경고 | 3 |
| [BAC](BAC - Bank of America Corp.md) | 2026-05-17 | +0.05 | Q1 EPS +25% 비트, 배당 $0.28, Fed 금리 동결 장기화 | 2 |
| [WFC](WFC - Wells Fargo and Company.md) | 2026-05-17 | +0.18 | Fed 자산제한 해제 (7년 만), ROTCE 17-18% 목표 재확인 | 2 |
| [C](C - Citigroup Inc.md) | 2026-05-17 | +0.03 | Investor Day ROTCE 목표 제시, 아시아 확장 승인 | 2 |
| [GS](GS - The Goldman Sachs Group.md) | 2026-05-17 | +0.00 | 주가 12개월 +65.5%, 사모 크레딧 신중론 | 2 |
| [MS](MS - Morgan Stanley.md) | 2026-05-17 | +0.08 | Q1 매출 $20.6B 사상 최대, E*TRADE 암호화폐 파일럿 | 2 |
| [V](V - Visa Inc.md) | 2026-05-17 | +0.15 | FY2Q EPS +20%·매출 +17%, UK FCA 조사 | 2 |
| [MA](MA - Mastercard Incorporated.md) | 2026-05-17 | +0.00 | Q1 EPS 비트, UK FCA 조사, AI Agent Pay 시연 | 2 |
| [AXP](AXP - American Express Company.md) | 2026-05-17 | +0.18 | Q1 EPS +18%, 골드 카드 ChatGPT 혜택, 여행 매각 | 2 |
| [BRK-B](BRK-B - Berkshire Hathaway.md) | 2026-05-17 | +0.10 | Q1 영업이익 $11.35B·현금 $397B, 델타항공 투자 | 2 |

### 소비재

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [WMT](WMT - Walmart Inc.md) | — | — | — | — |
| [COST](COST - Costco Wholesale.md) | — | — | — | — |
| [KO](KO - The Coca-Cola Company.md) | — | — | — | — |
| [PEP](PEP - PepsiCo.md) | — | — | — | — |
| [PG](PG - Procter and Gamble.md) | — | — | — | — |
| [MO](MO - Altria Group.md) | — | — | — | — |
| [MCD](MCD - McDonalds Corporation.md) | — | — | — | — |
| [HD](HD - The Home Depot.md) | — | — | — | — |
| [NKE](NKE - NIKE Inc.md) | — | — | — | — |
| [SBUX](SBUX - Starbucks Corporation.md) | — | — | — | — |

### 산업재 / 방산

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [CAT](CAT - Caterpillar Inc.md) | — | — | — | — |
| [DE](DE - Deere and Company.md) | — | — | — | — |
| [BA](BA - The Boeing Company.md) | — | — | — | — |
| [LMT](LMT - Lockheed Martin Corp.md) | — | — | — | — |
| [RTX](RTX - RTX Corporation.md) | — | — | — | — |
| [NOC](NOC - Northrop Grumman Corp.md) | — | — | — | — |
| [HON](HON - Honeywell International.md) | — | — | — | — |
| [GE](GE - GE Aerospace.md) | — | — | — | — |
| [UPS](UPS - United Parcel Service.md) | — | — | — | — |
| [FDX](FDX - FedEx Corporation.md) | — | — | — | — |

### 부동산 (REITs)

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [AMT](AMT - American Tower Corporation.md) | 2026-05-17 | +0.08 | Q1 EPS +15% 상회, 데이터센터 +17%, 가이던스 상향 | 2 |
| [CCI](CCI - Crown Castle Inc.md) | 2026-05-17 | +0.05 | 파이버·소형기지국 $8.5B 매각, 순수 타워 전환 | 2 |
| [PLD](PLD - Prologis Inc.md) | 2026-05-17 | +0.18 | Q1 EPS +29.6% 대폭 상회, 데이터센터 착공 $4.5-5.5B | 2 |
| [EQIX](EQIX - Equinix Inc.md) | 2026-05-17 | +0.13 | Q1 매출 +8%·마진 51%, AI 데이터센터 $50B 최고 | 1 |
| [DLR](DLR - Digital Realty Trust.md) | 2026-05-17 | +0.13 | Q1 매출 +16.2%, Core FFO 가이던스 상향 | 2 |
| [O](O - Realty Income Corporation.md) | 2026-05-17 | +0.05 | 670회 연속 월배당 134번째 인상, AFFO 가이던스 상향 | 2 |
| [SPG](SPG - Simon Property Group.md) | 2026-05-17 | +0.20 | Q1 FFO +7.5%, 배당 +7.1%, 소매 매출 +11.8%/sqft | 2 |
| [WELL](WELL - Welltower Inc.md) | 2026-05-17 | +0.20 | Q1 NOI +16.4%·순이익 +183%, 복수 애널리스트 상향 | 2 |
| [PSA](PSA - Public Storage.md) | 2026-05-17 | -0.03 | Q1 매출 -18% 미스·NOI +0.4%, NSA $5.63B 인수 발표 | 2 |
| [VICI](VICI - VICI Properties Inc.md) | 2026-05-17 | +0.08 | Q1 EPS +15.5% 상회, AFFO 가이던스 상향, 골든엔터 인수 | 2 |

### 통신 / 미디어

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [VZ](VZ - Verizon Communications.md) | — | — | — | — |
| [T](T - AT&T Inc.md) | — | — | — | — |
| [TMUS](TMUS - T-Mobile US.md) | — | — | — | — |
| [CMCSA](CMCSA - Comcast Corporation.md) | — | — | — | — |
| [CHTR](CHTR - Charter Communications.md) | — | — | — | — |
| [NFLX](NFLX - Netflix Inc.md) | — | — | — | — |
| [DIS](DIS - The Walt Disney Company.md) | — | — | — | — |
| [SPOT](SPOT - Spotify Technology.md) | — | — | — | — |
| [EA](EA - Electronic Arts Inc.md) | — | — | — | — |
| [TTWO](TTWO - Take-Two Interactive.md) | — | — | — | — |

### 유틸리티 / 전력

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [NEE](NEE - NextEra Energy.md) | 2026-06-05 | +0.03 | Dominion $670억 합병 + 고금리·희석 우려로 -13.7% | 2 |
| [SO](SO - The Southern Company.md) | 2026-06-05 | -0.01 | 조지아파워 요금 인하 명령 vs Vogtle 3·4호기 정격 출력 | 2 |
| [DUK](DUK - Duke Energy Corporation.md) | 2026-06-05 | +0.08 | AI 데이터센터 원전 공급 테크 협의 + Q1 EPS $1.93 | 2 |
| [AEP](AEP - American Electric Power.md) | 2026-06-05 | +0.08 | Q1 EPS +7.3% YoY + $417억 4년 자본투자 (7.9% 요금기반 성장) | 2 |
| [EXC](EXC - Exelon Corporation.md) | 2026-06-05 | -0.01 | PECO 요금 신청 철회 + 송전 $1.5B 증액 — 혼조 신호 | 2 |
| [CEG](CEG - Constellation Energy.md) | 2026-06-05 | +0.09 | MSFT+Meta 5,650MW 원전 PPA + YTD -25% → 역발상 매력 | 2 |
| [VST](VST - Vistra Corp.md) | 2026-06-05 | +0.10 | Meta 20년 PPA 2,600MW + 로터스 가스발전 7개 인수 | 2 |
| [SRE](SRE - Sempra.md) | 2026-06-05 | +0.03 | Voss Capital Oncor 분리 촉구 — 구조적 가치 해제 잠재력 | 2 |
| [ED](ED - Consolidated Edison.md) | 2026-06-05 | 0.00 | 의미있는 뉴스 없음 — 49년 배당 성장 안정 인컴주 | 1 |
| [D](D - Dominion Energy.md) | 2026-06-05 | +0.08 | NEE 합병 발표 + 130GW AI 파이프라인 + 규제 승인이 관건 | 2 |

### 조선 (한국)

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [329180.KS](329180.KS - HD Hyundai Heavy Industries.md) | 2026-06-03 | +0.33 | VLGC 8척 1.416조원 수주, 연간 목표 60.8% 조기 달성, KDDX 소송 | 2 |
| [042660.KS](042660.KS - Hanwha Ocean Co.md) | 2026-06-03 | +0.13 | Leidos 미 해군 설계 협력, 캐나다 해군 MOU 체결 | 2 |
| [010140.KS](010140.KS - Samsung Heavy Industries.md) | 2026-06-03 | +0.25 | FDC 시장 선점 — Capital/LR MOU·Supermicro AI 서버 JDP | 2 |
| [010620.KS](010620.KS - HMM Co.md) | — | — | — | — |

## 오늘의 시그널 (2026-06-05 · 금요일 · 에너지 / 원자재 + 유틸리티 / 전력))

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장 (예: 비만치료제 임상 데이터 연속)
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈 (예: 관세, FOMC, 유가, 비만치료제, 데이터센터 전력) 로 동시 움직임

**2026-06-05 감지된 시그널:**

- **섹터 동기화 (OPEC+ 위험)**: XOM, CVX, COP, SHEL, OXY — 6/7 OPEC+ 추가 증산 결정 가능성으로 에너지 5종목 동시 매크로 하방 압박.
- **섹터 동기화 (AI 원전 PPA)**: CEG, VST, DUK — MSFT·Meta 원전 장기 계약과 AI 데이터센터 전력 수요가 유틸리티 섹터 새 성장 테마로 자리잡음.
- **연속성 (NEE-D 합병)**: 2주 연속 NEE 합병 스토리가 NEE와 D 양쪽 모두에 등장 — 규제 승인이 핵심 관문으로 부각.
- **모순 (NEM)**: 5월 29일 -0.03 (생산 하락·비용 우려) → 6월 5일 +0.24 (Q1 FCF $31억 기록) — 금값 $4,900 신고점이 비용 우려를 완전히 역전시킴.
- **섹터간 전파**: 한 섹터의 충격이 다른 섹터로 번지는 패턴 (예: AI capex → 반도체 + 데이터센터 REIT + 유틸리티 동시 수혜)

### 감지된 패턴 (2026-06-03 · 수요일 · 자동차 / 모빌리티 + 조선 (한국))

- **섹터 양극화 (EV 수요 분화)**: RIVN +0.30 / NIO +0.20 / TSLA +0.10 (신규 EV 상승) vs F -0.07 / TM -0.09 / STLA -0.30 (전통 완성차 하락) — EV 모멘텀 스타트업과 전통 완성차의 센티멘트 격차 심화. RIVN R2 출시가 EV 스타트업 구심점.
- **섹터 동기화 (규제·법적 리스크)**: TM 인증 위반(일본 3개 차종 판매 중단) + STLA 증권사기 소송 — 완성차 양대 리스크가 동시에 터짐. 브랜드 신뢰도 이슈의 실질적 영향 30일 추적 필요.
- **섹터간 전파 (AI → 자동차 + 조선)**: NVIDIA DRIVE Hyperion 협력이 현대차·기아 동시 언급 → 조선 010140.KS는 Supermicro AI 서버 JDP → AI capex 파급 효과가 자동차·조선 양 섹터로 확산.
- **조선 섹터 동기화 (방산·신사업)**: 329180.KS VLGC 수주 + 포시도니아 MOU, 042660.KS 미국·캐나다 해군 MOU, 010140.KS FDC 3자 MOU — K-조선 빅3 모두 포시도니아 2026을 계기로 방산·신사업 동시 확장.
- **최고 신호**: 329180.KS +0.33 — 연간 목표 60.8% 5개월 달성 + 포시도니아 해군 MOU 겹침. RIVN +0.30 — R2 출시 D-6일 + VW 전략 투자 복합 호재.
- **경고 신호**: STLA -0.30 — 증권사기 소송 마감으로 법적 리스크 최고조. F -0.07 — 4월 EV 판매 -31% 붕괴로 EV 전환 전략 재점검 필요.
- **주목 이벤트**: RIVN R2 인도 시작(6월 9일) — 실제 인도량이 모멘텀 지속의 핵심. 현대차 $200억 미국 투자 공식 발표 일정 (미정). TM 인증 위반 추가 모델 확산 여부.

---

### 감지된 패턴 (2026-06-02 · 화요일 · 반도체)

- **섹터 동기화 (COMPUTEX 2026 + AI 사이클)**: NVDA +0.50 / TSM +0.41 / LRCX +0.40 / AVGO +0.39 / AMAT +0.39 / ASML +0.33 / MU +0.47 — 7종목이 COMPUTEX 2026과 AI 인프라 확장 테마로 동반 강세. 젠슨 황의 COMPUTEX 키노트가 전체 반도체 공급망(파운드리·장비·메모리)에 연쇄 긍정 시그널.
- **섹터 동기화 (NVDA RTX Spark 충격파)**: QCOM -0.22 / INTC -0.20 / AMD +0.16 — NVDA의 AI PC 슈퍼칩 RTX Spark(100+ TOPS) 발표가 QCOM(-8.78%)·INTC(-4.67%) 동반 급락 촉발. AMD도 4% 급락. AI PC 시장 주도권이 CPU/모바일칩에서 NVDA GPU로 이동하는 구조 변화 신호.
- **섹터간 전파**: NVDA AI 가속기 수요 확대 선언 → TSMC(파운드리 수혜), LRCX·AMAT·ASML(장비 사이클 상향), MU(HBM 수요 직결) — 반도체 밸류체인 전체에 COMPUTEX 효과 동시 침투.
- **최고 신호**: NVDA +0.50 — COMPUTEX 키노트(Vera Rubin CPU + RTX Spark) + 주주환원 FCF 50%+ + TSMC 파트너십 심화 삼중 호재. MU +0.47 — HBM4 전량 매진·시총 $1조 돌파·6/24 Q3 실적 기대 삼중 강세.
- **경고 신호**: QCOM -0.22 — NVDA RTX Spark이 Snapdragon X Elite(45 TOPS) 대비 2배 이상 성능 우위 부각으로 AI PC 시장 지위 흔들림. INTC -0.20 — COMPUTEX에서 Xeon 6+ 발표에도 시장 실망, PC·서버 양면 압박 지속.
- **주목 이벤트**: AVGO Q2 FY2026 실적 내일(6/3) 발표 — AI 수주잔고 $73B 확인 여부가 반도체 섹터 전반 센티멘트에 영향 예상. QCOM 6월 24일 인베스터 데이(Dragonfly 세부 발표)도 단기 변수.

---

## 오늘의 시그널 (2026-06-05 · 금요일 · 에너지 / 원자재 + 유틸리티 / 전력)

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장 (예: 비만치료제 임상 데이터 연속)
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈 (예: 관세, FOMC, 유가, 비만치료제, 데이터센터 전력) 로 동시 움직임

**2026-06-05 감지된 시그널:**

- **섹터 동기화 (OPEC+ 위험)**: XOM, CVX, COP, SHEL, OXY — 6/7 OPEC+ 추가 증산 결정 가능성으로 에너지 5종목 동시 매크로 하방 압박.
- **섹터 동기화 (AI 원전 PPA)**: CEG, VST, DUK — MSFT·Meta 원전 장기 계약과 AI 데이터센터 전력 수요가 유틸리티 섹터 새 성장 테마로 자리잡음.
- **연속성 (NEE-D 합병)**: 2주 연속 NEE 합병 스토리가 NEE와 D 양쪽 모두에 등장 — 규제 승인이 핵심 관문으로 부각.
- **모순 (NEM)**: 5월 29일 -0.03 (생산 하락·비용 우려) → 6월 5일 +0.24 (Q1 FCF $31억 기록) — 금값 $4,900 신고점이 비용 우려를 완전히 역전시킴.
- **섹터간 전파**: 한 섹터의 충격이 다른 섹터로 번지는 패턴 (예: AI capex → 반도체 + 데이터센터 REIT + 유틸리티 동시 수혜)

### 감지된 패턴 (2026-05-18 · 빅테크 / 소프트웨어)

- **섹터 동기화 (AI 독립 전략)**: MSFT·GOOGL·AMZN·META·PLTR 5 종목 모두 AI 전략이 핵심 뉴스 키워드. OpenAI 독립(MSFT), Googlebook(GOOGL), AWS AI(AMZN), Meta Superintelligence Labs(META), AIP 상업화(PLTR) 동시 가속화.
- **섹터 동기화 (소프트웨어 섹터 로테이션)**: ADBE +3.2%·CRM 반등 시도 — 반도체에서 소프트웨어로 자금 이동이 빅테크/소프트웨어 섹터 전반에 영향.
- **섹터 동기화 (밸류에이션 압박)**: PLTR(-26% YTD)·CRM(-30% YTD)·IBM(-26% YTD) 세 종목이 동시에 고밸류에이션·구조적 우려로 인한 조정 구간.
- **최고 신호**: ORCL +0.15 — Wedbush·Oppenheimer 동시 상향 + 삼성 계약이 겹친 이중 긍정. PLTR +0.12 — Q1 +85% 어닝 서프라이즈, 단 밸류에이션 압박 지속.
- **경고 신호**: AAPL -0.08 — 폴더블 출시 지연이 구글 Googlebook 출시 타이밍과 맞물려 하드웨어 경쟁에서 불리. IBM -0.08 — 메가캡 최하위 성과 지속.
- **섹터간 전파**: 전날(토) 금융·REITs AI capex 투자 붐 → 오늘(월) 빅테크 AI 전략 가속화로 AI 테마 섹터 연속 확산.

---

### 감지된 패턴 (2026-05-29 · 금요일 · 에너지/원자재 + 유틸리티/전력)

- **섹터 동기화 (이란 휴전 유가 하락)**: XOM -3.31%, CVX -3.05%, COP -3.43% 5/26 동반 급락 — 이란 핵 협상 진전이 에너지 섹터 전반 매도 촉발.
- **섹터 동기화 (AI 전력 수요)**: CEG +0.25 / VST +0.20 / AEP +0.15 — 원자력·전력회사 3종목이 공통으로 AI 데이터센터 전력 계약을 핵심 성장 동력으로 발표.
- **섹터 동기화 (M&A 프리미엄)**: NEE +0.18 / D +0.15 — NEE-Dominion $4000억 합병 발표로 유틸리티 섹터 M&A 파도 시작. SO·DUK·AEP도 잠재적 M&A 수혜 프리미엄.
- **최고 신호**: CEG +0.25 — Q1 EPS $3.68 vs 컨센서스 $3.12 대폭 상회 + Microsoft 20년 원자력 PPA 체결이 겹친 이중 긍정. LIN +0.18 — Q1 EPS +10% + 가이던스 상향 + RBC PT $552.
- **경고 신호**: SLB -0.13 — 차기 분기 EPS -28% YoY + 유가 하락 직격. COP -0.05 — 연간 생산가이던스 하향 수정. APD -0.08 — 미국 3개 프로젝트 철수 $31억 손상.
- **섹터간 전파**: 에너지 섹터 유가 하락 압력이 SLB 유전 서비스 업종으로 가장 강하게 전파 (SLB -0.13 = 섹터 최하위). 반면 유틸리티/전력은 AI 수요 테마로 에너지 하락과 탈동조화.

## 사용 팁

- 점수 변화가 큰 종목 우선 확인 → 해당 `{TICKER} - {name}.md` 의 [일자별 기록] 최신만 읽으면 충분.
- [미해결 가설] 컬럼이 비어있지 않은 종목은 후속 검증이 필요한 사안이 누적된 상태.
- 섹터 단위로 뽑아서 보면 매크로 충격이 어떤 종목들에 동시에 영향을 주는지 빠르게 파악 가능.
- 요일별 라운드로빈이므로 특정 종목이 몇일 동안 업데이트되지 않을 수 있다 — 정상.