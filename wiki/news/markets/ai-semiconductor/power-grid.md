---
title: "전력 생산·전력망 — 시장 종합"
created: 2026-07-06
updated: 2026-07-06
domain: finance
type: claim
weight: reference
confidence: low
tags: [routine-news, market-summary, ai-semiconductor, power-grid]
map: ai-semiconductor
market_id: power-grid
sources: ["https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary"]
---

# 전력 생산·전력망 — 시장 종합

**Power Generation & Grid** · ⑥ 장비·소재·전력 · 규모 DC 전력 ~485 TWh(’25) → ~950 TWh(’30) · 성장 ~2배 (AI는 3배)

> [!info] 자동 종합 노트
> 이 파일은 시장지도 노드 `power-grid` 의 종합 페이지다. `indicator_dashboard` 루틴이 관리한다 —
> **daily-market-analysis** 루틴이 담당 요일에 [소속 기업 동향]을, **market-research** 루틴이 주 1회
> [시장 정의]·[병목 상태]·[시장 상황 종합]·[시장 뉴스 로그]를 갱신한다. HTML 마커는 루틴의 앵커이므로 지우지 않는다.
> 사람은 굳어진 사실을 `wiki/topics/` 로 승격(promote)만 한다.

## 시장 정의

AI 데이터센터에 전기를 공급하는 발전·전력계약·전력망 접속.

**수요 동인** — AI 학습/추론 + GW급 단일 캠퍼스. ~$700B(’26) AI 투자가 전력으로 귀결.

## 병목 상태 — 🔴 급성 병목 (`acute`)

> [!claim] (출처: 시장지도 as_of 2026-06)
> 현재 가장 단단한 단기 병목으로 널리 지목 — 전력망 접속 대기 다년치, 발전 용량, 가스터빈 리드타임(2028–30까지 예약). 원자력/SMR은 ~2029 전 순증 불가. IEA도 공급망/전력망 제약이 공격적 시나리오를 제한한다 명시.

## 시장 상황 종합

<!-- SYNTHESIS_START -->
> [!claim] (as_of 2026-06 · market-research 루틴)
> DC 전력 ’30까지 2~3배, 전력망 접속 대기·가스터빈 리드타임이 최대 단기 병목.
<!-- SYNTHESIS_END -->

## 소속 기업 동향

<!-- PLAYERS_START -->
| 기업 | 역할 | 최근 시그널 | 핵심 한 줄 | 로그 |
|---|---|---|---|---|
| Constellation | 미 최대 원자력 (MS TMI 재가동) | +0.19 (2026-07-03) | 원전 증설·MS 스리마일 PPA·Calpine Q1 비트 vs PJM 가격상한 오버행으로 YTD -20% | [CEG](../../tickers/CEG - Constellation Energy.md) |
| Vistra | 원자력+가스 | +0.18 (2026-07-03) | Q1 +43%·Fitch IG·Meta/AWS 3,800MW PPA vs PJM 가격상한·내부자 매도로 6일 -12% | [VST](../../tickers/VST - Vistra Corp.md) |
| NextEra | 신재생 1위 (Dominion 딜) | +0.15 (2026-07-03) | $67B 도미니언 인수로 세계 최대 규제 유틸리티·130GW AI 파이프라인 vs 버지니아 SCC·의회 검토 | [NEE](../../tickers/NEE - NextEra Energy.md) |
| GE Vernova | 가스터빈 (2030까지 예약) + SMR | watchlist 외 | — | `GEV` |
| Talen | Susquehanna/AWS PPA | watchlist 외 | — | `TLN` |
<!-- PLAYERS_END -->

## 시장 뉴스 로그 (최신순)

<!-- MARKET_NEWS_START -->
- **2026-05** － **변압기 리드타임 4–5년으로 — 미국 신규 DC 50%+ 지연** — 전기장비는 원가 <10%인데 병목의 ~100%. GOES 강·동박 공급이 관건. (pv-magazine) [↗](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/)
- **2026-04** － **IEA: AI 데이터센터 전력수요 2030년까지 3배** — DC 전력 485→950 TWh 전망. 전력망·공급망 제약이 더 공격적 시나리오를 가로막음. (IEA) [↗](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary)
<!-- MARKET_NEWS_END -->

## 사실 누적 (Verified Facts)

<!-- FACTS_START -->
<!-- FACTS_END -->

## 관련 위키

- [AI 데이터센터 전력 인프라 — 내 판단](../../../syntheses/ai-datacenter-power-infrastructure.md)
- [GE Vernova](../../../entities/ge-vernova.md)
- [Bloom Energy](../../../entities/bloom-energy.md)
- [LS일렉트릭](../../../entities/ls-electric.md)
- [두산에너빌리티](../../../entities/doosan-enerbility.md)
