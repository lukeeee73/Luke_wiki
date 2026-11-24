---
title: "데이터센터 네트워킹 — 시장 종합"
created: 2026-07-06
updated: 2026-11-24
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
| NVIDIA | NVLink 스케일업 준독점 + Spectrum-X · 점유 40% | 🟢 +0.12 (2026-11-24) | 리더십 공백 속에서도 3분기 매출이 103% 급증하며 서프라이즈를 냈고, 이사회는 젠슨 황의 복귀는 없다고 공식 확인했다. | [NVDA](../../tickers/NVDA - NVIDIA Corporation.md) |
| Broadcom | 머천트 스위치 실리콘(Tomahawk) | 🟢 +0.08 (2026-11-24) | 반도체 업종 전반의 매도세에서 벗어나 AI 인프라 수요가 재확인됐지만 밸류에이션 부담은 여전하다. | [AVGO](../../tickers/AVGO - Broadcom Inc.md) |
| Arista | DC 이더넷 ~19% · 점유 20% | 🟢 +0.16 (2026-11-23) | 3분기 깜짝실적 이후에도 AI 인프라주 전반의 급등락에 동반되며 출렁였고, 성장 모멘텀 둔화 우려도 제기됐다 | [ANET](../../tickers/ANET - Arista Networks, Inc.md) |
| Cisco | 기존 강자, AI 점유율 하락 · 점유 15% | watchlist 외 | — | `CSCO` |
| Marvell | DPU·커스텀 실리콘 | ⚪ -0.01 (2026-11-24) | 12/1 실적 발표를 앞둔 공백기에 업종 셀오프로 주가가 떨어졌지만 신규 이사 선임 등 거버넌스 보강이 있었다. | [MRVL](../../tickers/MRVL - Marvell Technology, Inc.md) |
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
