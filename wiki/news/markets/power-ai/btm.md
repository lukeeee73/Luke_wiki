---
title: "BTM 구내·전용 발전 조달 — 시장 종합"
created: 2026-07-06
updated: 2026-07-06
domain: finance
type: claim
weight: reference
confidence: low
tags: [routine-news, market-summary, power-ai, btm]
map: power-ai
market_id: btm
sources: ["https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw", "https://www.naturalgasintel.com/news/data-centers-going-off-grid-with-natural-gas-to-find-any-way-to-get-power/", "https://heatmap.news/energy/natural-gas-data-centers-speed"]
---

# BTM 구내·전용 발전 조달 — 시장 종합

**Behind-the-Meter / On-site Power** · ② 조달 경로 · 규모 ’28 BTM 40GW+ 전망(SemiAnalysis) · 신규 증분의 25–33%(McKinsey) · 장비 TAM ~50GW/yr(’29) · 성장 ’28+ 신규 DC 의 절반 이상 전망

> [!info] 자동 종합 노트
> 이 파일은 시장지도 노드 `btm` 의 종합 페이지다. `indicator_dashboard` 루틴이 관리한다 —
> **daily-market-analysis** 루틴이 담당 요일(금 — 유틸리티/전력 · 전력 인프라(AI) 그룹)에 [소속 기업 동향]을,
> **market-research** 루틴이 주 1회 [시장 정의]·[병목 상태]·[시장 상황 종합]·[시장 뉴스 로그]를 갱신한다.
> HTML 마커는 루틴의 앵커이므로 지우지 않는다. 사람은 굳어진 사실을 `wiki/topics/` 로 승격(promote)만 한다.

## 시장 정의

계통(그리드)을 우회해 DC 부지 안·옆에 전용 발전(가스터빈·연료전지·향후 SMR)을 두는 조달 경로. 속도가 무기.

**수요 동인** — 계통접속 3~5년 vs BTM 가스 ~18개월. xAI Colossus(VoltaGrid 가스발전기)가 원형 — 이후 하이퍼스케일러·네오클라우드의 기본 옵션으로 확산.

## 병목 상태 — 🟡 부상하는 병목 (`emerging`)

> [!claim] (출처: 시장지도 as_of 2026-07)
> 속도의 대가 — 터빈·왕복엔진 리드타임(’29 매진), 대기오염 인허가(가스 연소), 부지 가스 공급 인프라가 제약. 소비자 요금 전가 논쟁과 규제 리스크도 부상.

## 시장 상황 종합

<!-- SYNTHESIS_START -->
> [!claim] (as_of 2026-07 · market-research 루틴)
> BTM 이 '예외'에서 '기본 옵션'으로 — ’28+ 신규 DC 절반 이상이 BTM 전망. 미드스트림·연료전지 업체가 직접 전력 공급자로 변신 중.
<!-- SYNTHESIS_END -->

## 소속 기업 동향

<!-- PLAYERS_START -->
| 기업 | 역할 | 최근 시그널 | 핵심 한 줄 | 로그 |
|---|---|---|---|---|
| VoltaGrid | 모듈러 가스발전 — xAI Colossus 전력 (비상장) | — | — | 비상장 |
| Crusoe | 수직통합 DC+발전 개발 — 와이오밍 1.8GW급 (비상장) | — | — | 비상장 |
| Williams | 미드스트림→온사이트 발전 진출 ($5.1B power innovation) | watchlist 외 | — | `WMB` |
| Energy Transfer | CloudBurst DC 에 가스 직공급 (~1.2GW) | watchlist 외 | — | `ET` |
| Bloom Energy | 연료전지 BTM — Oracle·Equinix | — (수집 전) | 신규 편입 — 첫 뉴스 수집 대기 | `BE` |
| ProEnergy | 항공파생 터빈 피커 — BTM 브리지 전력 (비상장) | — | — | 비상장 |
<!-- PLAYERS_END -->

## 시장 뉴스 로그 (최신순)

<!-- MARKET_NEWS_START -->
- **2026-06** ± **BTM 가스발전, 소비자 요금 인상 논쟁으로 — 그래도 확산 지속** — BTM 붐이 가스 수요·요금에 파급 — 규제 리스크 부상 (Utility Dive) [↗](https://www.utilitydive.com/news/data-centers-raise-energy-bills-not-for-reason-you-think/822205/)
- **2026-05** ＋ **'속도-전력 문제, 천연가스로 풀었다' — BTM 이 기본 옵션으로** — 계통 3~5년 대기 vs BTM 가스 ~18개월 — 신규 DC 절반+가 BTM 전망 (Heatmap News) [↗](https://heatmap.news/energy/natural-gas-data-centers-speed)
- **2026-04** ＋ **미드스트림, DC 온사이트 발전 사업 직접 진출 가속** — Williams·ET 가 파이프+발전 결합 상품으로 BTM 공급자化 (NGI / Enverus) [↗](https://www.naturalgasintel.com/news/data-centers-going-off-grid-with-natural-gas-to-find-any-way-to-get-power/)
<!-- MARKET_NEWS_END -->

## 사실 누적 (Verified Facts)

<!-- FACTS_START -->
<!-- FACTS_END -->

## 인접 시장 (지도 링크)

- ⬅ 수요측 [AI 데이터센터 전력 수요](ai-dc-demand.md) — 속도 우선 — 구내 전용 발전
- ➡ 공급측 [가스 발전 (신설 CCGT·온사이트)](gas-power.md) — 온사이트 가스 (~18개월)
- ➡ 공급측 [연료전지 온사이트 발전](fuel-cells.md) — 무연소 인허가 — 터빈 대체
- ➡ 공급측 [SMR · 차세대 원자로](smr.md) — 차세대 온사이트 (’30±)
- ➡ 공급측 [재생에너지 + ESS](renewables-storage.md) — 온사이트 태양광+ESS 보조
- ➡ 공급측 [변압기 · 스위치기어 · HVDC](transformers.md) — 구내 변전 장비

## 관련 위키

- [AI 데이터센터 전력 인프라 — 내 판단](../../../syntheses/ai-datacenter-power-infrastructure.md)
- [Bloom Energy](../../../entities/bloom-energy.md)
- [전력 생산·전력망 (AI·반도체 지도 자매 노드)](../ai-semiconductor/power-grid.md)
