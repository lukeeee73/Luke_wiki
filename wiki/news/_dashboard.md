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

루틴이 매일 갱신한다. 9 종목의 가장 최근 narrative_score 와 핵심 이슈 한 줄을 모아서 폰에서 한눈에 보기 위한 페이지.

> [!info] 마지막 업데이트
> 루틴이 다음 실행에 자동으로 갱신한다.

## 최신 스냅샷

| Ticker | as_of | score | 핵심 한 줄 | open claims |
|---|---|---|---|---|
| [AAPL](AAPL.md)  | — | — | — | — |
| [MSFT](MSFT.md)  | — | — | — | — |
| [GOOGL](GOOGL.md)| — | — | — | — |
| [AMZN](AMZN.md)  | — | — | — | — |
| [NVDA](NVDA.md)  | — | — | — | — |
| [META](META.md)  | — | — | — | — |
| [ORCL](ORCL.md)  | — | — | — | — |
| [PLTR](PLTR.md)  | — | — | — | — |
| [TSLA](TSLA.md)  | — | — | — | — |

## 오늘의 시그널

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장 (예: NVDA capex 우려 5 연속)
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈 (예: 관세, FOMC) 로 동시 움직임

(루틴 첫 실행 전이라 비어 있음)

## 사용 팁

- 점수 변화가 큰 종목 우선 확인 → 해당 `{TICKER}.md` 의 [일자별 기록] 최신만 읽으면 충분.
- [미해결 가설] 컬럼이 비어있지 않은 종목은 후속 검증이 필요한 사안이 누적된 상태.
