---
title: "Watchlist News Dashboard"
created: 2026-05-16
updated: 2026-06-01
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
| [NVDA](NVDA - NVIDIA Corporation.md) | — | — | — | — |
| [AMD](AMD - Advanced Micro Devices.md) | — | — | — | — |
| [INTC](INTC - Intel Corporation.md) | — | — | — | — |
| [QCOM](QCOM - QUALCOMM Incorporated.md) | — | — | — | — |
| [TSM](TSM - Taiwan Semiconductor Mfg.md) | — | — | — | — |
| [ASML](ASML - ASML Holding NV.md) | — | — | — | — |
| [AMAT](AMAT - Applied Materials.md) | — | — | — | — |
| [LRCX](LRCX - Lam Research Corp.md) | — | — | — | — |
| [AVGO](AVGO - Broadcom Inc.md) | — | — | — | — |
| [MU](MU - Micron Technology.md) | — | — | — | — |

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
| [XOM](XOM - Exxon Mobil Corporation.md) | 2026-05-29 | +0.08 | Q1 컨센서스 상회 + 베네수엘라 복귀 협상 + Barclays $182 상향 | 1 |
| [CVX](CVX - Chevron Corporation.md) | 2026-05-29 | +0.10 | Q1 강세 + 지중해 가스전 진출 + 이사 $7300만 블록 매도 | 1 |
| [COP](COP - ConocoPhillips.md) | 2026-05-29 | -0.05 | 연간 생산가이던스 하향 수정 (-3.4%) | 1 |
| [SHEL](SHEL - Shell plc.md) | 2026-05-29 | +0.15 | Q1 조정이익 $69억 + 배당 5% 인상 + LNG 캐나다 램프업 | 1 |
| [OXY](OXY - Occidental Petroleum.md) | 2026-05-29 | +0.10 | Q1 생산·FCF 상회 + Barclays Hold→Buy + PT $75 | 1 |
| [SLB](SLB - Schlumberger Limited.md) | 2026-05-29 | -0.13 | 차기 EPS -28% YoY + 유가 하락 -3.4% | 1 |
| [FCX](FCX - Freeport-McMoRan.md) | 2026-05-29 | +0.15 | Barclays OW 신규 개시 + 구리 EV·재생에너지 수요 강세 | 1 |
| [NEM](NEM - Newmont Corporation.md) | 2026-05-29 | -0.03 | 2026 생산량 하락 + 비용 상승 vs 금값 $3,000 유지 | 1 |
| [LIN](LIN - Linde plc.md) | 2026-05-29 | +0.18 | Q1 EPS +10% YoY + 가이던스 상향 + 전자 가스 강세 | 1 |
| [APD](APD - Air Products and Chemicals.md) | 2026-05-29 | -0.08 | 미국 3개 프로젝트 철수 ($31억 손상) vs NEOM 80% 완공 | 1 |

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
| [NEE](NEE - NextEra Energy.md) | 2026-05-29 | +0.18 | Dominion $4000억 합병 발표 — 세계 최대 규제 유틸리티 탄생 | 1 |
| [SO](SO - The Southern Company.md) | 2026-05-29 | +0.10 | Q1 EPS 상회 + 가이던스 상향 + Vogtle 4호기 정격출력 | 1 |
| [DUK](DUK - Duke Energy Corporation.md) | 2026-05-29 | +0.13 | Q1 EPS 상회 + $1022억 자본투자 + 인디애나 18% 요금 신청 | 1 |
| [AEP](AEP - American Electric Power.md) | 2026-05-29 | +0.15 | Q1 EPS 상회 + 3GW 데이터센터 계약 + 가이던스 상향 | 1 |
| [EXC](EXC - Exelon Corporation.md) | 2026-05-29 | 0.00 | Q1 EPS 컨센서스 부합 — 뚜렷한 촉매 없음 | 1 |
| [CEG](CEG - Constellation Energy.md) | 2026-05-29 | +0.25 | Q1 EPS $3.68 대폭 상회 + Microsoft 20년 원자력 PPA 체결 | 1 |
| [VST](VST - Vistra Corp.md) | 2026-05-29 | +0.20 | Q1 EBITDA 상회 + 가이던스 상향 + Energy Harbor 원자력 인수 완료 | 1 |
| [SRE](SRE - Sempra.md) | 2026-05-29 | 0.00 | Q1 EPS 컨센서스 하회 + LNG 수출 용량 확대 승인 | 1 |
| [ED](ED - Consolidated Edison.md) | 2026-05-29 | +0.08 | Q1 EPS 상회 + NYC 그리드 현대화 $7억 투자 | 1 |
| [D](D - Dominion Energy.md) | 2026-05-29 | +0.15 | NEE와 합병 합의 (0.8138배) — 주가 합병 프리미엄 반영 | 1 |

### 조선 (한국)

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [329180.KS](329180.KS - HD Hyundai Heavy Industries.md) | — | — | — | — |
| [042660.KS](042660.KS - Hanwha Ocean Co.md) | — | — | — | — |
| [010140.KS](010140.KS - Samsung Heavy Industries.md) | — | — | — | — |
| [010620.KS](010620.KS - HMM Co.md) | — | — | — | — |

## 오늘의 시그널 (2026-05-18 · 월요일 · 빅테크 / 소프트웨어)

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장 (예: 비만치료제 임상 데이터 연속)
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈 (예: 관세, FOMC, 유가, 비만치료제, 데이터센터 전력) 로 동시 움직임
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