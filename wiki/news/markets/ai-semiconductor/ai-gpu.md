---
title: "AI 가속기 (GPU) — 시장 종합"
created: 2026-07-06
updated: 2026-07-06
domain: finance
type: claim
weight: reference
confidence: low
tags: [routine-news, market-summary, ai-semiconductor, ai-gpu]
map: ai-semiconductor
market_id: ai-gpu
sources: ["https://www.bloomberg.com/company/press/ai-accelerator-market-looks-set-to-exceed-600-billion-by-2033-driven-by-hyperscale-spending-and-asic-adoption-according-to-bloomberg-intelligence/"]
---

# AI 가속기 (GPU) — 시장 종합

**AI Accelerators / Data-Center GPU** · ③ AI 컴퓨팅 · 규모 $170–200B (’25) → $370–600B (’30+) · 성장 ~16% CAGR

> [!info] 자동 종합 노트
> 이 파일은 시장지도 노드 `ai-gpu` 의 종합 페이지다. `indicator_dashboard` 루틴이 관리한다 —
> **daily-market-analysis** 루틴이 담당 요일에 [소속 기업 동향]을, **market-research** 루틴이 주 1회
> [시장 정의]·[병목 상태]·[시장 상황 종합]·[시장 뉴스 로그]를 갱신한다. HTML 마커는 루틴의 앵커이므로 지우지 않는다.
> 사람은 굳어진 사실을 `wiki/topics/` 로 승격(promote)만 한다.

## 시장 정의

AI 학습·추론을 돌리는 데이터센터 GPU — 프런티어 AI의 지배적 연산 기판.

**수요 동인** — 프런티어 학습(연산 5배/년) + 추론 폭발. 전체 AI 연산 용량 ~7개월마다 2배.

## 병목 상태 — 🟠 병목 완화중 (`easing`)

> [!claim] (출처: 시장지도 as_of 2026-06)
> 칩 설계가 아니라 상류(CoWoS·HBM)와 하류(전력)가 제약. NVDA 자체는 공급 제약 상태 — 수요가 한계가 아님.

## 시장 상황 종합

<!-- SYNTHESIS_START -->
> [!claim] (as_of 2026-06 · market-research 루틴)
> Blackwell→Rubin 전환기, 수요는 공급 초과 지속. 커스텀 ASIC이 점유율을 80%대로 잠식 중.
<!-- SYNTHESIS_END -->

## 소속 기업 동향

<!-- PLAYERS_START -->
| 기업 | 역할 | 최근 시그널 | 핵심 한 줄 | 로그 |
|---|---|---|---|---|
| NVIDIA | GPU 출하 ~90% · 가속기 매출 80–85% · 점유 85% | +0.38 (2026-06-30) | Palantir 정부 AI·RTX Spark·Vera Rubin 풀생산, 단 5월 고점 대비 -23% | [NVDA](../../tickers/NVDA - NVIDIA Corporation.md) |
| AMD | ~5–8% (MI350/MI400) · 점유 8% | +0.52 (2026-06-30) | 데이터센터 +57%·Gartner 최강자·Rackspace 30MW, 중국 규제 리스크 | [AMD](../../tickers/AMD - Advanced Micro Devices.md) |
| Intel | <1% (Gaudi) · 점유 1% | +0.43 (2026-06-30) | Cantor $150(+67%)·18A-P 리스크생산·TSMC 인상 반사이익, +7.2% | [INTC](../../tickers/INTC - Intel Corporation.md) |
<!-- PLAYERS_END -->

## 시장 뉴스 로그 (최신순)

<!-- MARKET_NEWS_START -->
_아직 수집된 시장 단위 뉴스가 없다 — market-research 루틴이 채운다._
<!-- MARKET_NEWS_END -->

## 사실 누적 (Verified Facts)

<!-- FACTS_START -->
<!-- FACTS_END -->

## 관련 위키

- [NVIDIA](../../../entities/nvidia.md)
- [CUDA — 소프트웨어 해자](../../../concepts/cuda.md)
- [반도체·AI 칩 가치사슬 종합 — 내 판단](../../../syntheses/semiconductor-ai-chip-value-chain.md)
