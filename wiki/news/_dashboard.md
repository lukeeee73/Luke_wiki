---
title: "Watchlist News Dashboard"
created: 2026-05-16
updated: 2026-05-16
domain: finance
type: index
weight: reference
confidence: low
tags: [routine-news, watchlist, dashboard]
sources: []
---

# Watchlist News Dashboard

루틴이 매일 갱신한다. 섹터 그룹별로 watchlist 종목들의 가장 최근 narrative_score 와 핵심 이슈 한 줄을 모아서 폰에서 한눈에 보기 위한 페이지.

> [!info] 마지막 업데이트
> 루틴이 다음 실행에 자동으로 갱신한다.

## 최신 스냅샷 (섹터별)


### 빅테크 / AI 플랫폼

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [AAPL](AAPL.md) | — | — | — | — |
| [MSFT](MSFT.md) | — | — | — | — |
| [GOOGL](GOOGL.md) | — | — | — | — |
| [AMZN](AMZN.md) | — | — | — | — |
| [META](META.md) | — | — | — | — |
| [ORCL](ORCL.md) | — | — | — | — |
| [PLTR](PLTR.md) | — | — | — | — |

### 반도체

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [NVDA](NVDA.md) | — | — | — | — |
| [AMD](AMD.md) | — | — | — | — |
| [TSM](TSM.md) | — | — | — | — |
| [AVGO](AVGO.md) | — | — | — | — |

### 자동차 / 모빌리티

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [TSLA](TSLA.md) | — | — | — | — |

### 바이오 / 제약 / 헬스케어

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [LLY](LLY.md) | — | — | — | — |
| [NVO](NVO.md) | — | — | — | — |
| [JNJ](JNJ.md) | — | — | — | — |
| [UNH](UNH.md) | — | — | — | — |

### 에너지 / 원자재

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [XOM](XOM.md) | — | — | — | — |
| [FCX](FCX.md) | — | — | — | — |
| [NEM](NEM.md) | — | — | — | — |

### 금융

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [JPM](JPM.md) | — | — | — | — |
| [V](V.md) | — | — | — | — |
| [BRK-B](BRK-B.md) | — | — | — | — |

### 소비재

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [WMT](WMT.md) | — | — | — | — |
| [COST](COST.md) | — | — | — | — |
| [KO](KO.md) | — | — | — | — |

### 산업재 / 방산

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [CAT](CAT.md) | — | — | — | — |
| [BA](BA.md) | — | — | — | — |
| [LMT](LMT.md) | — | — | — | — |

### 부동산 (REITs)

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [AMT](AMT.md) | — | — | — | — |
| [PLD](PLD.md) | — | — | — | — |
| [EQIX](EQIX.md) | — | — | — | — |

### 조선 (한국)

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [329180.KS](329180.KS.md) | — | — | — | — |
| [042660.KS](042660.KS.md) | — | — | — | — |


## 오늘의 시그널

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장 (예: NVDA capex 우려 5 연속)
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈 (예: 관세, FOMC, 유가, 비만치료제 임상) 로 동시 움직임
- **섹터간 전파**: 한 섹터의 충격이 다른 섹터로 번지는 패턴 (예: 반도체 capex → 부동산 REIT 데이터센터 수요)

(루틴 첫 실행 전이라 비어 있음)

## 사용 팁

- 점수 변화가 큰 종목 우선 확인 → 해당 `{TICKER}.md` 의 [일자별 기록] 최신만 읽으면 충분.
- [미해결 가설] 컬럼이 비어있지 않은 종목은 후속 검증이 필요한 사안이 누적된 상태.
- 섹터 단위로 묶어서 보면 매크로 충격이 어떤 종목들에 동시에 영향을 주는지 빠르게 파악 가능.
