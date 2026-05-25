---
title: "Watchlist News Dashboard"
created: 2026-05-16
updated: 2026-05-25
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

> 루틴은 실행되는 요일을 자동 감지해 그난 처리할 섹터만 뉴스 수집 → narrative_score → wiki/news 업데이트를 수행한다.

## 최신 스냅샷 (섹터별)

### 빅테크 / 소프트웨어

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [AAPL](AAPL - Apple Inc.md) | 2026-05-25 | -0.10 | 개별 뉴스 없음 — 관세·EU 규제 매크로 기조 지속 | 1 |
| [MSFT](MSFT - Microsoft Corporation.md) | 2026-05-25 | +0.03 | Ackman $2.1B 매수, Moody's 신용 하향 소폭 압박 | 2 |
| [GOOGL](GOOGL - Alphabet Inc.md) | 2026-05-25 | +0.10 | Q1 순이익 +81%, 클라우드 백로그 $460B 두 배, Gemini 가격 전쟁 | 3 |
| [AMZN](AMZN - Amazon.com Inc.md) | 2026-05-25 | +0.13 | Q1 EPS $2.78 대폭 비트, AWS +28%, Anthropic 수익 $168억 | 3 |
| [META](META - Meta Platforms Inc.md) | 2026-05-25 | +0.00 | 2026 광고 GOOGL 초월 전망, Behemoth 모델, capex $145B 상향 | 3 |
| [ORCL](ORCL - Oracle Corporation.md) | 2026-05-25 | +0.25 | Q3 OCI +84%, AI +243%, 잔고 $5530억, $300억 정부 계약 | 2 |
| [CRM](CRM - Salesforce, Inc.md) | 2026-05-25 | -0.03 | Agentforce 29K 건 $800M ARR, Q1 FY27 5월 27일 발표 | 3 |
| [ADBE](ADBE - Adobe Inc.md) | 2026-05-25 | -0.10 | Piper Sandler Neutral 하향 $330, 바이브 코딩 구조적 우려 | 3 |
| [IBM](IBM - International Business Machines.md) | 2026-05-25 | -0.10 | 개별 뉴스 없음 — Oracle AI 급성장이 WatsonX 위협 | 2 |
| [PLTR](PLTR - Palantir Technologies Inc.md) | 2026-05-25 | +0.13 | DIA 계약 도전, 19/28 강력 매수 목표 $194.81(+42%) | 3 |

### 반도체

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
| [SHEL](SHEL - Shell plc.md) | 2026-05-22 | +0.13 | Shell CEO 10억 배럴 부족 경고·호르무즈 봉쇄 | 2 |
| [OXY](OXY - Occidental Petroleum.md) | 2026-05-22 | +0.03 | Q1 EPS 비트 but CEO 퇴임·주가 -7.8% 혼조 | 2 |
| [SLB](SLB - Schlumberger Limited.md) | 2026-05-22 | +0.10 | Bernstein/Barclays/BofA 목표가 동시 상향 | 2 |
| [FCX](FCX - Freeport-McMoRan.md) | 2026-05-22 | +0.20 | 구리 역대 최고 $6.44/lb·Grasberg PB 2/3 재개 | 2 |
| [NEM](NEM - Newmont Corporation.md) | 2026-05-22 | +0.30 | Q1 EPS $2.90 역대 최고·$6B 추가 자사주매입 | 2 |
| [LIN](LIN - Linde plc.md) | 2026-05-22 | +0.08 | Q1 EPS 비트·우주 고객 장기 공급 계약 체결 | 2 |
| [APD](APD - Air Products and Chemicals.md) | 2026-05-22 | +0.08 | Q2 EPS·매출 모두 비트·복수 목표가 상향 | 2 |

### 금융

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [JPM](JPM - JPMorgan Chase and Co.md) | 2026-05-23 | +0.08 | AI 인력 효율화·$1.5조 방산·AI 이니셔티브 발표 | 4 |
| [BAC](BAC - Bank of America Corp.md) | 2026-05-23 | +0.09 | LTX AI 채권 플랫폼 가입·자산관리 두 자릿수 성장 | 3 |
| [WFC](WFC - Wells Fargo and Company.md) | 2026-05-23 | +0.16 | 대출 $1조 돌파·신용카드 +60% 자산제한 해제 성과 | 3 |
| [C](C - Citigroup Inc.md) | 2026-05-23 | +0.12 | 이란 전쟁 트레이딩 서프라이즈·자산관리 두 자릿수 | 3 |
| [GS](GS - The Goldman Sachs Group.md) | 2026-05-23 | +0.06 | 사모 크레딧 신중론·이란 전쟁 트레이딩 수혜 | 2 |
| [MS](MS - Morgan Stanley.md) | 2026-05-23 | +0.08 | 웹스 매니지먼트 +16%·E*TRADE 암호화폐 기관 확대 | 3 |
| [V](V - Visa Inc.md) | 2026-05-23 | -0.06 | AI 에이전틱 커머스·스테이블코인 위협 10년 최저 밸류 | 3 |
| [MA](MA - Mastercard Incorporated.md) | 2026-05-23 | -0.04 | AI 에이전틱 커머스 위협·Q1 EPS +12% 실적 괴리 | 3 |
| [AXP](AXP - American Express Company.md) | 2026-05-23 | +0.05 | Q1 EPS +7% 비트·폐쇄형 네트워크 스테이블코인 면역 | 3 |
| [BRK-B](BRK-B - Berkshire Hathaway.md) | 2026-05-23 | +0.10 | Abel 주주환담 분할 불가·GOOGL +224% 포트폴리오 대전환 | 3 |

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
| [AMT](AMT - American Tower Corporation.md) | 2026-05-23 | +0.05 | Bernstein 아웃퍼폼 업그레이드 $207·타워 REIT 회복 | 2 |
| [CCI](CCI - Crown Castle Inc.md) | 2026-05-23 | +0.14 | $8.5B 매각 완료·AFFO 상향·$1B 자사주매입 | 3 |
| [PLD](PLD - Prologis Inc.md) | 2026-05-23 | +0.05 | Q1 동일점포 NOI +8.8%·배당 $1.07 인상 | 3 |
| [EQIX](EQIX - Equinix Inc.md) | 2026-05-23 | +0.03 | 2026 매출 +9-10%·11년 연속 배당 인상·차입금 급증 | 3 |
| [DLR](DLR - Digital Realty Trust.md) | 2026-05-23 | +0.16 | 역대 최대 AI 임대 200MW·자본지출 $250M 상향 | 3 |
| [O](O - Realty Income Corporation.md) | 2026-05-23 | +0.04 | 671회 연속 월배당·투자 가이던스 $9.5B 상향 | 3 |
| [SPG](SPG - Simon Property Group.md) | 2026-05-23 | +0.06 | Q2 배당 $2.25·FFO 가이던스 상향·96% 입주율 | 3 |
| [WELL](WELL - Welltower Inc.md) | 2026-05-23 | +0.14 | $4.2B 인수 완료·PSA 데이터·ML 파트너십 | 3 |
| [PSA](PSA - Public Storage.md) | 2026-05-23 | +0.04 | WELL·PSA 시니어 주택 데이터·ML 파트너십 신사업 | 3 |
| [VICI](VICI - VICI Properties Inc.md) | 2026-05-23 | +0.05 | Q2 배당 $0.4325·Barclays $34 상향 18% 업사이드 | 3 |

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

## 오늘의 시그널 (2026-05-25 · 월요일 · 빅테크 / 소프트웨어)

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈로 동시 움직임
- **섹터간 전파**: 한 섹터의 충격이 다른 섹터로 번지는 패턴

### 감지된 패턴

- **모순 (ADBE 내러티브 역전)**: ADBE +0.12(2026-05-18) → -0.10(2026-05-25), Δ -0.22. Piper Sandler '바이브 코딩·좌석 압축' 구조적 하향으로 소프트웨어 셉터 주도주 내러티브 완전 역전. 전회 셉터 로테이션 수혜주에서 구조적 멀티플 압축 피해주로 전환.
- **셉터 동기화 (AI 인프라 플랫폼 양극화)**: ORCL +0.25 (AI 인프라 +243%, $5530억 백로그 — 최강), GOOGL +0.10 (클라우드 +63%, Gemini 가격 전쟁), AMZN +0.13 (AWS +28%, Bedrock +170%), MSFT +0.03 — 클라우드 AI 인프라 수혜 종목 동기화 상승. 반면 ADBE(-0.10)·IBM(-0.10)·CRM(-0.03)은 AI 직접 경쟁에 구조적 노출로 압박.
- **연속성 (AI capex 투자 부담 테마 지속)**: META capex $145B 상향 (3회 연속 capex 우려 등장). AI 인프라 수요가 하이퍼스케일러 전반의 자본지출 경쟁 심화 — AMZN $200B, GOOGL $175-185B, META $145B.
- **최고 시그널**: ORCL +0.25 — Q3 AI 인프라 +243%, OCI +84%, $5530억 미이행 잔고(+325%), $300억 미국 정부 클라우드 계약. AI 클라우드 인프라 시장에서 AWS·Azure를 위협하는 3rd force 부상 가장 강한 신호.
- **경고 시그널**: ADBE -0.10 ← 전회 +0.12 역전. Piper Sandler '바이브 코딩' 우려가 단순 경쟁 압박을 넘어 수익모델 구조적 해체 가능성 제기. CRM(-0.03)과 함께 소프트웨어 좌석 기반 모델 전반 재평가 압박.
- **셉터간 전파 예고**: 빅테크 AI 인프라 capex 경쟁($200B+/社) → 다음 화요일 반도체 셉터(NVDA·AMD·ASML) 수요 직접 견인. 특히 ORCL $5530억 백로그는 NVDA GPU 수요 확약 성격 — 반도체 셉터 강세 예고.

## 사용 팀

- 점수 변화가 큰 종목 우선 확인 → 해당 `{TICKER} - {name}.md` 의 [일자별 기록] 최신만 읽으면 충분.
- [미해결 가설] 콼럼이 비어있지 않은 종목은 후속 검증이 필요한 사안이 누적된 상태.
- 섹터 단위로 묶어서 보면 매크로 충격이 어떤 종목들에 동시에 영향을 주는지 빠르게 파악 가능.
- 요일별 라운드로빈이므로 특정 종목이 몇일 동안 업데이트되지 않을 수 있다 — 정상.