---
title: "전력공급·냉각 장비 — 시장 종합"
created: 2026-07-06
updated: 2026-07-06
domain: finance
type: claim
weight: reference
confidence: low
tags: [routine-news, market-summary, ai-semiconductor, power-cooling]
map: ai-semiconductor
market_id: power-cooling
sources: ["https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/"]
---

# 전력공급·냉각 장비 — 시장 종합

**Power Delivery & Cooling** · ④ 핵심 부품 (병목) · 규모 액침냉각 ~$6B(’25)→$19–29B(’30) · 성장 냉각 ~20%+ CAGR

> [!info] 자동 종합 노트
> 이 파일은 시장지도 노드 `power-cooling` 의 종합 페이지다. `indicator_dashboard` 루틴이 관리한다 —
> **daily-market-analysis** 루틴이 담당 요일에 [소속 기업 동향]을, **market-research** 루틴이 주 1회
> [시장 정의]·[병목 상태]·[시장 상황 종합]·[시장 뉴스 로그]를 갱신한다. HTML 마커는 루틴의 앵커이므로 지우지 않는다.
> 사람은 굳어진 사실을 `wiki/topics/` 로 승격(promote)만 한다.

## 시장 정의

전력을 칩까지 변환·분배하고 열을 제거하는 장비 — 변압기·스위치기어·PMIC·액침냉각.

**수요 동인** — 랙 밀도 급증(GPU >1kW, 랙 100kW→MW급) → 액침냉각·800VDC/HVDC 전환(Rubin 세대).

## 병목 상태 — 🔴 급성 병목 (`acute`)

> [!claim] (출처: 시장지도 as_of 2026-06)
> 전기 장비측이 가장 타이트한 단기 병목 중 하나. 변압기 리드타임 ~4–5년(2020 전 2~2.5년). '전기장비는 원가 <10%인데 병목의 ~100%'. 미국 신규 DC 50%+가 장비 부족으로 지연/취소(~7GW).

## 시장 상황 종합

<!-- SYNTHESIS_START -->
> [!claim] (as_of 2026-06 · market-research 루틴)
> 변압기 리드타임 4–5년으로 미국 DC 50%+ 지연. 800VDC·액침냉각 전환 가속.
<!-- SYNTHESIS_END -->

## 소속 기업 동향

<!-- PLAYERS_START -->
| 기업 | 역할 | 최근 시그널 | 핵심 한 줄 | 로그 |
|---|---|---|---|---|
| Vertiv | 전력+액침냉각 (NVIDIA GB200 레퍼런스) · 점유 22% | watchlist 외 | — | `VRT` |
| Eaton | 변압기·스위치기어·PDU · 점유 12% | watchlist 외 | — | `ETN` |
| Monolithic Power | 고밀도 GPU 전력전달 'last inch' | — (수집 전) | 신규 편입 — 첫 뉴스 수집 대기 | [MPWR](../../tickers/MPWR - Monolithic Power Systems.md) |
| Navitas · Infineon · ON | GaN/SiC 800VDC | watchlist 외 | — | `NVTS` |
| Schneider Electric | 변압기·스위치기어 (해외) · 점유 12% | — | — | 비상장 |
<!-- PLAYERS_END -->

## 시장 뉴스 로그 (최신순)

<!-- MARKET_NEWS_START -->
_아직 수집된 시장 단위 뉴스가 없다 — market-research 루틴이 채운다._
<!-- MARKET_NEWS_END -->

## 사실 누적 (Verified Facts)

<!-- FACTS_START -->
<!-- FACTS_END -->

## 관련 위키

- [AI 데이터센터 전력 인프라 — 내 판단](../../../syntheses/ai-datacenter-power-infrastructure.md)
