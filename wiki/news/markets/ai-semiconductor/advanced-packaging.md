---
title: "첨단 패키징 (CoWoS·SoIC) — 시장 종합"
created: 2026-07-06
updated: 2026-07-06
domain: finance
type: claim
weight: reference
confidence: low
tags: [routine-news, market-summary, ai-semiconductor, advanced-packaging]
map: ai-semiconductor
market_id: advanced-packaging
sources: ["https://www.trendforce.com/news/2025/12/08/news-tsmcs-cowos-l-s-reportedly-fully-booked-osat-partners-step-up-with-ases-cowop-in-focus/"]
---

# 첨단 패키징 (CoWoS·SoIC) — 시장 종합

**Advanced Packaging (2.5D/3D)** · ④ 핵심 부품 (병목) · 규모 CoWoS 용량 35k→130k wpm (’24→’26, ~4배) · 성장 ~80% CAGR (용량)

> [!info] 자동 종합 노트
> 이 파일은 시장지도 노드 `advanced-packaging` 의 종합 페이지다. `indicator_dashboard` 루틴이 관리한다 —
> **daily-market-analysis** 루틴이 담당 요일에 [소속 기업 동향]을, **market-research** 루틴이 주 1회
> [시장 정의]·[병목 상태]·[시장 상황 종합]·[시장 뉴스 로그]를 갱신한다. HTML 마커는 루틴의 앵커이므로 지우지 않는다.
> 사람은 굳어진 사실을 `wiki/topics/` 로 승격(promote)만 한다.

## 시장 정의

GPU 로직 다이와 HBM 스택을 실리콘 인터포저 위에 통합 — 가속기를 물리적으로 완성하는 단계.

**수요 동인** — 모든 고급 가속기에 필수. GPU 물량 × HBM 스택수(증가) × 다이 크기(레티클 초과 → CoWoS-L).

## 병목 상태 — 🟠 병목 완화중 (`easing`)

> [!claim] (출처: 시장지도 as_of 2026-06)
> CoWoS-L/S ’26까지 매진이나 ~4배 증설로 급성 병목은 완화중 → 제약이 상류 HBM과 하류 전력으로 이동. 물리 한계: 레티클(~858mm²) → 멀티레티클 스티칭, 인터포저 워피지.

## 시장 상황 종합

<!-- SYNTHESIS_START -->
> [!claim] (as_of 2026-06 · market-research 루틴)
> CoWoS 4배 증설로 ’23–24 급성 병목은 완화, 병목이 HBM·전력으로 이동.
<!-- SYNTHESIS_END -->

## 소속 기업 동향

<!-- PLAYERS_START -->
| 기업 | 역할 | 최근 시그널 | 핵심 한 줄 | 로그 |
|---|---|---|---|---|
| TSMC | 지배 (CoWoS-L/S·SoIC) · NVDA가 60–63% 선점 · 점유 80% | +0.29 (2026-06-30) | 첨단노드 90% 점유·5~10% 인상·Winbond 협력, ITC 예비판정 리스크 | [TSM](../../tickers/TSM - Taiwan Semiconductor Mfg.md) |
| Amkor | 2차 CoWoS · 미국 증설 · 점유 5% | — (수집 전) | 신규 편입 — 첫 뉴스 수집 대기 | [AMKR](../../tickers/AMKR - Amkor Technology, Inc.md) |
| ASE | CoWoS + CoWoP 대안 · 점유 12% | watchlist 외 | — | `ASX` |
| Intel | EMIB/Foveros (오버플로 수주) · 점유 3% | +0.43 (2026-06-30) | Cantor $150(+67%)·18A-P 리스크생산·TSMC 인상 반사이익, +7.2% | [INTC](../../tickers/INTC - Intel Corporation.md) |
<!-- PLAYERS_END -->

## 시장 뉴스 로그 (최신순)

<!-- MARKET_NEWS_START -->
- **2025-12** · **TSMC CoWoS-L/S 2026까지 완판 — OSAT가 CoWoP로 보완** — ~4배 증설로 급성 CoWoS 병목은 완화 중, 제약이 HBM·전력으로 이동. (TrendForce) [↗](https://www.trendforce.com/news/2025/12/08/news-tsmcs-cowos-l-s-reportedly-fully-booked-osat-partners-step-up-with-ases-cowop-in-focus/)
<!-- MARKET_NEWS_END -->

## 사실 누적 (Verified Facts)

<!-- FACTS_START -->
<!-- FACTS_END -->

## 관련 위키

- [CoWoS — 첨단 패키징](../../../concepts/cowos.md)
- [TSMC](../../../entities/tsmc.md)
