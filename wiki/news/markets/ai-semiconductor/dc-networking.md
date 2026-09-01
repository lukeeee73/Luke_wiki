---
title: "데이터센터 네트워킹 — 시장 종합"
created: 2026-07-06
updated: 2026-09-01
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
| NVIDIA | NVLink 스케일업 준독점 + Spectrum-X · 점유 40% | 🟢🟢 +0.21 (2026-09-01) | 2분기 실적이 기대를 크게 웃돌았지만 메모리 원가 부담과 미디어텍 투자 논란으로 주가는 하루 만에 일부 되돌렸다 | [NVDA](../../tickers/NVDA - NVIDIA Corporation.md) |
| Broadcom | 머천트 스위치 실리콘(Tomahawk) | 🟢 +0.06 (2026-09-01) | 내일 실적 발표를 앞두고 기대감은 있지만 경쟁사의 대형 수주 소식에 다소 눌렸다 | [AVGO](../../tickers/AVGO - Broadcom Inc.md) |
| Arista | DC 이더넷 ~19% · 점유 20% | 🟢🟢 +0.39 (2026-08-31) | 엔비디아의 어닝 서프라이즈로 AI 인프라 투자심리가 개선되며 주가가 함께 올랐고, 기관투자자의 신규 지분 매수 공시까지 겹쳤다 | [ANET](../../tickers/ANET - Arista Networks, Inc.md) |
| Cisco | 기존 강자, AI 점유율 하락 · 점유 15% | watchlist 외 | — | `CSCO` |
| Marvell | DPU·커스텀 실리콘 | 🟢 +0.14 (2026-09-01) | 매출이 사상 최대를 기록하고 전망도 올렸는데도 주가는 오히려 크게 빠지는 이례적인 하루였다 | [MRVL](../../tickers/MRVL - Marvell Technology, Inc.md) |
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
