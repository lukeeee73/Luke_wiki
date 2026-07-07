---
title: "AI 데이터센터 전력 수요 — 시장 종합"
created: 2026-07-06
updated: 2026-07-06
domain: finance
type: claim
weight: reference
confidence: low
tags: [routine-news, market-summary, power-ai, ai-dc-demand]
map: power-ai
market_id: ai-dc-demand
sources: ["https://www.goldmansachs.com/insights/articles/us-data-center-power-demand-projected-to-double-by-2027", "https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary"]
---

# AI 데이터센터 전력 수요 — 시장 종합

**AI Data Center Power Demand** · ① 최종 수요 · 규모 美 DC 31GW(’25)→41GW(’26)→~100GW(’30) · 글로벌 ~945TWh(’30, IEA) · 성장 미국 GW 기준 연 +30%대

> [!info] 자동 종합 노트
> 이 파일은 시장지도 노드 `ai-dc-demand` 의 종합 페이지다. `indicator_dashboard` 루틴이 관리한다 —
> **daily-market-analysis** 루틴이 담당 요일(금 — 유틸리티/전력 · 전력 인프라(AI) 그룹)에 [소속 기업 동향]을,
> **market-research** 루틴이 주 1회 [시장 정의]·[병목 상태]·[시장 상황 종합]·[시장 뉴스 로그]를 갱신한다.
> HTML 마커는 루틴의 앵커이므로 지우지 않는다. 사람은 굳어진 사실을 `wiki/topics/` 로 승격(promote)만 한다.

## 시장 정의

AI 학습·추론용 데이터센터의 전력 소비 — 이 지도의 모든 조달·발전·장비 수요의 근원.

**수요 동인** — 하이퍼스케일러 ’26 capex $700B±와 GW급 단일 캠퍼스(Stargate ~7GW 등). 칩 확보전이 일단락되며 전력이 AI 빌드아웃의 제1 제약으로.

## 병목 상태 — 병목 없음 (수요의 근원)

> [!claim] (출처: 시장지도 as_of 2026-07)
> 이 노드는 병목 표기가 없다 — 지도 전체 수요의 근원이며, 제약은 하류의 조달 경로(계통접속 대기열)와 장비(터빈·변압기) 노드에 나타난다.

## 시장 상황 종합

<!-- SYNTHESIS_START -->
> [!claim] (as_of 2026-07 · market-research 루틴)
> 전력 확보가 '컴퓨트 전쟁'의 본선으로 — 4대 하이퍼스케일러 전원이 원자력 계약 체결, 조달 무게추는 BTM 으로 이동 중.
<!-- SYNTHESIS_END -->

## 소속 기업 동향

<!-- PLAYERS_START -->
| 기업 | 역할 | 최근 시그널 | 핵심 한 줄 | 로그 |
|---|---|---|---|---|
| Microsoft | 원자력 PPA 선구 (TMI 재가동 835MW) | +0.14 (2026-06-29) | 셰브론과 20년 2.67GW 텍사스 AI DC 전력계약, FTC 반독점 조사·OpenAI 지출 분산 | [MSFT](../../tickers/MSFT - Microsoft Corporation.md) |
| Amazon | Talen 1,920MW + X-energy SMR 투자 | +0.31 (2026-06-29) | AWS GPU 예약가 ~20% 인상·프라임데이 매출 +9.3%, AI 모멘텀 시총 $3T 기대 | [AMZN](../../tickers/AMZN - Amazon.com Inc.md) |
| Meta | 원자력 최대 약정 ~6.6GW (Vistra·CEG·Oklo·TerraPower) | +0.14 (2026-06-29) | 연간 capex 가이던스 $125–145B 상향, 구글의 Gemini 사용 제한 보도 | [META](../../tickers/META - Meta Platforms Inc.md) |
| Alphabet | Kairos SMR 500MW 첫 기업 PPA | +0.07 (2026-06-29) | 다우 편입 첫날 +3.7%, AI 컴퓨트 인프라용 ~$80B 주식 발행 발표 | [GOOGL](../../tickers/GOOGL - Alphabet Inc.md) |
| Oracle | Bloom 연료전지 2.8GW — BTM 대표 사례 | +0.13 (2026-06-29) | RPO $638B(+363%)·OCI +93% vs 주간 -19% 급락, FY27 $40B 추가 조달 계획 | [ORCL](../../tickers/ORCL - Oracle Corporation.md) |
| OpenAI · xAI | 비상장 — xAI Colossus 가 BTM 가스의 원형 | — | — | 비상장 |
<!-- PLAYERS_END -->

## 시장 뉴스 로그 (최신순)

<!-- MARKET_NEWS_START -->
- **2026-06** ＋ **골드만삭스: 美 DC 전력 31GW(’25)→41GW(’26)→66GW(’27) 전망** — 2027년까지 수요 2배 — 전력이 AI 빌드아웃 제1 제약으로 (Goldman Sachs) [↗](https://www.goldmansachs.com/insights/articles/us-data-center-power-demand-projected-to-double-by-2027)
<!-- MARKET_NEWS_END -->

## 사실 누적 (Verified Facts)

<!-- FACTS_START -->
<!-- FACTS_END -->

## 인접 시장 (지도 링크)

- ➡ 공급측 [BTM 구내·전용 발전 조달](btm.md) — 속도 우선 — 구내 전용 발전
- ➡ 공급측 [그리드 접속 · 유틸리티 조달 (FTM)](grid-ftm.md) — 계통 접속 + 유틸리티·PPA

## 관련 위키

- [AI 데이터센터 전력 인프라 — 내 판단](../../../syntheses/ai-datacenter-power-infrastructure.md)
- [전력 생산·전력망 (AI·반도체 지도 자매 노드)](../ai-semiconductor/power-grid.md)
- [하이퍼스케일러·프런티어 CAPEX (AI·반도체 지도)](../ai-semiconductor/hyperscaler-capex.md)
