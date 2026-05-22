---
title: "Watchlist News Dashboard"
created: 2026-05-16
updated: 2026-05-22
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

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [AAPL](AAPL - Apple Inc.md) | 2026-05-18 | -0.08 | 폴더블 힌지 결함 출시 지연 가능성 | 1 |
| [MSFT](MSFT - Microsoft Corporation.md) | 2026-05-18 | +0.08 | OpenAI 탈피 독립 AI 전략, Ackman 매수 | 1 |
| [GOOGL](GOOGL - Alphabet Inc.md) | 2026-05-18 | +0.10 | EPS 컨센서스 $14.22 상향, 클라우드 점유율 확대 | 2 |
| [AMZN](AMZN - Amazon.com Inc.md) | 2026-05-18 | +0.10 | AWS +28%, $3조 돌파 임박 — 관세 소송 병행 | 2 |
| [META](META - Meta Platforms Inc.md) | 2026-05-18 | +0.02 | Q1 매출 +33% 강세 but capex $125B 우려 | 2 |
| [ORCL](ORCL - Oracle Corporation.md) | 2026-05-18 | +0.15 | Wedbush/Oppenheimer 동시 상향, 삼성 Java 계약 | 1 |
| [CRM](CRM - Salesforce, Inc.md) | 2026-05-18 | -0.05 | BofA Underperform 하향, AI 좌석 잠식 우려 | 2 |
| [ADBE](ADBE - Adobe Inc.md) | 2026-05-18 | +0.12 | $25B 자사주 + 소프트웨어 섹터 로테이션 주도 | 2 |
| [IBM](IBM - International Business Machines.md) | 2026-05-18 | -0.08 | YTD -26% 메가캐프 최하위, RBC 목표 하향 | 2 |
| [PLTR](PLTR - Palantir Technologies Inc.md) | 2026-05-18 | +0.12 | Q1 +85% 어닝 대폭 서프라이즈, 가이던스 상향 | 2 |

### 반독체

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [NVDA](NVDA - NVIDIA Corporation.md) | 2026-05-19 | +0.32 | Q1 어닝 5/20 발표 기대, H200 중국 승인, 목표주가 상향 | 2 |
| [AMD](AMD - Advanced Micro Devices.md) | 2026-05-19 | +0.30 | Q1 데이터센터 $5.8B 역대 최고, MI450 AI 칩 예고 | 2 |
| [TSM](TSM - Taiwan Semiconductor Mfg.md) | 2026-05-19 | +0.25 | A13/A12/N2U 3년 로드맵 공개, AI/HPC 매출 61% | 2 |
| [AVGO](AVGO - Broadcom Inc.md) | 2026-05-19 | +0.32 | AI 칩 2027년 $1000억 목표, Meta 2nm 파트너십 | 2 |
| [INTC](INTC - Intel Corporation.md) | 2026-05-19 | -0.20 | 애플 계약 레거시 공정 실망, 서버 CPU -370bps | 2 |
| [QCOM](QCOM - QUALCOMM Incorporated.md) | 2026-05-19 | -0.20 | Q3 가이던스 하회, JPMorgan 중립 하향 $140 | 2 |
| [ASML](ASML - ASML Holding NV.md) | 2026-05-19 | +0.28 | 2026 가이던스 +16%, 인도 Tata 300mm 팩 파트너십 | 2 |
| [AMAT](AMAT - Applied Materials.md) | 2026-05-19 | +0.30 | Q2 매출·마진 역대 최고, Q3 가이던스 대폭 상회 | 2 |
| [LRCX](LRCX - Lam Research Corp.md) | 2026-05-19 | +0.18 | Q1 역대 최고, 삼성 5/21 파업 공급망 리스크 | 2 |
| [MU](MU - Micron Technology.md) | 2026-05-19 | +0.30 | HBM 2026 전량 매진, Q2 +196% YoY, 목표 $1,100 | 2 |

### 자동차 / 모빌리티

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [TSLA](TSLA - Tesla Inc.md) | — | — | — | — |
| [TM](TM - Toyota Motor Corporation.md) | — | — | — | — |
| [F](F - Ford Motor Company.md) | — | — | — | — |
| [GM](GM - General Motors Company.md) | — | — | — | — |
| [STLA](STLA - Stellantis NV.md) | — | — | — | — |
| [HMC](HMC - Honda Motor Co.md) | — | — | — | — |
| [RIVN](RIVN - Rivian Automotive.md) | — | — | — | — |
| [NIO](NIO - NIO Inc.md) | — | — | — | — |
| [005380.KS](005380.KS - Hyundai Motor Company.md) | — | — | — | — |
| [000270.KS](000270.KS - Kia Corporation.md) | — | — | — | — |

### 바이오 / 제약 / 헬스케어

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [LLY](LLY - Eli Lilly and Company.md) | — | — | — | — |
| [NVO](NVO - Novo Nordisk AS.md) | — | — | — | — |
| [JNJ](JNJ - Johnson and Johnson.md) | — | — | — | — |
| [PFE](PFE - Pfizer Inc.md) | — | — | — | — |
| [MRK](MRK - Merck and Co.md) | — | — | — | — |
| [ABBV](ABBV - AbbVie Inc.md) | — | — | — | — |
| [AZN](AZN - AstraZeneca PLC.md) | — | — | — | — |
| [UNH](UNH - UnitedHealth Group.md) | — | — | — | — |
| [TMO](TMO - Thermo Fisher Scientific.md) | — | — | — | — |
| [ABT](ABT - Abbott Laboratories.md) | — | — | — | — |

### 에너지 / 원자재

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [XOM](XOM - Exxon Mobil Corporation.md) | 2026-05-22 | +0.10 | Q1 어닝 비트·$20B 바이백·호르무즈 봉쇄 유가 급등 | 2 |
| [CVX](CVX - Chevron Corporation.md) | 2026-05-22 | +0.05 | 7일 연속 상승 지정학 수혜·내부자 $161M 순매도 | 2 |
| [COP](COP - ConocoPhillips.md) | 2026-05-22 | +0.13 | 30년 알래스카 LNG 계약·Q1 EPS $1.89 강세 | 2 |
| [SHEL](SHEL - Shell plc.md) | 2026-05-22 | +0.13 | Shell CEO 10억 배럴 부족 경고·호르무즈 빌쇄 | 2 |
| [OXY](OXY - Occidental Petroleum.md) | 2026-05-22 | +0.03 | Q1 EPS 비트 but CEO 퇴임·주가 -7.8% 혼조 | 2 |
| [SLB](SLB - Schlumberger Limited.md) | 2026-05-22 | +0.10 | Bernstein/Barclays/BofA 목표가 동시 상향 | 2 |
| [FCX](FCX - Freeport-McMoRan.md) | 2026-05-22 | +0.20 | 구리 역대 최고 $6.44/lb·Grasberg PB 2/3 재개 | 2 |
| [NEM](NEM - Newmont Corporation.md) | 2026-05-22 | +0.30 | Q1 EPS $2.90 역대 최고·$6B 추가 자사주매입 | 2 |
| [LIN](LIN - Linde plc.md) | 2026-05-22 | +0.08 | Q1 EPS 비트·우주 고객 장기 공급 계약 체결 | 2 |
| [APD](APD - Air Products and Chemicals.md) | 2026-05-22 | +0.08 | Q2 EPS·매출 모두 비트·복수 목표가 상향 | 2 |

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
| [NEE](NEE - NextEra Energy.md) | 2026-05-22 | +0.03 | $67B Dominion 인수·AI 30개 데이터센터 허브 계획 | 2 |
| [SO](SO - The Southern Company.md) | 2026-05-22 | +0.03 | 배당 $3.04 인상·Raymond James/Mizuho 목표 상향 | 2 |
| [DUK](DUK - Duke Energy Corporation.md) | 2026-05-22 | +0.08 | Q1 EPS $1.93 비트·$103B 자본계획 5~7% 성장 | 2 |
| [AEP](AEP - American Electric Power.md) | 2026-05-22 | +0.15 | Q1 7GW 신규 데이터센터 부하·자본계획 $78B 상향 | 2 |
| [EXC](EXC - Exelon Corporation.md) | 2026-05-22 | 0.00 | Q1 EPS·매출 상회·TD Cowen 목표 $51→$49 하향 | 2 |
| [CEG](CEG - Constellation Energy.md) | 2026-05-22 | +0.23 | Q1 매출 $11.12B vs 컨센서스 $8.71B 대폭 상회 | 2 |
| [VST](VST - Vistra Corp.md) | 2026-05-22 | +0.25 | Meta/AWS 3,800MW 20년 PPA·Q1 매출 8% 상회 | 2 |
| [SRE](SRE - Sempra.md) | 2026-05-22 | -0.03 | Q1 EPS·매출 미스·Morgan Stanley Overweight 유지 | 2 |
| [ED](ED - Consolidated Edison.md) | 2026-05-22 | -0.03 | Q1 컨센서스 상회·대다수 애널리스트 Sell 의견 | 2 |
| [D](D - Dominion Energy.md) | 2026-05-22 | +0.18 | $67B NEE 인수 +23% 프리미엄·D 주가 +11% 급등 | 2 |

### 조선 (한국)

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [329180.KS](329180.KS - HD Hyundai Heavy Industries.md) | — | — | — | — |
| [042660.KS](042660.KS - Hanwha Ocean Co.md) | — | — | — | — |
| [010140.KS](010140.KS - Samsung Heavy Industries.md) | — | — | — | — |
| [010620.KS](010620.KS - HMM Co.md) | — | — | — | — |

## 오늘의 시그널 (2026-05-22 · 금요일 · 에너지/원자재 + 유틸리티/전력)

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈로 동시 움직임
- **섹터간 전파**: 한 섹터의 충격이 다른 섹터로 번지는 패턴

### 감지된 패턴

- **섹터 동기화 (에너지 지정학 수혜 사이클)**: XOM·CVX·COP·SHEL 4종목이 호르무즈 해협 보쇄·Shell CEO 판매 가능 세계 원유 10억 배럴 부족 경고·Citigroup 유가 $120 전망으로 동시 양수. 에너지 공급 부족 매크로 환경 직차 가동.
- **섹터 동기화 (귀금속·원자재 수퍼사이클)**: FCX(+0.20)·NEM(+0.30) 동반 강세. 구리 역대 최고가 $6.44/lb + 금 실현가 +66% YoY + AI 인프라 구리 수요 구조적 상승 삼박자 동기화.
- **섹터 동기화 (AI 전력 수혜 유틸리티)**: VST(+0.25)·CEG(+0.23)·AEP(+0.15) 3종목이 AI 데이터센터 전력 수요로 동시 양수. 유틸리티 섹터 내 AI 수혜 여부에 따른 차별화 심화.
- **모순 (에너지 섹터 내 CEO 리스크)**: NEM(+0.30) 역대 최고 실적 vs OXY(+0.03) CEO 퇴임·주가 -7.8% 혼조 — 동일 섹터에서 리더십 리스크 영향 군단 분화.
- **모순 (유틸리티 AI 수혜/비수혜 극단 분리)**: VST(+0.25)·CEG(+0.23) vs SRE(-0.03)·ED(-0.03) — AI 전력 인프라 수혜 여부에 따른 유틸리티 섹터 내 가장 큰 편차(+0.28). EXC(0.00) 중간 포지셈.
- **최고 신호**: NEM +0.30 — Q1 역대 최고 실적(EPS $2.90·FCF $3.1B)에 $6B 추가 자사주매입 병행. 금 수퍼사이클 레버리지 완전 가동. / VST +0.25 — Meta/AWS 3,800MW 20년 PPA로 AI 전력 IPP 독보적 1위 확보.
- **경고 신호**: OXY +0.03 (CEO 퇴임 구조적 불확실성) / SRE -0.03 (Q1 EPS·매출 미스) / ED -0.03 (대다수 Sell 의견) — 전통 규제 유틸리티·리더십 교체 종목 단기 회시.
- **섹터간 전파 예고 (M&A 충격)**: NEE-D $67B 역대 최대 전력 유틸리티 M&A 발표 → 다음 실행 요일(월요일 · 빅테크/소프트웨어) MSFT·AMZN·META의 AI 데이터센터 전력 조달 비용 변화 뉴스 주목. AI 데이터센터 전력 비용 상승 → 빅테크 마진 압박 가능성.

## 사용 팁

- 점수 변화가 큰 종목 우선 확인 → 해당 `{TICKER} - {name}.md` 의 [일자별 기록] 최신만 읽으면 충분.
- [미해결 가설] 콜럼이 비어있지 않은 종목은 후속 검증이 필요한 사안이 누적된 상태.
- 섹터 단위로 뉵아서 보면 매크로 충격이 어떤 종목들에 동시에 영향을 주는지 빠르게 파악 가능.
- 요일별 라운드로빈이므로 특정 종목이 몇일 동안 업데이트되지 않을 수 있다 — 정상.
