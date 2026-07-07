---
title: "Markets — 시장 노드 종합 폴더"
created: 2026-07-06
updated: 2026-07-06
domain: finance
type: index
weight: reference
confidence: high
tags: [routine-news, market-summary, meta]
sources: []
---

# Markets — 시장 노드별 종합 (루틴 관리)

이 폴더는 대시보드 **시장 지도의 노드(시장) 단위** 종합 페이지를 담는다.
티커별 로그(`../tickers/`)가 "기업 한 곳의 사건 누적"이라면, 여기는
**한 시장에 속한 기업들의 상황 + 시장 구조·병목·뉴스를 한 페이지로 종합**한 것이다.

> [!info] 대시보드 시장 지도 연결
> 대시보드에서 시장 지도의 노드를 클릭하면 이 폴더의 해당 파일이 지도 아래에
> 바로 표시된다. **파일 경로 규칙이 그 매칭의 계약**이므로 바꾸지 않는다:
> `wiki/news/markets/{map_id}/{market_id}.md`
> (예: `ai-semiconductor/hbm.md`) — `market_id` 는
> `indicator_dashboard/data/markets/{map_id}.json` 의 `markets[].id` 와 1:1.

## 폴더 구조

```
wiki/news/markets/
├── README.md               # 이 파일
└── ai-semiconductor/       # AI·반도체 시장지도 (map_id) — 노드당 1파일
    ├── hbm.md              # 예: HBM 시장 종합
    └── {market_id}.md
```

새 시장지도(예: power-ai)를 이 레이어에 붙일 때는 같은 규칙으로
`{map_id}/` 폴더를 만든다.

## 파일 내부 계약 (섹션 앵커)

| 섹션 | 앵커 | 갱신 주체 · 주기 |
|---|---|---|
| 시장 정의 / 병목 상태 | (본문) | market-research 루틴 · 주 1회 (지도 JSON 과 동기) |
| 시장 상황 종합 | `SYNTHESIS_START/END` | market-research 루틴 · 주 1회 (weekly_note 와 동기) |
| 소속 기업 동향 | `PLAYERS_START/END` | daily-market-analysis 루틴 · 해당 섹터 요일 |
| 시장 뉴스 로그 | `MARKET_NEWS_START/END` | market-research 루틴 · 주 1회 (뉴스 스토어와 동기) |
| 사실 누적 | `FACTS_START/END` | 두 루틴 — Tier-1 2곳 이상 확인된 사실만 |

## 규칙

- **문체 (2026-07-07~)**: 신규 갱신분은 [../FORMAT.md](../FORMAT.md) 의 투자 브리핑 v2 를 따른다.
  [시장 상황 종합]은 "**지금 상황 → 왜 중요 → 투자자 관점**" 3문장 구조, 뉴스 로그 요약은
  번역된 한국어 제목 + 전문용어 괄호 풀이([용어집](../glossary.md)). 기존 내용은 재작성하지 않는다.
- 모든 파일은 `type: claim`, `confidence: low`, `tags: [routine-news, market-summary, {map_id}, {market_id}]`
  frontmatter 를 유지한다 — 사람-작성 위키와 명확히 구분되는 루틴 격리 영역이다.
- **정확성 우선**: 출처(URL) 없는 내용을 쓰지 않는다. 시장 구조·수치는
  `data/markets/{map_id}.json` (SSOT) 과 어긋나면 안 된다 — 지도 JSON 을 먼저
  고치고 이 파일에 반영한다.
- 소속 기업 동향의 시그널·핵심 한 줄은 티커 로그(`../tickers/`)와 일치해야 한다
  (다른 데서 새로 만들지 않는다 — 티커 로그를 종합).
- 굳어진 사실은 [사실 누적]에 `[!fact]` 로 쌓고, 충분히 중요해지면 사람이
  `wiki/topics/` 로 승격(promote)한다 — 절차는 [../README.md](../README.md) 와 동일.
