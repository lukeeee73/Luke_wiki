---
title: "데이터센터 네트워킹 — 시장 종합"
created: 2026-07-06
updated: 2026-09-08
domain: finance
type: claim
weight: reference
confidence: low
tags: [routine-news, market-summary, ai-semiconductor, dc-networking]
map: ai-semiconductor
market_id: dc-networking
sources: ["https://www.delloro.com/news/data-center-switch-sales-in-ai-back-end-networks-to-exceed-100-b-over-the-next-five-years/"]
---

# 데이터센터 네트워킹 — 시장 종합

**AI Data-Center Networking** · ③ AI 컴퓨팅 · 규모 백엔드 스위치 ~$10–13B (’25) · 5년 누적 >$100B · 성장 ~24% CAGR

> [!info] 자동 종합 노트
> 이 파일은 시장지도 노드 `dc-networking` 의 종합 페이지다. `indicator_dashboard` 루틴이 관리한다 —
> **daily-market-analysis** 루틴이 담당 요일에 [소속 기업 동향]을, **market-research** 루틴이 주 1회
> [시장 정의]·[병목 상태]·[시장 상황 종합]·[시장 뉴스 로그]를 갱신한다. HTML 마커는 루틴의 앵커이므로 지우지 않는다.
> 사람은 굳어진 사실을 `wiki/topics/` 로 승격(promote)만 한다.

## 시장 정의

GPU를 잇는 스위치 패브릭 — 스케일업(NVLink)과 스케일아웃(InfiniBand vs Ethernet).

**수요 동인** — GPU 클러스터 규모 확대(1만→10만→100만+). GPU마다 전용 고대역 포트 필요. 대역폭이 FLOPs와 함께 증가.

## 병목 상태 — 🟡 부상하는 병목 (`emerging`)

> [!claim] (출처: 시장지도 as_of 2026-06)
> 표준 전쟁(NVLink 독점 vs UALink vs Scale-Up Ethernet)이 마찰. 구리 도달거리가 랙 밖에서 한계 → 병목이 광(아래)으로 이동.

## 시장 상황 종합

<!-- SYNTHESIS_START -->
> [!claim] (as_of 2026-06 · market-research 루틴)
> 스케일업 표준 전쟁(NVLink vs UALink vs Ethernet) 격화. 이더넷이 InfiniBand를 추월.
<!-- SYNTHESIS_END -->

## 소속 기업 동향

<!-- PLAYERS_START -->
| 기업 | 역할 | 최근 시그널 | 핵심 한 줄 | 로그 |
|---|---|---|---|---|
| NVIDIA | NVLink 스케일업 준독점 + Spectrum-X · 점유 40% | 🟢 +0.17 (2026-09-08) | 엔비디아가 오픈소스 AI 플랫폼 허깅페이스를 13조원 규모에 인수하며 주가가 사상 최고치에 다가섰다. | [NVDA](../../tickers/NVDA - NVIDIA Corporation.md) |
| Broadcom | 머천트 스위치 실리콘(Tomahawk) | 🟢 +0.16 (2026-09-08) | 브로드컴이 인공지능 반도체 매출이 두 배 넘게 늘어난 실적을 발표했지만 이미 높았던 기대치 탓에 주가 반응은 차분했다. | [AVGO](../../tickers/AVGO - Broadcom Inc.md) |
| Arista | DC 이더넷 ~19% · 점유 20% | 🟢🟢 +0.39 (2026-09-07) | 도이체방크가 매수 커버리지를 새로 개시했고 9월21일 S&P100 지수 편입도 확정되며 견조한 흐름을 이어갔다 | [ANET](../../tickers/ANET - Arista Networks, Inc.md) |
| Cisco | 기존 강자, AI 점유율 하락 · 점유 15% | watchlist 외 | — | `CSCO` |
| Marvell | DPU·커스텀 실리콘 | ⚪ +0.05 (2026-09-08) | 마벨 주가가 실적 발표 후 급락했던 흐름에서 벗어나 반등했고 다음 달 투자자의 날이 다음 관전 포인트로 떠올랐다. | [MRVL](../../tickers/MRVL - Marvell Technology, Inc.md) |
<!-- PLAYERS_END -->

## 시장 뉴스 로그 (최신순)

<!-- MARKET_NEWS_START -->
_아직 수집된 시장 단위 뉴스가 없다 — market-research 루틴이 채운다._
<!-- MARKET_NEWS_END -->

## 사실 누적 (Verified Facts)

<!-- FACTS_START -->
<!-- FACTS_END -->

## 관련 위키

- [SerDes](../../../concepts/serdes.md)
- [Broadcom](../../../entities/broadcom.md)
