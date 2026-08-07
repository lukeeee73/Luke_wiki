---
title: "그리드 접속 · 유틸리티 조달 (FTM) — 시장 종합"
created: 2026-07-06
updated: 2026-07-31
domain: finance
type: claim
weight: reference
confidence: low
tags: [routine-news, market-summary, power-ai, grid-ftm]
map: power-ai
market_id: grid-ftm
sources: ["https://www.latitudemedia.com/news/ercots-large-load-queue-has-nearly-quadrupled-in-a-single-year/", "https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access", "https://www.whitecase.com/insight-alert/pjm-proposes-carve-out-new-services-co-located-data-centers"]
---

# 그리드 접속 · 유틸리티 조달 (FTM) — 시장 종합

**Grid / Front-of-the-Meter Procurement** · ② 조달 경로 · 규모 ERCOT 대형부하 큐 410GW(87%가 DC) · PJM ’30까지 대형부하 +55GW 전망 · 성장 대기열 폭증 — ERCOT 1Q26 신규 신청 198GW

> [!info] 자동 종합 노트
> 이 파일은 시장지도 노드 `grid-ftm` 의 종합 페이지다. `indicator_dashboard` 루틴이 관리한다 —
> **daily-market-analysis** 루틴이 담당 요일(금 — 유틸리티/전력 · 전력 인프라(AI) 그룹)에 [소속 기업 동향]을,
> **market-research** 루틴이 주 1회 [시장 정의]·[병목 상태]·[시장 상황 종합]·[시장 뉴스 로그]를 갱신한다.
> HTML 마커는 루틴의 앵커이므로 지우지 않는다. 사람은 굳어진 사실을 `wiki/topics/` 로 승격(promote)만 한다.

## 시장 정의

전통 경로 — 계통 접속 + 유틸리티 요금·장기 PPA 로 전력을 확보. 규모·신뢰도는 최고, 속도는 최악.

**수요 동인** — 500MW+ 급 캠퍼스는 결국 계통이 필요. 유틸리티는 large-load tariff(대형부하 요금제)로 리스크를 배분하며 수요를 선별 수용.

## 병목 상태 — 🔴 급성 병목 (`acute`)

> [!claim] (출처: 시장지도 as_of 2026-07)
> 계통접속 대기 전국 평균 ~25개월, 핫스팟 36–48개월(PJM ~40개월). PJM 용량 부족 ’30까지 15GW 전망 — 용량경매 $16.4B 사상최대로 요금 전가 논쟁 격화. FERC·PJM 이 공동입지(colocation) 규칙 제정 중.

## 시장 상황 종합

<!-- SYNTHESIS_START -->
> [!claim] (as_of 2026-07 · market-research 루틴)
> **지금 상황**: PJM 2028/29 용량경매가 또다시 가격상한($325/MW-day)에 도달 — 예비율 목표 대비 6.8GW 부족. ERCOT는 7/11부로 기존 개별심사 대기열 절차를 'Batch Zero' 시스템으로 전면 교체.
> **왜 중요**: 2년 연속 가격상한 도달은 신규 발전이 수요 증가를 구조적으로 못 따라가고 있다는 뜻이다.
> **투자자 관점**: 용량가격 상승은 기존 발전자산 보유자에게 유리하게 작용하고, 절차 개편(Batch Zero)이 실제 대기열 해소로 이어지는지가 다음 관전포인트다.
<!-- SYNTHESIS_END -->

## 소속 기업 동향

<!-- PLAYERS_START -->
| 기업 | 역할 | 최근 시그널 | 핵심 한 줄 | 로그 |
|---|---|---|---|---|
| Dominion | 버지니아 — 세계 최대 DC 클러스터 유틸리티 | -0.04 (2026-07-31) | 2분기 실적 발표, NEE 합병은 순항하나 버지니아 SCC 첫 공청회가 11월로 확정 | [D](../../tickers/D - Dominion Energy.md) |
| AEP | 765kV 송전 최대 — 오하이오 DC 벨트 | +0.12 (2026-07-31) | 2분기 EPS는 예상 밑돌았지만 가이던스 상향, 2030년까지 계약부하 69GW로 확대 | [AEP](../../tickers/AEP - American Electric Power.md) |
| Exelon | 송배전 전문 — 시카고·필라델피아·볼티모어 | -0.13 (2026-07-31) | 2분기 EPS가 예상을 밑돌면서 주가가 4.5% 급락, 연간 가이던스는 그대로 유지 | [EXC](../../tickers/EXC - Exelon Corporation.md) |
| Duke Energy | 동남부 — 캐롤라이나 DC 유치 | +0.10 (2026-07-31) | 캐롤라이나에 대형 신규 가스발전 프로젝트를 제안했고, 폭풍으로 인한 정전을 복구했다 | [DUK](../../tickers/DUK - Duke Energy Corporation.md) |
| Southern | 조지아 — 애틀랜타 DC 급증 대응 | +0.15 (2026-07-31) | 2분기 실적이 예상을 크게 웃돌아 연간 이익 전망을 상단으로 올렸다 | [SO](../../tickers/SO - The Southern Company.md) |
| NRG Energy | 텍사스 IPP — GEV·부동산과 DC 전력 합작 | watchlist 외 | — | `NRG` |
<!-- PLAYERS_END -->

## 시장 뉴스 로그 (최신순)

<!-- MARKET_NEWS_START -->
- **2026-07** － **PJM 용량경매 또 상한가 도달 — 예비율 6.8GW 부족 확인** — 2년 연속 가격상한 — 신규 발전이 수요 증가를 못 따라감 (Utility Dive) [↗](https://www.utilitydive.com/news/pjm-capacity-auction-price-cap-reserve-shortfall/825282/)
- **2026-07-11** ± **ERCOT, 대형부하 접속 절차를 'Batch Zero'로 전면 개편·시행** — 개별심사 대신 시스템 전체 일괄평가로 큐 절차 정비 (Willkie Farr) [↗](https://www.willkie.com/publications/2026/06/ercot-approves-implementing-new-batch-zero-process-for-large-load-interconnections)
- **2026-04** － **ERCOT 대형부하 큐 410GW — 1년새 4배, 87%가 데이터센터** — 1Q26 신규 신청만 198GW — 접속 대기열이 곧 시장 (Latitude Media / ERCOT) [↗](https://www.latitudemedia.com/news/ercots-large-load-queue-has-nearly-quadrupled-in-a-single-year/)
- **2026-03** ± **FERC, PJM 에 데이터센터 공동입지(colocation) 규칙 제정 명령** — 원전 옆 DC 직결 규칙 정비 — 그리드 조달의 게임 룰 재편 (Utility Dive / White & Case) [↗](https://www.whitecase.com/insight-alert/pjm-proposes-carve-out-new-services-co-located-data-centers)
- **2026-02** － **PJM 핫스팟 접속 대기 36~48개월 — 용량부족 ’30까지 15GW** — 계약 103GW 중 23GW 만 가동 — 실물(장비·인력)이 병목 (Carbon Direct / Ascend Analytics) [↗](https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access)
<!-- MARKET_NEWS_END -->

## 사실 누적 (Verified Facts)

<!-- FACTS_START -->
<!-- FACTS_END -->

## 인접 시장 (지도 링크)

- ⬅ 수요측 [AI 데이터센터 전력 수요](ai-dc-demand.md) — 계통 접속 + 유틸리티·PPA
- ➡ 공급측 [가스 발전 (신설 CCGT·온사이트)](gas-power.md) — 계통용 CCGT 신설
- ➡ 공급측 [기존 원전 (재가동·업레이트·PPA)](nuclear-existing.md) — 24/7 무탄소 장기 PPA
- ➡ 공급측 [재생에너지 + ESS](renewables-storage.md) — 재생 PPA (24/7 매칭)
- ➡ 공급측 [송전망 · 계통 인프라 건설](transmission.md) — 계통접속·변전 공사

## 관련 위키

- [AI 데이터센터 전력 인프라 — 내 판단](../../../wiki/syntheses/ai-datacenter-power-infrastructure.md)
- [전력 생산·전력망 (AI·반도체 지도 자매 노드)](../ai-semiconductor/power-grid.md)
