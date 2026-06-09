---
title: "Watchlist News Dashboard"
created: 2026-05-16
updated: 2026-06-09
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
| [AAPL](tickers/AAPL - Apple Inc.md)                     | 2026-06-08 | +0.09  | WWDC 2026 Apple Intelligence·AI Siri 공개, 주가 sell-the-news -1.89%  | 2           |
| [MSFT](tickers/MSFT - Microsoft Corporation.md)         | 2026-06-08 | +0.13  | MAI-Thinking-1 포함 7개 AI 모델 + Majorana 2 양자칩 공개, YTD -12%   | 2           |
| [GOOGL](tickers/GOOGL - Alphabet Inc.md)                | 2026-06-08 | +0.07  | capex $180~190B 상향, $25B Blackstone TPU 벤처, 배당 권리락 주가 -1.18%  | 2           |
| [AMZN](tickers/AMZN - Amazon.com Inc.md)                | 2026-06-08 | +0.17  | Corning 광섬유 대규모 계약, 자연어 물류 로봇 출시, 62명 전원 매수      | 2           |
| [META](tickers/META - Meta Platforms Inc.md)            | 2026-06-08 | +0.17  | Q1 EPS 57% 어닝 서프라이즈, 비즈니스 AI 에이전트 글로벌 출시           | 2           |
| [ORCL](tickers/ORCL - Oracle Corporation.md)            | 2026-06-08 | +0.30  | Q4 발표 6/12 (매출 +20% 기대), RPO +325% $533B, 3개 증권사 목표가 상향  | 1           |
| [CRM](tickers/CRM - Salesforce, Inc.md)                 | 2026-06-08 | +0.47  | Q1 FY27 EPS +50% (컨센 24% 초과), Agentforce ARR $1.2B (+205%)       | 2           |
| [ADBE](tickers/ADBE - Adobe Inc.md)                     | 2026-06-08 | -0.17  | Q2 발표 6/11, YTD -27.49%, 애널 혼조 (Stifel $400↑ vs TD Cowen $285↓) | 2           |
| [IBM](tickers/IBM - International Business Machines.md) | 2026-06-08 | +0.24  | $10B 양자컴퓨팅 투자 (+7%), Nvidia Vera Rubin 파트너, BofA $315 상향   | 2           |
| [PLTR](tickers/PLTR - Palantir Technologies Inc.md)     | 2026-06-08 | +0.46  | Q1 EPS 22% 어닝 서프라이즈, FY2026 가이던스 +71%, 미국 세 자릿수 성장  | 2           |

### 반도체

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [NVDA](tickers/NVDA - NVIDIA Corporation.md) | 2026-06-09 | +0.27 | 애플 AI 고객 확보·구글 GPU 렌탈 계약, 젠슨 황 상원 청문회 거부 | 2 |
| [AMD](tickers/AMD - Advanced Micro Devices.md) | 2026-06-09 | +0.29 | 영국 AI 인프라 £2B 투자, Q1 데이터센터 +57%, 바클레이즈 $665 목표 | 2 |
| [TSM](tickers/TSM - Taiwan Semiconductor Mfg.md) | 2026-06-09 | +0.24 | 주주총회 2026년 30%+ 성장 확인, 3nm 가격 +15% 진행, 시총 $1.89T | 2 |
| [AVGO](tickers/AVGO - Broadcom Inc.md) | 2026-06-09 | -0.09 | Q2 AI 매출 2배($108억)에도 FY 가이던스 미상향 → 주가 -15% | 2 |
| [INTC](tickers/INTC - Intel Corporation.md) | 2026-06-09 | +0.35 | 구글 TPU 300만+ 파운드리 수주·NVDA 18A 평가·+11% 급등 — 파운드리 전환점 | 2 |
| [QCOM](tickers/QCOM - QUALCOMM Incorporated.md) | 2026-06-09 | +0.07 | 칩섹터 반등 동조, JP모건 $265 상향, 6/24 인베스터 데이 데이터센터 기대 | 3 |
| [ASML](tickers/ASML - ASML Holding NV.md) | 2026-06-09 | +0.30 | 머스크 Terafab $550억 텍사스 팹·2일 연속 +6.5%+4.2%, BofA €1,921 상향 | 2 |
| [AMAT](tickers/AMAT - Applied Materials.md) | 2026-06-09 | +0.29 | Q2 FY2026 사상 최대·25년 최고 마진·장비 30%+ 가이던스, 임원 $2,526만 매도 | 2 |
| [LRCX](tickers/LRCX - Lam Research Corp.md) | 2026-06-09 | +0.21 | WFE $1,400억 상향, 미즈호·UBS·MS 3사 목표가 동시 상향, 배당 $0.26 | 2 |
| [MU](tickers/MU - Micron Technology.md) | 2026-06-09 | +0.35 | 6/24 어닝 예정 ($335억+), DRAM +58~63% TrendForce, YTD +174% | 4 |

### 자동차 / 모빌리티

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [TSLA](tickers/TSLA - Tesla Inc.md) | 2026-06-03 | +0.10 | 유럽 5월 판매 급증·Q1+17%, 텍사스 로보택시 규제 강화 | 2 |
| [TM](tickers/TM - Toyota Motor Corporation.md) | 2026-06-03 | -0.09 | 인증 위반으로 日 3개 차종 판매 중단, FY2026 실적 양호 | 2 |
| [F](tickers/F - Ford Motor Company.md) | 2026-06-03 | -0.07 | 4월 판매 -14.4%, EV -31.1% — CMO 퇴임 겹침 | 2 |
| [GM](tickers/GM - General Motors Company.md) | 2026-06-03 | +0.17 | 관세 대법원 수혜 가이던스 상향, Q1 EBIT $4.3B 견고 | 1 |
| [STLA](tickers/STLA - Stellantis NV.md) | 2026-06-03 | -0.30 | 증권사기 집단소송 마감 임박 — 법적 리스크 최고조 | 2 |
| [HMC](tickers/HMC - Honda Motor Co.md) | 2026-06-03 | +0.02 | 5월 미국 판매 +9.9%, Q4 FY2026 대규모 순손실 혼조 | 1 |
| [RIVN](tickers/RIVN - Rivian Automotive.md) | 2026-06-03 | +0.30 | R2 배송 6/9 시작 + VW 15.9% 지분 — 10거래일 연속 상승 | 3 |
| [NIO](tickers/NIO - NIO Inc.md) | 2026-06-03 | +0.20 | 5월 인도 +62.3%, ONVO L80 출시, Q2 110k-115k 가이던스 | 2 |
| [005380.KS](tickers/005380.KS - Hyundai Motor Company.md) | 2026-06-03 | -0.05 | 5월 판매 -7.7% 내수 약세, $200억 미국 투자 발표 예정 | 2 |
| [000270.KS](tickers/000270.KS - Kia Corporation.md) | 2026-06-03 | +0.07 | U.S. News 최우수 EV 3종 수상, NVIDIA 자율주행 협력 | 1 |

### 바이오 / 제약 / 헬스케어

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [LLY](tickers/LLY - Eli Lilly and Company.md) | 2026-06-04 | +0.22 | M&A $10B+ 가속화·독일 투자 절반 삭감 — 미국 우선 전략 선명화 | 2 |
| [NVO](tickers/NVO - Novo Nordisk AS.md) | 2026-06-04 | -0.07 | 경구형 위고비 UAE 론칭, 주가 1년 -38.9% 하락 지속 | 2 |
| [JNJ](tickers/JNJ - Johnson and Johnson.md) | 2026-06-04 | +0.13 | 닙포칼리맙 Phase 2 SLE·쇼그렌증 성공, 64년 연속 배당 3.1% 인상 | 2 |
| [PFE](tickers/PFE - Pfizer Inc.md) | 2026-06-04 | -0.02 | 350번째 연속 분기 배당, 2026년 20개 피벗 임상 계획 | 2 |
| [MRK](tickers/MRK - Merck and Co.md) | 2026-06-04 | +0.11 | ASCO 흑색종 5년 데이터 긍정·$6.7B 인수, LITESPARK-012 실패 | 3 |
| [ABBV](tickers/ABBV - AbbVie Inc.md) | 2026-06-04 | +0.15 | 아퀴프타 EU 편두통 승인, 골드만삭스 컨퍼런스 6/9 참가 | 2 |
| [AZN](tickers/AZN - AstraZeneca PLC.md) | 2026-06-04 | -0.09 | 카미제스트란트 FDA 결정 연기·안셀라미맙 Phase 3 실패 | 2 |
| [UNH](tickers/UNH - UnitedHealth Group.md) | 2026-06-04 | +0.09 | BofA·MS·Truist 동시 목표주가 $450+ 상향, 소송 재부상 | 2 |
| [TMO](tickers/TMO - Thermo Fisher Scientific.md) | 2026-06-04 | -0.03 | Q1 컨센서스 초과·미생물학 사업부 $1.075B 매각, 가이던스 보수적 | 2 |
| [ABT](tickers/ABT - Abbott Laboratories.md) | 2026-06-04 | +0.03 | 이중 CGM EU CE 마크·Exact Sciences 인수 완료, 주가 +4.4% | 3 |

### 에너지 / 원자재

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [XOM](tickers/XOM - Exxon Mobil Corporation.md) | 2026-06-05 | +0.10 | 텍사스 본거지 이전 + 가이아나 900k bpd 기록 + OPEC+ 6/7 증산 경계 | 2 |
| [CVX](tickers/CVX - Chevron Corporation.md) | 2026-06-05 | -0.05 | 싱가포르 정제 매각 $21.7억 + 가스 비중 확대 vs 호르무즈 직격탄 | 2 |
| [COP](tickers/COP - ConocoPhillips.md) | 2026-06-05 | -0.03 | 생산 가이던스 1.5% 하향 + 포트아서 LNG 첫 생산 임박 | 2 |
| [SHEL](tickers/SHEL - Shell plc.md) | 2026-06-05 | +0.01 | 자사주 매입 지속 + Q1 배당 $0.3906 + Buy 컨센서스 목표가 $99 | 2 |
| [OXY](tickers/OXY - Occidental Petroleum.md) | 2026-06-05 | +0.05 | CEO 교체(Hollub→Jackson) + 멕시코만 Bandit 광구 석유 발견 | 2 |
| [SLB](tickers/SLB - Schlumberger Limited.md) | 2026-06-05 | -0.05 | Tachyus AI 인수 + 30일 +15% vs Q2 EPS -28.4% YoY 예상 | 2 |
| [FCX](tickers/FCX - Freeport-McMoRan.md) | 2026-06-05 | +0.04 | Grasberg 복구 지연 (-) + $3B 신용한도 + UBS $75 상향 (구리 낙관론) | 2 |
| [NEM](tickers/NEM - Newmont Corporation.md) | 2026-06-05 | +0.24 | Q1 FCF $31억 기록 (금 $4,900/oz) + $60억 자사주매입 | 2 |
| [LIN](tickers/LIN - Linde plc.md) | 2026-06-05 | +0.17 | Q1 EPS +10% + 배당 33년 연속 + 삼성 반도체 팹 최대 딜 | 2 |
| [APD](tickers/APD - Air Products and Chemicals.md) | 2026-06-05 | +0.17 | Q2 EPS +19% YoY + 웰스파고 OW 상향 + 삼성 반도체 팹 계약 | 2 |

### 금융

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [JPM](tickers/JPM - JPMorgan Chase and Co.md) | 2026-06-06 | +0.19 | 토큰화 예금 'The Bridge' 참여, 주가 $312 역대 최고권 | 2 |
| [BAC](tickers/BAC - Bank of America Corp.md) | 2026-06-06 | +0.13 | 크로스보더 실시간 결제 출시 예정, 연준 은행 건전성 확인 | 2 |
| [WFC](tickers/WFC - Wells Fargo and Company.md) | 2026-06-06 | +0.18 | CEO Q2 IB/트레이딩 중반 성장 전망, 배당 $0.45 선언 | 2 |
| [C](tickers/C - Citigroup Inc.md) | 2026-06-06 | +0.19 | 주가 +4% 다년간 고점, Q1 매출 +14% YoY, The Bridge 참여 | 2 |
| [GS](tickers/GS - The Goldman Sachs Group.md) | 2026-06-06 | +0.11 | 블록체인 부동산 펀드 출시, CEO AI 투자 탐욕 경고 | 2 |
| [MS](tickers/MS - Morgan Stanley.md) | 2026-06-06 | +0.19 | Q1 EPS $3.43 상회·ROTCE 27.1%, M&A·IPO 물결 전망 | 2 |
| [V](tickers/V - Visa Inc.md) | 2026-06-06 | +0.17 | Canton Network 스테이블코인 파일럿, FQ2 실적 상회 | 2 |
| [MA](tickers/MA - Mastercard Incorporated.md) | 2026-06-06 | -0.03 | CFO 교체(Ling Hai), 주가 $600 고점 대비 장기 하락세 | 2 |
| [AXP](tickers/AXP - American Express Company.md) | 2026-06-06 | -0.04 | BofA 투자의견 하향, 신용카드 연체율 13%(15년 최고) | 3 |
| [BRK-B](tickers/BRK-B - Berkshire Hathaway.md) | 2026-06-06 | +0.15 | Alphabet $10B 투자(6% 할인), 시총 $1.02조 돌파 | 2 |

### 소비재

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [WMT](tickers/WMT - Walmart Inc.md) | 2026-06-07 | +0.11 | Q1 FY27 이커머스 +26%, 동일점포 +4.1%, Q2 가이던스 제시 — 강한 실적에도 주가 조정 | 1 |
| [COST](tickers/COST - Costco Wholesale.md) | 2026-06-07 | +0.17 | Q3 FY26 매출 +11.6% (2022년 이후 최고) — 강한 실적에도 주가 하락, 소비 경기 고점 논쟁 | 1 |
| [KO](tickers/KO - The Coca-Cola Company.md) | 2026-06-07 | 0.00 | 금일 의미 있는 신규 뉴스 없음 — 배당귀족 60년 연속 방어적 특성 유지 | 0 |
| [PEP](tickers/PEP - PepsiCo.md) | 2026-06-07 | 0.00 | 금일 의미 있는 신규 뉴스 없음 — 음료+스낵 결합 모델 견조 | 0 |
| [PG](tickers/PG - Procter and Gamble.md) | 2026-06-07 | +0.11 | 소비자 수요 서프라이즈 주가 +5%, Native 클린뷰티·Secret 젠Z 마케팅 호응 | 0 |
| [MO](tickers/MO - Altria Group.md) | 2026-06-07 | -0.02 | 금일 신규 뉴스 없음 — 담배 볼륨 감소 구조적 헤드윈드, 배당수익률 7%대 인컴주 | 0 |
| [MCD](tickers/MCD - McDonalds Corporation.md) | 2026-06-07 | +0.03 | 수제 치킨 메뉴 테스트 (치킨 전쟁 대응), 내부자 거래 신고 (6/1) | 0 |
| [HD](tickers/HD - The Home Depot.md) | 2026-06-07 | -0.02 | 금일 신규 뉴스 없음 — 금리 인하 기대감이 중기 촉매, 주가 $310.78 | 0 |
| [NKE](tickers/NKE - NIKE Inc.md) | 2026-06-07 | -0.12 | 월드컵 중심 턴어라운드 전략에 애널리스트 회의적, 주가 $42.98 약세 지속 | 1 |
| [SBUX](tickers/SBUX - Starbucks Corporation.md) | 2026-06-07 | -0.15 | AI 재고관리 폐기·기관 41.9% 매도·1개월 -9% — 턴어라운드 신뢰도 급락 | 1 |

### 산업재 / 방산

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [CAT](tickers/CAT - Caterpillar Inc.md) | 2026-06-07 | +0.23 | Q1 매출 +22%·사상 최대 수주잔고·가이던스 상향, 에버코어 목표가 $1,103 상향 | 0 |
| [DE](tickers/DE - Deere & Company.md) | 2026-06-07 | +0.03 | 인디애나·NC 신규 시설 미국 제조 확장 — 대형 촉매 부재 | 3 |
| [BA](tickers/BA - The Boeing Company.md) | 2026-06-07 | +0.11 | CEO 787 월 10대 목표·4번째 737 라인 계획, Q1 실적 컨센서스 상회 | 0 |
| [LMT](tickers/LMT - Lockheed Martin Corp.md) | 2026-06-07 | +0.04 | 스컹크웍스 GM 교체 (4년간 3번째), FY26 방위예산 $8,950억 우호 환경 | 0 |
| [RTX](tickers/RTX - RTX Corporation.md) | 2026-06-07 | +0.16 | Q1 조정 EPS +21%, 신규 방산 계약·P&W 생산 확대, 목표가 $215~$240 | 0 |
| [NOC](tickers/NOC - Northrop Grumman Corp.md) | 2026-06-07 | +0.11 | 해군 $1억 계약, 아르테미스 III 발송, 배당 +6.93% 인상 — 3중 긍정 | 0 |
| [HON](tickers/HON - Honeywell International.md) | 2026-06-07 | -0.02 | Honeywell Aerospace 분사 기준일 6/15·완료 6/29 (HONA 상장), 1:2 역분할 | 1 |
| [GE](tickers/GE - GE Aerospace.md) | 2026-06-07 | +0.23 | Q1 주문 +87%·EPS +15.5% 서프라이즈, 수주잔고 $2,100억 역대 최대 | 0 |
| [UPS](tickers/UPS - United Parcel Service.md) | 2026-06-07 | -0.10 | 아마존 물량 50%+ 감축 가속·화물기 사고 조사, 배당수익률 6.66% | 1 |
| [FDX](tickers/FDX - FedEx Corporation.md) | 2026-06-07 | +0.11 | 연간 가이던스 상향·분사 계획 발표 — UPS 대비 상대적 강세 | 0 |

### 부동산 (REITs)

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [AMT](tickers/AMT - American Tower Corporation.md) | 2026-06-06 | -0.06 | REITweek CEO 발표, 1년 상대 수익률 시장(-14.7%) 하회 | 2 |
| [CCI](tickers/CCI - Crown Castle Inc.md) | 2026-06-06 | +0.12 | $8.5B 파이버·스몰셀 매각 완료, 타워 전문 REIT 전환 | 2 |
| [PLD](tickers/PLD - Prologis Inc.md) | 2026-06-06 | +0.12 | Q1 역대 최대 임대 64M sqft, 데이터센터 BTS $1.3B | 2 |
| [EQIX](tickers/EQIX - Equinix Inc.md) | 2026-06-06 | +0.20 | Q1 AI Fabric 예약 +70%, Citi 포커스리스트, $10B 가이던스 | 1 |
| [DLR](tickers/DLR - Digital Realty Trust.md) | 2026-06-06 | +0.12 | 2026 가이던스 상향, 런던 AI 이노베이션 랩, Stifel $235 | 2 |
| [O](tickers/O - Realty Income Corporation.md) | 2026-06-06 | +0.12 | 671번째 연속 월 배당, Q1 AFFO/주 +6.6%, Jefferies 매수 $69 | 2 |
| [SPG](tickers/SPG - Simon Property Group.md) | 2026-06-06 | +0.15 | Q1 순이익 +15.9%, 배당 +7.1%, Eli Simon 신임 CEO | 2 |
| [WELL](tickers/WELL - Welltower Inc.md) | 2026-06-06 | +0.19 | Q1 매출 +38.3%, 동일점포 NOI +16.4%, 점유율 88.8% | 2 |
| [PSA](tickers/PSA - Public Storage.md) | 2026-06-06 | +0.16 | NSA 인수 제안(+30% 자산), 시너지 $110-130M | 2 |
| [VICI](tickers/VICI - VICI Properties Inc.md) | 2026-06-06 | +0.21 | Golden Entertainment $1.16B 인수 완료, 밸류에이션 A- | 2 |

### 통신 / 미디어

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [VZ](tickers/VZ - Verizon Communications.md) | 2026-06-07 | -0.09 | 대법원 FCC 과징금 판결 → 주가 -4%, T-Mobile 경쟁 심화 | 1 |
| [T](tickers/T - AT&T Inc.md) | 2026-06-07 | -0.09 | 대법원 FCC 과징금 판결 → -4% 동반 하락, 광케이블 확장 장기 긍정 | 0 |
| [TMUS](tickers/TMUS - T-Mobile US.md) | 2026-06-07 | +0.16 | Charter·Comcast MVNO 독점 계약, Q1 강세·애널리스트 30%+ 상승 전망 | 0 |
| [CMCSA](tickers/CMCSA - Comcast Corporation.md) | 2026-06-07 | +0.03 | T-Mobile MVNO 비즈니스 계약 — 케이블 가입자 감소 속 B2B 다각화 | 0 |
| [CHTR](tickers/CHTR - Charter Communications.md) | 2026-06-07 | +0.03 | T-Mobile MVNO 계약, Q1 Spectrum Mobile +36.8만 (누계 12.1M) | 0 |
| [NFLX](tickers/NFLX - Netflix Inc.md) | 2026-06-07 | +0.20 | 광고 고객사 +70% YoY·매출 $30억 경로, 가입자 3.25억+, SPOT $1억 계약 | 0 |
| [DIS](tickers/DIS - The Walt Disney Company.md) | 2026-06-07 | +0.07 | Q2 스트리밍 영업이익 +88%·마진 11%, 반기 배당 $0.75 (기준일 6/30) | 0 |
| [SPOT](tickers/SPOT - Spotify Technology.md) | 2026-06-07 | +0.09 | Netflix와 $1억 독점 팟캐스트 영상 계약 — 콘텐츠 수익화 강화 | 0 |
| [EA](tickers/EA - Electronic Arts Inc.md) | 2026-06-07 | +0.10 | FY26 사상 최대 실적, $550억 비공개 인수 CFIUS 심사 최종 단계 | 1 |
| [TTWO](tickers/TTWO - Take-Two Interactive.md) | 2026-06-07 | +0.22 | GTA VI 2026년 11월 19일 확정, Q4 어닝 비트, 목표가 $280~$320 | 0 |

### 유틸리티 / 전력

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [NEE](tickers/NEE - NextEra Energy.md) | 2026-06-05 | +0.03 | Dominion $670억 합병 + 고금리·희석 우려로 -13.7% | 2 |
| [SO](tickers/SO - The Southern Company.md) | 2026-06-05 | -0.01 | 조지아파워 요금 인하 명령 vs Vogtle 3·4호기 정격 출력 | 2 |
| [DUK](tickers/DUK - Duke Energy Corporation.md) | 2026-06-05 | +0.08 | AI 데이터센터 원전 공급 테크 협의 + Q1 EPS $1.93 | 2 |
| [AEP](tickers/AEP - American Electric Power.md) | 2026-06-05 | +0.08 | Q1 EPS +7.3% YoY + $417억 4년 자본투자 (7.9% 요금기반 성장) | 2 |
| [EXC](tickers/EXC - Exelon Corporation.md) | 2026-06-05 | -0.01 | PECO 요금 신청 철회 + 송전 $1.5B 증액 — 혼조 신호 | 2 |
| [CEG](tickers/CEG - Constellation Energy.md) | 2026-06-05 | +0.09 | MSFT+Meta 5,650MW 원전 PPA + YTD -25% → 역발상 매력 | 2 |
| [VST](tickers/VST - Vistra Corp.md) | 2026-06-05 | +0.10 | Meta 20년 PPA 2,600MW + 로터스 가스발전 7개 인수 | 2 |
| [SRE](tickers/SRE - Sempra.md) | 2026-06-05 | +0.03 | Voss Capital Oncor 분리 촉구 — 구조적 가치 해제 잠재력 | 2 |
| [ED](tickers/ED - Consolidated Edison.md) | 2026-06-05 | 0.00 | 의미있는 뉴스 없음 — 49년 배당 성장 안정 인컴주 | 1 |
| [D](tickers/D - Dominion Energy.md) | 2026-06-05 | +0.08 | NEE 합병 발표 + 130GW AI 파이프라인 + 규제 승인이 관건 | 2 |

### 조선 (한국)

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [329180.KS](tickers/329180.KS - HD Hyundai Heavy Industries.md) | 2026-06-03 | +0.33 | VLGC 8척 1.416조원 수주, 연간 목표 60.8% 조기 달성, KDDX 소송 | 2 |
| [042660.KS](tickers/042660.KS - Hanwha Ocean Co.md) | 2026-06-03 | +0.13 | Leidos 미 해군 설계 협력, 캐나다 해군 MOU 체결 | 2 |
| [010140.KS](tickers/010140.KS - Samsung Heavy Industries.md) | 2026-06-03 | +0.25 | FDC 시장 선점 — Capital/LR MOU·Supermicro AI 서버 JDP | 2 |

## 오늘의 시그널 (2026-06-09 · 화요일 · 반도체)

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장 (예: 비만치료제 임상 데이터 연속)
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈 (예: 관세, FOMC, 유가, 비만치료제, 데이터센터 전력) 로 동시 움직임

**2026-06-09 감지된 시그널:**

- **역방향 (INTC)**: 2026-06-02 -0.20 → 2026-06-09 +0.35 — 구글 TPU 파운드리 수주 단독 호재가 주가 +11%·narrative 역전. 6월 2주 만에 파운드리 비즈니스의 구조적 전환점. COMPUTEX 실망 대비 극적 반전.
- **역방향 (AVGO)**: 2026-06-02 +0.39 → 2026-06-09 -0.09 — AI 매출 2배에도 가이던스 미상향으로 -15%. "좋은 실적 + 기대 미충족 = 급락" 하이퍼성장주 공식 재확인.
- **섹터 동기화 (장비 슈퍼사이클)**: AMAT +0.29 / LRCX +0.21 / ASML +0.30 — 장비 3사 동시 강세. AMAT 사상 최대 실적·LRCX WFE $1,400억·ASML Terafab이 동일 테마 강화.
- **섹터 동기화 (AI 메모리 수요)**: MU +0.35 / 반도체 장비 섹터 동반 강세 — DRAM +58~63% 예측과 HBM 공급 부족이 메모리+장비 투트랙 수혜 확인.
- **연속성 (인텔 파운드리 반등)**: 2026-06-02 COMPUTEX 실망 → 2026-06-09 구글 TPU 수주. 2주 연속 인텔 파운드리 이슈가 섹터 센티멘트 주요 변수로 등장. NVDA의 18A 평가가 다음 30일 핵심 모니터링 변수.
- **최고 시그널**: INTC +0.35 — 구글 TPU·NVDA 18A·+11% 세 호재가 단하루 집중. 파운드리 사업 구조 전환의 역사적 일.
- **경고 시그널**: AVGO -0.09 — AI 매출 2배에도 시장 기대 미달. "AI 기대주는 가이던스가 모든 것" 원칙 재확인. QCOM +0.07 — 반등에도 6/5 급락 상처 잔존, 6/24 인베스터 데이가 최후 판단 시점.
- **주목 이벤트**: 6/24 MU Q3 FY2026 어닝(±20% 예상), 6/24 QCOM 인베스터 데이 Dragonfly 발표, NVDA 18A 평가 결과 (수주 미확정 — 60일 대기).

### 감지된 패턴 (2026-06-06 · 토요일 · 금융 + 부동산 (REITs))

## 오늘의 시그널 (2026-06-06 · 토요일 · 금융 + 부동산 (REITs))

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장 (예: 비만치료제 임상 데이터 연속)
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈 (예: 관세, FOMC, 유가, 비만치료제, 데이터센터 전력) 로 동시 움직임

**2026-06-06 감지된 시그널:**

- **섹터 동기화 (토큰화 예금 네트워크)**: JPM·BAC·C — The Clearing House 주관 'The Bridge' 공동 구축. 대형 은행 3사가 블록체인 결제 인프라를 공동 건설하는 구조적 변화 신호. Visa·Mastercard의 스테이블코인 파일럿과 함께 금융 디지털화 가속.
- **섹터 동기화 (금융주 강세)**: JPM +0.19, C +0.19, MS +0.19, WFC +0.18 — 4종목이 동시에 강한 긍정 모멘텀. 금리 고정(3.5%) 환경에서도 IB 수수료·수익 다각화로 섹터 전반 리레이팅.
- **섹터 동기화 (AI 데이터센터 REIT)**: EQIX +0.20, VICI +0.21, WELL +0.19 — REIT 상위권이 모두 AI 수요 또는 인구통계 트렌드 수혜. EQIX AI Fabric +70% 가 데이터센터 REIT 강세의 핵심.
- **모순 (PSA)**: 2026-05-17 -0.03 (Q1 미스) → 2026-06-06 +0.16 (NSA 인수+운영 개선) — NSA 전략적 인수 발표가 단기 실적 부진을 완전 역전.
- **경고 신호**: MA -0.03, AXP -0.04 — 결제 양강과 고급카드가 동시 부정 모멘텀. MA는 장기 하락추세+CFO 교체, AXP는 BofA 하향+연체율 15년 최고. 결제 섹터 내 양극화 심화(네트워크 모델 강세 vs 신용 모델 약세).
- **AMT 경고**: -0.06으로 REIT 섹터 유일 부정 점수 — 금리 유지 환경에서 글로벌 타워 REIT의 상대 수익률 부진. CCI의 타워 집중 전환이 AMT에 경쟁 압력 추가.
- **섹터간 전파 (AI capex → 금융 + REIT)**: Alphabet $80B AI 인프라 → BRK $10B 투자(금융), EQIX AI Fabric 수요 3배 증가(REIT). AI 인프라 투자 붐이 금융(대출·투자) + 데이터센터 REIT 동시 수혜 확인.

### 감지된 패턴 (2026-06-05 · 금요일 · 에너지 / 원자재 + 유틸리티 / 전력)

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

### 감지된 패턴 (2026-06-08 · 빅테크 / 소프트웨어)

- **섹터 동기화 (AI 인프라 초대형 투자)**: GOOGL capex $180~190B + META capex $145B + AMZN Corning 광섬유 계약 — 빅테크 AI 인프라 군비경쟁 본격화. 반도체·데이터센터 REIT 동반 수혜 기대.
- **섹터 동기화 (어닝 서프라이즈 물결)**: CRM +47% narrative (+0.47), PLTR +46% (+0.46), ORCL +30% (+0.30) — 엔터프라이즈 AI SaaS 어닝 서프라이즈 동시 다발.
- **역방향 신호**: ADBE -0.17 — YTD -27.49%, Q2 실적 불확실성·CEO 교체로 섹터 내 유일한 약세. AI 크리에이티브 시장 경쟁 심화 vs. 섹터 전반 강세 간 디커플링.
- **최고 신호**: CRM +0.47 — Agentforce ARR +205%, Q1 EPS 24% 어닝 서프라이즈. PLTR +0.46 — FY2026 가이던스 +71%, 미국 세 자릿수 성장.
- **경고 신호**: ADBE -0.17 — 섹터 내 유일한 약세. AAPL +0.09 — WWDC Apple Intelligence 공개에도 sell-the-news -1.89%.
- **섹터간 전파**: 빅테크 AI capex 확대 → 반도체(NVDA·AVGO) + 유틸리티(AI 전력수요) + 광섬유(Corning) 연쇄 수혜. IBM $10B 양자 투자 → 양자컴퓨팅 테마 부각.

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
