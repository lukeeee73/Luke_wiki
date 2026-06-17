---
title: "Watchlist News Dashboard"
created: 2026-05-16
updated: 2026-06-17
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
| [AAPL](tickers/AAPL - Apple Inc.md)                     | 2026-06-15 | +0.03  | WWDC 후 주가 8% 하락, MS PT $360 상향, 시리 AI 베타 미국 한정 (EU·중국 제외) | 1           |
| [MSFT](tickers/MSFT - Microsoft Corporation.md)         | 2026-06-15 | +0.15  | Q3 Azure +40% / AI $37B 런레이트(+123%), 배당 $0.91, Xbox 대규모 감원 | 2           |
| [GOOGL](tickers/GOOGL - Alphabet Inc.md)                | 2026-06-15 | +0.21  | +3.19% 급등, Q1 순이익 +81%, AI 에이전트 6/12 공개, 배당 $0.22 지급   | 2           |
| [AMZN](tickers/AMZN - Amazon.com Inc.md)                | 2026-06-15 | +0.10  | +3.70% 급등, 프라임데이 6/23~26 확정, EU·FTC 이중 규제 리스크           | 2           |
| [META](tickers/META - Meta Platforms Inc.md)            | 2026-06-15 | +0.11  | 비즈니스 AI 에이전트 글로벌 출시, 광고 AI 전환율 개선 확인, YTD -13%   | 1           |
| [ORCL](tickers/ORCL - Oracle Corporation.md)            | 2026-06-15 | +0.07  | Q4 IaaS +93%·클라우드 +47% 달성, $20B 유상증자 → 주가 8~10% 급락     | 2           |
| [CRM](tickers/CRM - Salesforce, Inc.md)                 | 2026-06-15 | +0.26  | $36억 Fin 인수(AI 에이전트), Q1 EPS +50%, Agentforce ARR $1.2B (+205%) | 2           |
| [ADBE](tickers/ADBE - Adobe Inc.md)                     | 2026-06-15 | +0.06  | Q2 EPS 비트+가이던스 상향, CFO 퇴임+3개 다운그레이드, 6일 -19% 후 +1.7% | 2           |
| [IBM](tickers/IBM - International Business Machines.md) | 2026-06-15 | +0.21  | Q1 FCF +13%, ServiceNow 협력, Anderon 양자 파운드리 설립, ATH 대비 -17% | 2           |
| [PLTR](tickers/PLTR - Palantir Technologies Inc.md)     | 2026-06-15 | +0.20  | +5.2% ($134.71), 목표가 $225 상향, Q1 +85%, 구글·GNP·McCarthy 파트너십 | 2           |

### 반도체

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [NVDA](tickers/NVDA - NVIDIA Corporation.md) | 2026-06-16 | +0.23 | 시총 $5.1조 세계 1위, NAVER AI 파트너십, SOX -10% 여진 후 회복·52주 고점 -26% | 5 |
| [AMD](tickers/AMD - Advanced Micro Devices.md) | 2026-06-16 | +0.31 | MEXT 인수 + Ryzen AI Halo $3,999 출시로 52주 고점($547) 달성, 시총 $9,000억 돌파 | 5 |
| [TSM](tickers/TSM - Taiwan Semiconductor Mfg.md) | 2026-06-16 | +0.30 | 5월 매출 +30.1% YoY·시총 $2.28조 최고, 3nm 15% 가격 인상 공급자 우위 확인 | 4 |
| [AVGO](tickers/AVGO - Broadcom Inc.md) | 2026-06-16 | -0.11 | Q2 AI $10.8B(2배) 달성에도 FY 미상향 -15%, 구글 TPU 다변화 리스크 재부각 | 6 |
| [INTC](tickers/INTC - Intel Corporation.md) | 2026-06-16 | +0.04 | NVDA RTX Spark 경쟁 -1.95%, 구글 300만 TPU 수주(6/8), YTD +250% 밸류에이션 부담 | 5 |
| [QCOM](tickers/QCOM - QUALCOMM Incorporated.md) | 2026-06-16 | +0.12 | Tenstorrent $8-10B 인수 협의, Humain 200MW 계약, 6/24 인베스터 데이 8일 대기 | 6 |
| [ASML](tickers/ASML - ASML Holding NV.md) | 2026-06-16 | +0.28 | YTD +69.2% 후 -4.7% 조정, CEO Terafab '매우 진지', 4개 증권사 PT 동시 상향 | 5 |
| [AMAT](tickers/AMAT - Applied Materials.md) | 2026-06-16 | +0.29 | P/S 16배 역대 최고, Q2 사상 최대·WFE 30%+ 상향, 싱가포르 $5억 캠퍼스 | 5 |
| [LRCX](tickers/LRCX - Lam Research Corp.md) | 2026-06-16 | +0.27 | Q3 사상 최대 $58.4억·Q4 가이던스 $66억, 첨단 패키징 +50%, 6/17 배당 권리락 | 6 |
| [MU](tickers/MU - Micron Technology.md) | 2026-06-16 | +0.32 | NVDA HBM4 인증(Vera Rubin), 미국 1α DRAM 생산 개시, 6/24 Q3 실적 기대 | 6 |

### 로보틱스 / 피지컬 AI

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [TER](tickers/TER - Teradyne, Inc.md) | 2026-06-16 | +0.29 | Nasdaq-100 6/22 편입, 공군 $1.4억 다년 계약, Q1 AI 수요 70%, Automate 2026 준비 | 4 |
| [HSAI](tickers/HSAI - Hesai Group.md) | 2026-06-16 | -0.05 | 8:1 주식 분할 AGM(6/26), Kosmo 3D 센서 출시, YTD -23.42% 지정학·경쟁 복합 압박 | 4 |
| [MP](tickers/MP - MP Materials Corp.md) | 2026-06-16 | +0.01 | 애플·DoD 장기 공급 계약, 미중 협정 진전 → 지정학 프리미엄 해소 -10%, CEO 매도 | 4 |

### 자동차 / 모빌리티

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [TSLA](tickers/TSLA - Tesla Inc.md) | 2026-06-17 | +0.06 | JPMorgan PT $475 상향(자율주행 재평가), Q1 FCF 적자, 사이버트럭 생산 확대 | 2 |
| [TM](tickers/TM - Toyota Motor Corporation.md) | 2026-06-17 | -0.12 | 렉서스 EV 개발 중단, FY2026 순이익 -19.24%, 5월 미국 판매 -0.6%, 8만2천대 리콜 | 2 |
| [F](tickers/F - Ford Motor Company.md) | 2026-06-17 | -0.20 | 5월 미국 판매 -13.6%·EV -22.2%, 42만대 리콜, EBIT 마진 -4.5% | 2 |
| [GM](tickers/GM - General Motors Company.md) | 2026-06-17 | +0.07 | 2027 실버라도 공개, 테네시 LFP→에너지저장 전환, 배당 $0.18(6/18) | 1 |
| [STLA](tickers/STLA - Stellantis NV.md) | 2026-06-17 | -0.09 | 다수 집단소송 제기, 씨티 목표가 EUR 7.20 하향, 전고체 배터리 테스트 긍정 | 2 |
| [HMC](tickers/HMC - Honda Motor Co.md) | 2026-06-17 | -0.19 | 70년 만의 연간 적자(관세+EV 구조조정 $9B+), 5월 미국 판매 +9.9% | 1 |
| [RIVN](tickers/RIVN - Rivian Automotive.md) | 2026-06-17 | +0.01 | R2 양산 개시, AT&T 5G 파트너십(+6%), NHTSA R1S 서스펜션 조사, 2% 감원 | 3 |
| [NIO](tickers/NIO - NIO Inc.md) | 2026-06-17 | +0.21 | Q1 EPS +105.6% 서프라이즈, 5월 인도 +62.3%, Onvo L60 가격 인하 | 2 |
| [005380.KS](tickers/005380.KS - Hyundai Motor Company.md) | 2026-06-17 | +0.08 | HMGMA 2단계 $27억(+20만대·3,000일자리), Pleos Connect 출시, 박민우 42dot 수장 | 2 |
| [000270.KS](tickers/000270.KS - Kia Corporation.md) | 2026-06-17 | 0.00 | 신규 재료 없음, 다음 실적 발표 7/17 예정 | 1 |

### 바이오 / 제약 / 헬스케어

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [LLY](tickers/LLY - Eli Lilly and Company.md) | 2026-06-11 | +0.34 | 경구 GLP-1 Foundayo FDA 최초 승인·Ebglyss 8주 투약 승인·메디케어 GLP-1 7/1 적용 시작 | 3 |
| [NVO](tickers/NVO - Novo Nordisk AS.md) | 2026-06-11 | -0.14 | 경구 위고비 300만 처방에도 LLY FDA 승인으로 가려져 주가 약세 지속 | 4 |
| [JNJ](tickers/JNJ - Johnson and Johnson.md) | 2026-06-11 | +0.19 | Firefly Bio $10억 인수·FY2026 가이던스 $100.8B 상향·닙포칼리맙 SLE 2상 성공 | 3 |
| [PFE](tickers/PFE - Pfizer Inc.md) | 2026-06-11 | -0.08 | RBC 등급 Sector Perform 상향·SOLIS-1 2상 시작·H2 종양학 3상 데이터 예정 | 3 |
| [MRK](tickers/MRK - Merck and Co.md) | 2026-06-11 | +0.03 | 경구 HIV 치료 3상 성공(Gilead 공동)·KEYNOTE-D46 폐암 병용 중단·주가 +1.5% | 3 |
| [ABBV](tickers/ABBV - AbbVie Inc.md) | 2026-06-11 | +0.17 | 아퀴프타 EU 편두통 급성기 승인·EHA 2026 혈액암 데이터·스카이리지 성장 지속 | 2 |
| [AZN](tickers/AZN - AstraZeneca PLC.md) | 2026-06-11 | +0.19 | 경구 GLP-1 엘레코글리프론 Phase 3 진입·2025 실적 매출+8.6%·컨센서스 $224 Strong Buy | 3 |
| [UNH](tickers/UNH - UnitedHealth Group.md) | 2026-06-11 | -0.20 | CMS 2027 메디케어 요율 동결·버크셔 지분 완전 매각·독점금지 조사 지속 | 3 |
| [TMO](tickers/TMO - Thermo Fisher Scientific.md) | 2026-06-11 | +0.15 | Q1 어닝 비트 + FY EPS 가이던스 상향·ASMS 신형 질량분석기 2종 공개 | 3 |
| [ABT](tickers/ABT - Abbott Laboratories.md) | 2026-06-11 | +0.08 | 리브레 듀오 EU CE 마크(세계 최초 이중 CGM)·Exact Sciences 인수 완료 | 3 |

### 에너지 / 원자재

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [XOM](tickers/XOM - Exxon Mobil Corporation.md) | 2026-06-12 | +0.07 | 가이아나 $46.7억 이익 + 베네수엘라 협상 진전 vs 미·이란 딜 유가 하락 리스크 | 2 |
| [CVX](tickers/CVX - Chevron Corporation.md) | 2026-06-12 | +0.10 | 미국 생산 +24% (헤스 통합) + $60억 주주환원 + Buy 컨센서스 $216 | 2 |
| [COP](tickers/COP - ConocoPhillips.md) | 2026-06-12 | -0.01 | 잭스 에너지 피크 선정 vs 2026 생산 가이던스 2.295-2.325 MMBOED 하향 | 2 |
| [SHEL](tickers/SHEL - Shell plc.md) | 2026-06-12 | +0.09 | CEO 유가 5~10년 상승 전망 + 나미비아 경질유 발견 + 자사주 매입 지속 | 2 |
| [OXY](tickers/OXY - Occidental Petroleum.md) | 2026-06-12 | +0.09 | OxyChem $58억 부채 감소 + 6개월 +35% 랠리 — 밸류에이션 점검 국면 | 2 |
| [SLB](tickers/SLB - Schlumberger Limited.md) | 2026-06-12 | +0.05 | 퀄컴 엣지 AI 파트너십 + 디지털 투자자의 날 — 디지털 전환 리더십 | 2 |
| [FCX](tickers/FCX - Freeport-McMoRan.md) | 2026-06-12 | +0.01 | Q1 어닝 21% 상회 vs 그라스베르그 40% 삭감 + 구리 $5.80/lb 역대 최고 | 2 |
| [NEM](tickers/NEM - Newmont Corporation.md) | 2026-06-12 | -0.16 | 금 가격 $4,331 (-16.6%) + 생산 -10% + AISC $1,680 — 이중 압박 | 2 |
| [LIN](tickers/LIN - Linde plc.md) | 2026-06-12 | +0.11 | Q1 EPS +10% + 배당 $1.60 (6/18) + RBC 목표가 $570 상향 | 2 |
| [APD](tickers/APD - Air Products and Chemicals.md) | 2026-06-12 | +0.03 | 나스닥 대비 YTD 초과 성과 + NEOM 그린수소 프로젝트 지속 | 1 |

### 금융

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [JPM](tickers/JPM - JPMorgan Chase and Co.md) | 2026-06-13 | +0.06 | AI 에이전트 하반기 배포·Prometheus $120억 투자 참여 vs DOJ 디뱅킹 소환장 | 3 |
| [BAC](tickers/BAC - Bank of America Corp.md) | 2026-06-13 | +0.04 | 크로스보더 결제 연내 출시·우선주 배당 공시 vs DOJ 소환장+AI 규제 강화 | 3 |
| [WFC](tickers/WFC - Wells Fargo and Company.md) | 2026-06-13 | +0.14 | Q2 시장 부문 중간 십대 % 성장 전망·배당 $0.45 vs DOJ 소환장 | 3 |
| [C](tickers/C - Citigroup Inc.md) | 2026-06-13 | +0.25 | 블록체인 토큰화 주식 거래 플랫폼 출시 (+5.6%)·CFO 강한 가이던스 | 3 |
| [GS](tickers/GS - The Goldman Sachs Group.md) | 2026-06-13 | +0.32 | 스페이스X 미국 최대 IPO 주관·앤트로픽 공동 주관·목표가 $900 상향 | 3 |
| [MS](tickers/MS - Morgan Stanley.md) | 2026-06-13 | +0.21 | 자산관리 $9조 달성·앤트로픽 IPO 공동 주관·어닝 리비전 상향 | 3 |
| [V](tickers/V - Visa Inc.md) | 2026-06-13 | +0.34 | FQ2 매출 +17% 13년 최고·OpenAI 결제 통합·스테이블코인 파일럿 | 3 |
| [MA](tickers/MA - Mastercard Incorporated.md) | 2026-06-13 | +0.17 | Agent Pay for Machines 출시·교환수수료 합의 예비 승인·CFO 교체 | 3 |
| [AXP](tickers/AXP - American Express Company.md) | 2026-06-13 | +0.06 | CFO 수수료 전망 긍정·델타 파트너십 갱신 vs 연체율 13% 15년 최고 | 4 |
| [BRK-B](tickers/BRK-B - Berkshire Hathaway.md) | 2026-06-13 | +0.12 | 알파벳 $80억 AI 공모 $100억 투자·시총 $1.05조·Abel CEO 안정화 | 3 |

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
| [AMT](tickers/AMT - American Tower Corporation.md) | 2026-06-13 | +0.03 | 배당 $1.79 (권리락 6/12)·DISH 계약 종료 역풍·CCI 타워 경쟁 심화 | 3 |
| [CCI](tickers/CCI - Crown Castle Inc.md) | 2026-06-13 | +0.20 | $85억 파이버·소형셀 매각 완료·AFFO 가이던스 $4.53~$4.65 상향 | 2 |
| [PLD](tickers/PLD - Prologis, Inc.md) | 2026-06-13 | +0.12 | 52주 신고가 $147.93·RBC $148·Truist $154·Citi $145 목표주가 상향 | 2 |
| [EQIX](tickers/EQIX - Equinix, Inc.md) | 2026-06-13 | +0.30 | Citi 포커스리스트·연매출 $101~102억 가이던스·AI Fabric 예약 +70%·연결 3배 | 2 |
| [DLR](tickers/DLR - Digital Realty Trust.md) | 2026-06-13 | +0.12 | EPS 리비전 A+·바르셀로나 BCN1 개장·Q2 배당 $1.22 | 3 |
| [O](tickers/O - Realty Income Corporation.md) | 2026-06-13 | +0.07 | 월 배당 $0.271 (0.2% 인상)·수익률 5.32%·방어적 안정성 유지 | 3 |
| [SPG](tickers/SPG - Simon Property Group.md) | 2026-06-13 | +0.19 | Q1 순이익 +15.9%·FFO 가이던스 상향·Eli Simon 신임 CEO 공식 취임 | 3 |
| [WELL](tickers/WELL - Welltower Inc.md) | 2026-06-13 | +0.15 | Q1 모든 지표 호조·+3.4% (6/9) vs say-on-pay 부결 거버넌스 리스크 | 3 |
| [PSA](tickers/PSA - Public Storage.md) | 2026-06-13 | +0.17 | NSA 결합 제안 (자산+30%, 시너지 $1.1~1.3억)·Q1 점유율 92.2% 1위 | 3 |
| [VICI](tickers/VICI - VICI Properties Inc.md) | 2026-06-13 | +0.17 | AFFO 가이던스 상향·One Beverly Hills $15억 메자닌·캐나다 카지노 인수 | 3 |

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
| [NEE](tickers/NEE - NextEra Energy.md) | 2026-06-12 | -0.04 | Dominion $670억 인수 발표 — NEE -9% 희석 우려 vs 세계 최대 유틸리티 창출 | 2 |
| [SO](tickers/SO - The Southern Company.md) | 2026-06-12 | +0.08 | 보글 원전 3·4호기 완전 가동 + 조지아·앨라배마 AI 데이터센터 수요 성장 | 2 |
| [DUK](tickers/DUK - Duke Energy Corporation.md) | 2026-06-12 | +0.08 | 캐롤라이나 10GW 신규 발전 조달 + 미국 최대 데이터센터 밀집 영역 서비스 | 2 |
| [AEP](tickers/AEP - American Electric Power.md) | 2026-06-12 | +0.07 | Q1 EPS $1.64 + 가이던스 $6.12~6.42 유지 + 목표가 $141 (10% 상승 여력) | 2 |
| [EXC](tickers/EXC - Exelon Corporation.md) | 2026-06-12 | +0.02 | 분기 배당 $0.42 + 순수 T&D — 시카고·필라델피아·볼티모어 AI 인프라 간접 수혜 | 2 |
| [CEG](tickers/CEG - Constellation Energy.md) | 2026-06-12 | +0.19 | TMI FERC 면제 허가 + 5,650MW 하이퍼스케일러 PPA + 2차공모 오버행 해소 기대 | 2 |
| [VST](tickers/VST - Vistra Corp.md) | 2026-06-12 | +0.21 | Q1 EBITDA +20% + EBITDA 가이던스 $68~76억 재확인 + 메타 2,600MW PPA | 2 |
| [SRE](tickers/SRE - Sempra.md) | 2026-06-12 | +0.04 | 포트아서 LNG 1단계 건설 진행 + SoCal 유틸리티 에너지 효율 프로그램 안정적 | 2 |
| [ED](tickers/ED - Consolidated Edison.md) | 2026-06-12 | +0.02 | YTD +14.5% 방어주 성과 + 49년 연속 배당 증가 (배당귀족 유지) | 1 |
| [D](tickers/D - Dominion Energy.md) | 2026-06-12 | +0.10 | NEE $670억 인수로 오늘 주가 급등 — 버지니아 DC 클러스터(~70% 인터넷) 핵심 자산 | 2 |

### 조선 (한국)

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [329180.KS](tickers/329180.KS - HD Hyundai Heavy Industries.md) | 2026-06-17 | -0.18 | KDDX ₩7.8조 입찰 탈락(보안 벌점 결정적), 가처분 기각 → 한화오션 수주 확정 | 1 |
| [042660.KS](tickers/042660.KS - Hanwha Ocean Co.md) | 2026-06-17 | +0.30 | KDDX ₩7.8조 수주(이지스 6척, 2030년), +7.85% 급등, 캐나다 CPSP 후보 | 2 |
| [010140.KS](tickers/010140.KS - Samsung Heavy Industries.md) | 2026-06-17 | +0.25 | 델핀 FLNG $29억·Cedar LNG 진수(세계 최초 3기 동시)·GTT LNG 2척·베트남 ₩3,410억 | 2 |
| [010620.KS](tickers/010620.KS - HD Hyundai Mipo Dockyard Co. Ltd..md) | 2026-06-17 | +0.05 | Q2/Q3 PCTC·MR 탱커 납기 순조, 메탄올 추진 MR 탱커 시장 선두 | 1 |

## 오늘의 시그널 (2026-06-17 · 수요일 · 자동차 / 모빌리티 + 조선 (한국))

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈로 동시 움직임

**2026-06-17 감지된 시그널:**

- **최고 시그널 (042660.KS +0.30)**: KDDX ₩7.8조 수주 단독 수확 — 이지스 구축함 6척 2030년 납품, 캐나다 CPSP 후보 부상, 온타리오 파트너십까지 삼중 호재. 한국 해군 함정 시장 주도권을 단번에 획득.
- **최고 시그널 (NIO +0.21)**: Q1 EPS 컨센서스 105.6% 상회 + 5월 인도 +62.3% + Onvo L60 가격 경쟁력 — 중국 EV 섹터 내 최강 모멘텀 주. 전통 완성차(F·TM·HMC) 대비 중국 EV 스타트업 디커플링이 극명.
- **역방향 (329180.KS → 042660.KS)**: KDDX 패자(-0.18) vs 승자(+0.30)의 극명한 대조. 보안 벌점(-1.2점)이 ₩7.8조를 가른 결정적 요인 — 방산 조선사 내부 관리 리스크의 실질 비용 확인.
- **섹터 동기화 (일본 완성차 EV 후퇴)**: TM(-0.12, 렉서스 EV 중단) + HMC(-0.19, 70년 만의 연간 적자) — 일본 완성차 1·2위 모두 EV 전환 비용 직격. 일본 자동차 섹터의 구조적 EV 전환 지체가 단기 악재·장기 경쟁력 의문으로 부각.
- **섹터 동기화 (완성차 전반 EV 수요 둔화)**: F(-0.20, EV -22.2%) + TM(-0.12) + HMC(-0.19) — 전통 완성차 3종목이 공통으로 EV 수요 부진, 판매 둔화, 리콜 악재로 동반 약세. EV 전환 비용 부담이 섹터 전반 헤드윈드.
- **섹터 동기화 (K-조선 방산+LNG 동시 수주 러시)**: 042660.KS(KDDX 방산) + 010140.KS(Delfin FLNG + Cedar LNG) + 010620.KS(PCTC·MR 납기) — K-조선 3사 모두 수주 집행 모멘텀. 방산·FLNG·중소형 특수선 3개 세그먼트가 동시 강세로 조선 섹터 수퍼사이클 재확인.
- **모순 (RIVN 급반전)**: 2026-06-03 +0.30 → 2026-06-17 +0.01 — R2 실제 양산 시작에도 NHTSA 조사·2% 감원이 모멘텀 급감. "출시 기대 → 출시 현실" 전환 과정에서 실행 리스크 현실화.
- **연속성 (STLA 법적 리스크)**: 2026-06-03 -0.30(증권사기 소송 마감) → 2026-06-17 -0.09(다수 집단소송 제기) — 2주 연속 법적 리스크 테마. 소송 비용 누적이 밸류에이션 디스카운트 확대 요인.
- **주목 이벤트**: GM 배당 $0.18 지급(6/18), 현대차 배당 지급(6/30), 기아 다음 실적 발표(7/17), 042660.KS 캐나다 CPSP 최종 수주 결정(미정), 010140.KS Delfin FLNG 착공 일정.

### 감지된 패턴 (2026-06-16 · 화요일 · 반도체 + 로보틱스 / 피지컬 AI)

## 오늘의 시그널 (2026-06-16 · 화요일 · 반도체 + 로보틱스 / 피지컬 AI)

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈로 동시 움직임

**2026-06-16 감지된 시그널:**

- **최고 시그널 (AMD +0.31)**: MEXT 인수 완료 + Ryzen AI Halo $3,999 출시로 52주 고점 + 시총 $9,000억 돌파. 12개월 +300% 랠리 지속 — AI PC(에지)·데이터센터 양축 동시 공략으로 NVDA와의 경쟁이 반도체 최대 테마로 부상.
- **최고 시그널 (MU +0.32)**: NVDA Vera Rubin HBM4 공식 인증 + 미국 1α DRAM 생산 개시 + 6/24 Q3 실적 이중 카탈리스트. HBM 공급자 우위 시장 + 국내 생산 보조금 양방향 수혜 구조.
- **섹터 동기화 (WFE 슈퍼사이클 가속)**: AMAT +0.29 / LRCX +0.27 / ASML +0.28 — 장비 3사 일제히 강세. AMAT P/S 16배 역대 최고·LRCX Q3 사상 최대·ASML CEO Terafab '진지' — WFE 사이클이 AI 수요로 새로운 고점 도달.
- **섹터 동기화 (AI PC 3파전)**: NVDA RTX Spark / AMD Ryzen AI Halo / INTC 신규 AI 칩 — 에지 AI PC 시장에서 3강 동시 격돌. INTC -1.95%·AMD +6.98%·NVDA +3%로 당일 AMD 압도적 우세. 단기 시장점유율 변화 모니터링 필요.
- **연속성 (TSM 가격 인상 → 업스트림 강세)**: 3nm 15% 인상 + 5월 +30.1% + 시총 $2.28조 최고 — 2주 연속 TSMC 공급자 우위 확인. 칩 업체(NVDA·AMD) 원가 상승 vs 파운드리(TSM) 마진 개선 양극화 심화.
- **역방향 (AVGO 추가 약세)**: -0.02 → -0.11 — 구글 TPU 다변화로 추가 하락. Q2 발표 이후 2주 연속 부정적 신호. Q3 실적(8월)이 반전 여부 최후 판단 시점.
- **역방향 (INTC 상승 후 조정)**: 6/8 구글 수주 +11% → 6/16 NVDA 경쟁 -1.95%. YTD +250% 랠리 후 AI PC 경쟁 구도 재평가 시작. 신규 AI 칩 2026 말 제한 출하 타이밍이 관건.
- **신규 섹터 (로보틱스 / 피지컬 AI)**: TER +0.29 (Nasdaq-100 편입+공군 계약) / HSAI -0.05 (지정학·가격경쟁) / MP +0.01 (미중 협정 지정학 프리미엄 해소). 로보틱스 내 미국(TER)·중국(HSAI)·원자재(MP) 3중 분기 — 지정학이 핵심 차별화 요인.
- **경고 (밸류에이션 과열)**: AMAT P/S 16배(닷컴 초과) / TER GF Value +129% 과대평가 / AMD YTD +300% — 반도체·로보틱스 전반 밸류에이션 고점 경보. WFE 사이클 피크아웃 신호 감지 시 급격한 조정 위험.
- **주목 이벤트**: 6/17(내일) LRCX 배당 권리락, 6/22 TER Nasdaq-100 편입·Automate 2026, 6/24 MU Q3 실적(GS $900·Cowen $1,500 목표)·QCOM 인베스터 데이·NVDA 주주총회·HSAI AGM(8:1 분할), AMD Q2 어닝(7월 예정).

### 감지된 패턴 (2026-06-10 · 화요일 · 반도체)

## 오늘의 시그널 (2026-06-10 · 화요일 · 반도체)

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장 (예: 비만치료제 임상 데이터 연속)
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈 (예: 관세, FOMC, 유가, 비만치료제, 데이터센터 전력) 로 동시 움직임

**2026-06-10 감지된 시그널:**

- **연속성 (TSMC 가격 인상)**: 2주 연속 3nm 가격 인상 테마 등장 — TSM·NVDA·AMD 모두 연관. 5월 매출 +30.1% 발표로 수요 이탈 없이 가격 협상력 확인. TSM은 수익성 개선, 고객사(NVDA·AMD)는 마진 압박이라는 양방향 영향 주목.
- **연속성 (인텔 파운드리 반등)**: 2026-06-09 구글 TPU 수주 +11% → 2026-06-10 WF $110·바클레이즈 $100 추가 상향. 3주 연속 인텔 파운드리 이슈가 반도체 섹터 센티멘트 주요 변수. NVDA 18A 수주 여부가 다음 60일 핵심 모니터링.
- **역방향 (NVDA)**: 2026-06-09 +0.27 → 2026-06-10 +0.10 — Apple/Google 파트너십은 긍정적이나 TSMC 가격 인상 H2 마진 압박이 점수 하향 견인. 장기 성장 vs 단기 원가 상승 트레이드오프.
- **섹터 동기화 (WFE 슈퍼사이클)**: AMAT +0.29 / ASML +0.29 / LRCX +0.13 — 장비 3사 모두 WFE 강세론 동반 강화. AMAT 30%+ 전망 상향이 ASML·LRCX 수주 사이클에 선행 시그널로 작동.
- **섹터 동기화 (AI 메모리 구조적 부족)**: MU +0.21 / AMAT WFE 30%+ — HBM 전량 매진과 $2,000억 증설이 메모리 WFE 수요 직결. 6/24 MU 어닝이 반도체 섹터 다음 방향 분기점.
- **경고 (AVGO 여진)**: AVGO -0.02, 추가 -1.75% — 2주 전 -15% 충격 후 중립권 회복 중이나 SOX 셀오프 촉발 책임으로 섹터 신뢰도 회복 지연. Q3 AI 가이던스 상향 여부(8월)가 최후 판단 시점.
- **경고 (ARK/내부자 매도)**: AMD -4.74%, ARK $3,900만 + 내부자 $1.2억 — 6개월 2배 급등 후 기관 차익실현 가속. 섹터 전반 고점 경계 시그널.
- **주목 이벤트**: 6/17 LRCX 배당 권리락, 6/24 MU Q3 FY2026 어닝(GS $900 / Cantor $1,500 목표), 6/24 QCOM 인베스터 데이 Dragonfly 세부 발표, NVDA 18A 평가 결과 (60일 대기).

### 감지된 패턴 (2026-06-09 · 화요일 · 반도체)

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

### 감지된 패턴 (2026-06-13 · 토요일 · 금융 + 부동산 (REITs))

## 오늘의 시그널 (2026-06-13 · 토요일 · 금융 + 부동산 (REITs))

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장 (예: 비만치료제 임상 데이터 연속)
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈 (예: 관세, FOMC, 유가, 비만치료제, 데이터센터 전력) 로 동시 움직임

**2026-06-13 감지된 시그널:**

- **최고 시그널 (GS +0.32)**: 스페이스X 미국 최대 IPO 주관 + 앤트로픽 IPO 공동 주관 + 목표주가 $900 상향 삼중 호재. IPO 파이프라인 역사적 집중 — IB 수수료 창출이 최대 사이클에 진입했음을 신호.
- **최고 시그널 (V +0.34)**: FQ2 매출 +17% (13년 최고) + OpenAI 결제 통합 + 스테이블코인 파일럿 삼중 동시 발사. 비자가 AI 에이전트 결제, 스테이블코인, 전통 거래량 세 분야에서 동시에 선점 포지션 확보.
- **섹터 동기화 (AI IPO 수수료 물결)**: GS +0.32 / MS +0.21 / JPM 참여 — 스페이스X·앤트로픽 두 대형 AI IPO가 동시에 파이프라인에 진입. IB 섹터 역사적 수수료 집중이 대형 은행 전반 어닝 서프라이즈 기대 상승.
- **섹터 동기화 (AI 결제 인프라)**: V +0.34 / MA +0.17 / C +0.25 — 비자(OpenAI 통합), 마스터카드(Agent Pay), 씨티(블록체인 플랫폼)가 동시에 AI 시대 금융 인프라 포지셔닝 발표. 디지털 금융 전환의 가속화.
- **역방향 (GS 탐욕 경고 vs 실적)**: 솔로몬 CEO '투자자 탐욕 모드' 경고를 하면서도 동시에 스페이스X·앤트로픽 IPO를 주관 — '경고를 발하는 주관사' 아이러니. AI IPO 사이클 후반부 도달 가능성 경계.
- **모순 (MA)**: 2026-06-06 -0.03 → 2026-06-13 +0.17 — 교환수수료 합의 예비 승인 + Agent Pay 출시가 CFO 교체 불안을 완전 역전. 규제 불확실성 해소가 회복 동력.
- **연속성 (DOJ 디뱅킹 규제)**: JPM·BAC·WFC 동시 소환장 → 금융 섹터 전반 규제 리스크 테마 2주 연속 지속. 법무부 규제 조사 결과가 은행 섹터 다음 방향 분기점.
- **섹터 동기화 (데이터센터 REIT AI 수요)**: EQIX +0.30 / CCI +0.20 / DLR +0.12 — AI 인프라 수요가 인터커넥션(EQIX), 타워(CCI), 하이퍼스케일(DLR) 전 분야로 파급. EQIX AI Fabric 3배 성장이 섹터 선행 시그널.
- **섹터 동기화 (REIT M&A 물결)**: PSA(NSA 결합)·VICI(캐나다 카지노 + One Beverly Hills)·PLD(BTS 데이터센터) — REITs 섹터 M&A·포트폴리오 확장 동시 가속화.
- **경고 (AXP 소비자 신용)**: 연체율 13% (15년 최고) — AXP 단독이 아닌 소비자 신용 전반의 경고 시그널. Q2 실적 발표(7월) 때 대손충당금 증가 여부가 금융 섹터 하방 리스크 가늠자.
- **주목 이벤트**: GS·MS·JPM Anthropic IPO 실행 일정(미정), V FQ3 실적(10월 예정), AXP Q2 실적 대손충당금(7월), EQIX Q2 실적(7/29) AI Fabric 예약 지속성, CCI AFFO 실현 여부(Q2), PSA·NSA 딜 FTC 심사 결과.

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
