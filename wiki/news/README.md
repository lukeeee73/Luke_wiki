---
title: "News — Routine Log Folder"
created: 2026-05-16
updated: 2026-05-16
domain: finance
type: index
weight: reference
confidence: high
tags: [routine-news, meta, watchlist]
sources: []
---

# News — 루틴 자동 수집 폴더

이 폴더는 `indicator_dashboard` 의 `daily-market-analysis` 루틴이 매일 자동으로 누적하는 watchlist 종목 뉴스 로그를 담는다.

## 사람이 작성한 위키와 분리되는 이유

- 모든 항목은 **AI 가 수집·요약한 것**이며, 검증되지 않은 상태로 들어온다.
- 따라서 frontmatter 는 항상 `type: claim`, `confidence: low`, `tags: [routine-news, ...]` 로 표시되어 다른 위키 페이지(원칙·프레임워크·내 판단)와 명확히 구분된다.
- 사실로 굳어진 항목은 별도 [사실 누적] 섹션에 모이고, 충분히 중요해지면 `wiki/topics/` 나 `wiki/entities/` 의 사람-편집 페이지로 승격(promote)될 수 있다.

## 폴더 구조

```
wiki/news/
├── README.md           # 이 파일
├── _dashboard.md       # 9 종목의 가장 최근 narrative_score / 핵심 이슈 한눈에 보기
├── AAPL.md             # 종목별 누적 로그 (역순)
├── MSFT.md
├── GOOGL.md
├── AMZN.md
├── NVDA.md
├── META.md
├── ORCL.md
├── PLTR.md
└── TSLA.md
```

## 각 종목 파일의 구조

```markdown
---
title: "{TICKER} — Routine News Log"
domain: finance
type: claim
weight: reference
confidence: low
tags: [routine-news, watchlist, {TICKER}]
---

# {TICKER} — Routine News Log

## 미해결 가설 (Open Claims)
- [ ] 2026-05-10: ... (pending)
- [x] 2026-05-08: ... (verified 2026-05-09 by Reuters)
- [~] 2026-05-07: ... (refuted 2026-05-09 by Apple)

## 사실 누적 (Verified Facts)
> [!fact] (검증일 YYYY-MM-DD, 출처) 본문

## 일자별 기록 (역순)

### YYYY-MM-DD
**narrative_score**: ±0.XX
**key_events**: ..., ...
**risks**: ...

> [!claim] (출처: ..., 날짜) 헤드라인
> 한 줄 한국어 요약. impact: + / - / neutral, category: ...
```

## 인식론 규칙

루틴이 매일 다음 절차를 따라 사실 신뢰도를 점진적으로 확정한다:

1. **신규 항목은 무조건 `[!claim]` (confidence: low) 로 들어온다.**
2. 다음 N 일 (기본 7 일) 안에 같은 사실을 보고하는 **독립 Tier-1 매체** (Reuters/Bloomberg/WSJ/FT/NYT/회사 IR) 가 1 건 이상 추가되면 → `[!fact]` 로 승격되고 [사실 누적] 으로 이동.
3. 같은 기간 안에 **반증** (회사 부인, 정정 보도, 후속 데이터 반대) 이 나오면 → Open Claims 에서 `[~] refuted` 마킹 + 일자별 기록에 반증 노트.
4. 7 일이 지나도 검증/반증 어느 쪽도 없으면 → `aged-out` 으로 마킹하고 Open Claims 에서 제외 (일자별 기록은 그대로 보존).

## 옵시디언에서 보는 법

- 폰에서 빠르게 보고 싶으면 `_dashboard.md` 에 9 종목 narrative_score / 핵심 이슈가 한 표로 모여 있음.
- 종목 깊게 보려면 `{TICKER}.md` → 맨 위 [미해결 가설] → 그 아래 [일자별 기록].
- 다른 위키 페이지와 섞이지 않도록 `routine-news` 태그로 필터 가능.

## 사람이 직접 수정해도 되는 부분

- [사실 누적] 섹션의 항목을 `wiki/topics/` 페이지로 승격하면서 출처 boost.
- [미해결 가설] 의 checkbox 를 수동으로 `[x]` / `[~]` 로 바꾸기 (루틴이 다음 실행에 인식).
- 루틴이 만든 [일자별 기록] 본문은 가급적 수정하지 말고 코멘트로 보강 (`> [!note] 내 의견` 추가).
