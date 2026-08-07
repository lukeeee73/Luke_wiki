---
title: "Routine News — 자동 수집 격리 폴더"
created: 2026-05-16
updated: 2026-08-07
domain: finance
type: index
weight: reference
confidence: high
tags: [routine-news, meta, watchlist]
sources: []
---

# Routine News — 루틴 자동 수집 폴더

이 폴더는 `indicator_dashboard` 의 `daily-market-analysis` 루틴이 매일 자동으로 누적하는 watchlist 종목 뉴스 로그를 담는다.

> [!important] 🚧 `wiki/` 밖으로 이전 (2026-08-07) — 경로 계약 변경
> 이 폴더는 **`wiki/news/` 였다가 최상위 `routine-news/` 로 옮겨졌다.**
> `wiki/` 는 이제 사람이 직접 쓴 지식만 담는다 — 루틴 산출물은 `wiki/` 아래 어디에도 쓰지 않는다.
>
> | 예전 경로 | 지금 경로 |
> |---|---|
> | `wiki/news/tickers/{TICKER} - {COMPANY}.md` | `routine-news/tickers/{TICKER} - {COMPANY}.md` |
> | `wiki/news/markets/{map_id}/{market_id}.md` | `routine-news/markets/{map_id}/{market_id}.md` |
> | `wiki/news/signals/YYYY-MM-DD.md` | `routine-news/signals/YYYY-MM-DD.md` |
> | `wiki/news/_dashboard.md` | `routine-news/_dashboard.md` |
>
> 파일명 규칙(`{TICKER} - {COMPANY}.md`)과 폴더 내부 구조는 **그대로**다 — 바뀐 건 앞의 `wiki/news/` → `routine-news/` 뿐이다.
> `indicator_dashboard` 쪽에서 고쳐야 할 것은 아래 [연동 저장소가 고쳐야 할 것](#연동-저장소가-고쳐야-할-것) 참고.

## 왜 옮겼나

옵시디언 vault 에서 **내가 쓴 것과 루틴이 쓴 것이 섞이는 문제**를 경로 수준에서 끊기 위해서다.

- 분리 직전 기준으로 `wiki/` 안 마크다운 320개 중 249개(78%)가 루틴 산출물이고 사람이 쓴 건 71개뿐이었다 — 내 지식 저장소가 아니라 뉴스 아카이브처럼 보였다.
- 검색·그래프·태그 창이 전부 `confidence: low` 자동 수집물에 잠식됐다.
- 사람-작성 페이지에서 `../news/...` 로 나가는 링크가 다수 끊어진 채 방치됐다 (`news/AAPL.md` 처럼 옛 파일명).

이제 경계는 **폴더 하나**로 단순해졌다: `routine-news/` 안이면 루틴, 밖이면 사람.
`.obsidian/app.json` 의 `userIgnoreFilters` 가 이 폴더를 검색·그래프·퀵스위처에서 제외한다.

> [!important] ✍️ 형식 개편 (2026-07-07) — 투자 브리핑 v2
> **2026-07-07 부터 모든 신규 항목은 [FORMAT.md](FORMAT.md) 의 "투자 브리핑 v2" 형식으로 쓴다.**
> 쉬운 한국어 · "무슨 일 → 왜 중요 → 주가에 의미" 3단 구조 · 신호등(🟢⚪🔴) 표기 ·
> "앞으로 지켜볼 것" 필수 · 전문용어는 괄호 풀이 + [용어집](glossary.md).
> 아래 "각 종목 파일의 구조"의 마커·섹션 계약은 유지되고, **엔트리 내부 문체만** v2 를 따른다.
> 2026-07-06 이전에 쌓인 항목은 옛 형식 그대로 보존한다 (재작성 금지).

> [!info] 대시보드 시장 지도 연결
> 이 로그는 대시보드 **시장 지도**(주식 탭)에도 노출된다 — 시장/기업 상세 패널의
> "옵시디언 위키 노트" 섹션이 지도 플레이어의 티커를 `tickers/{TICKER} - *.md` 와
> 자동 매칭해서, 지도에서 바로 종목 뉴스 로그 전문을 읽을 수 있다.
> 파일명 규칙(`{TICKER} - {COMPANY}.md`)이 이 매칭의 계약이므로 형식을 바꾸지 않는다.

## 사람이 작성한 위키와 분리되는 이유

- 모든 항목은 **AI 가 수집·요약한 것**이며, 검증되지 않은 상태로 들어온다.
- 따라서 frontmatter 는 항상 `type: claim`, `confidence: low`, `tags: [routine-news, ...]` 로 표시되어 다른 위키 페이지(원칙·프레임워크·내 판단)와 명확히 구분된다.
- 사실로 굳어진 항목은 별도 [사실 누적] 섹션에 모이고, 충분히 중요해지면 `wiki/topics/` 나 `wiki/entities/` 의 사람-편집 페이지로 승격(promote)될 수 있다.

### 링크는 한 방향으로만 흐른다

```
routine-news/  ──링크 가능──▶  wiki/     (맥락 참조. 예: 시장 노드 → 개념 페이지)
routine-news/  ◀──링크 금지──  wiki/     (사람-작성 페이지는 루틴 산출물을 링크하지 않는다)
```

사람-작성 페이지가 `routine-news/` 를 링크하면 검증되지 않은 `confidence: low` 자료에
내 판단이 매달리게 되고, 루틴이 파일을 지우거나 이름을 바꿀 때 링크가 조용히 깨진다.
루틴 뉴스를 근거로 쓰고 싶으면 **promote 절차를 거쳐** 원 출처(Tier-1/IR URL)를 사람-작성 페이지의
`sources:` 에 직접 박는다 — 뉴스 로그 파일을 가리키지 않는다.

## 폴더 구조

```
routine-news/            # ← 최상위. wiki/ 안이 아니다.
├── README.md           # 이 파일
├── FORMAT.md           # ✍️ 투자 브리핑 v2 — 신규 항목 글쓰기 형식 (2026-07-07~)
├── glossary.md         # 용어집 — 브리핑에 나오는 전문용어 한 줄 풀이
├── _dashboard.md       # 모든 종목의 가장 최근 narrative_score / 핵심 이슈 한눈에 보기 (섹터별)
│                        # + 최근 시그널 링크 목록. 시그널 본문은 담지 않는다.
├── tickers/            # 자동 생성된 종목별 원본 로그 격리 폴더
│   └── {TICKER} - {COMPANY}.md
│                        # 종목별 누적 로그 (역순). 한국 종목은 {NUMBER}.KS - {COMPANY}.md
├── markets/            # 시장지도 노드별 종합 페이지 — 기업 동향 + 시장 구조·병목·뉴스
│   └── {map_id}/{market_id}.md
│                        # 예: ai-semiconductor/hbm.md — 규칙은 markets/README.md
└── signals/            # 날짜별 시그널 — 하루 한 파일
    └── YYYY-MM-DD.md
                         # 그날 처리한 섹터에서 감지한 시그널. 파일명은 날짜만.
```

루틴은 종목 파일을 반드시 `routine-news/tickers/` 아래에만, 시장 종합 파일을 반드시
`routine-news/markets/{map_id}/` 아래에만, 시그널을 반드시 `routine-news/signals/` 아래에만 만든다.

**절대 쓰지 않는 곳**: `wiki/` 전체(하위 폴더 포함), `inbox/`, `sources/`, 저장소 루트의 임시 `.md`,
그리고 옛 경로인 `wiki/news/` 와 최상위 `news/`. 이 규칙은 `scripts/validate_vault.py` 가 강제한다.

## 시그널은 왜 하루 한 파일인가 (2026-08-06 분리)

> [!important] 같은 파일 = 충돌 지점
> 예전에는 매일의 `## 오늘의 시그널` 을 `_dashboard.md` **한 파일에 계속 덧붙였다.**
> 이 저장소는 옵시디언(obsidian-git)·루틴·ingest 세 곳에서 동시에 쓰이기 때문에,
> 매일 같은 파일의 같은 구역을 고치는 구조는 git 머지 충돌을 반복해서 만들었다.
> 실제로 분리 전 `_dashboard.md` 에는 시그널 23개가 **날짜 순서가 뒤엉킨 채** 쌓여 있었고
> (07-15 다음에 07-23), 내용 없는 빈 `### 감지된 패턴` 헤딩 7개가 머지 잔해로 남아 있었다.

그래서 시그널은 **하루 한 파일**(`signals/YYYY-MM-DD.md`)로 쓴다. 서로 다른 날은 서로 다른
파일이므로 두 writer 가 같은 날 같은 줄을 고칠 일이 구조적으로 없다.

**루틴이 지켜야 할 것:**

1. 시그널은 항상 `signals/{오늘 날짜}.md` 를 **새로 만들어** 쓴다. 기존 파일에 덧붙이지 않는다.
2. frontmatter 는 `type: claim` / `confidence: low` / `tags: [routine-news, signals]` 고정.
3. `_dashboard.md` 에서는 "최근 시그널" 목록 맨 위에 링크 한 줄만 추가한다 (본문 금지).
4. 같은 날 두 번 실행되면 그날 파일을 **덮어쓴다** (append 아님) — 멱등성 유지.

`_dashboard.md` 와 종목별 로그 파일의 watchlist 는 `indicator_dashboard` 의
`scripts/fetch_fred.py` 의 `STOCKS` 딕셔너리를 단일 진실 공급원으로 사용한다.
종목·섹터가 추가/변경되고 실제 기록할 뉴스가 있으면 루틴이 새 `tickers/{TICKER} - {COMPANY}.md` 를 자동 생성하고
`_dashboard.md` 의 해당 섹터 표에 행을 추가한다.

## 섹터 그룹 (현재 운영 중)

`_dashboard.md` 에서 종목 행을 다음 섹터 헤더 아래에 묶는다 (순서 고정):

1. 빅테크 / 소프트웨어 (10 종목)
2. 반도체 — AI 칩 · 설계 (11 종목)
3. 반도체 — 메모리 (HBM·DRAM) (3 종목)
4. 반도체 — 파운드리 · 패키징 · 기판 (3 종목)
5. 반도체 — 장비 · 소재 (10 종목)
6. AI 인프라 — 네트워킹 · 광 · 네오클라우드 (5 종목)
7. 로보틱스 / 피지컬 AI (5 종목)
8. 자동차 / 모빌리티 (10 종목)
9. 바이오 / 제약 / 헬스케어 (10 종목)
10. 에너지 / 원자재 (10 종목)
11. 금융 (10 종목)
12. 소비재 (10 종목)
13. 산업재 / 방산 (14 종목)
14. 부동산 (REITs) (10 종목)
15. 통신 / 미디어 (10 종목)
16. 유틸리티 / 전력 (10 종목)
17. 전력 인프라 (AI) (10 종목)
18. 조선 (한국) (4 종목)

이 순서는 `indicator_dashboard` 의 `app.js` `STOCK_GROUPS` 및 `scripts/watchlist_data.py` `GROUPS` 와 일치한다.
반도체 4개 그룹 + AI 인프라 그룹의 종목 구성은 **AI·반도체 시장지도 노드의 플레이어와 1:1 동기화**가
원칙이다 (2026-07-06 정합 작업 — 시장지도에서 봐야 하는 기업은 전부 watchlist 에 있다).


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

### YYYY-MM-DD (요일) — 신호등: 🟢 순풍 (+0.XX)

**세 줄 요약**
1. ... (전문용어 없이)

**뉴스 브리핑**

**① 한국어로 번역한 제목** 🟢
- **무슨 일**: ... / **왜 중요**: ... / **주가에 의미**: ...
- 출처: [매체](URL) · 날짜

**앞으로 지켜볼 것**
- [ ] 날짜 이벤트 — 확인할 것: ...
```

일자별 엔트리의 상세 작성 규칙(신호등 매핑, 뉴스당 4줄 고정, 금지 목록)은
**[FORMAT.md](FORMAT.md) 가 단일 기준**이다. 2026-07-06 이전 엔트리는
`**narrative_score**: / **key_events**: / [!claim]` 구조의 옛 형식으로 남아 있다.

## 인식론 규칙

루틴이 매일 다음 절차를 따라 사실 신뢰도를 점진적으로 확정한다:

1. **신규 항목은 무조건 `[!claim]` (confidence: low) 로 들어온다.**
2. 다음 N 일 (기본 7 일) 안에 같은 사실을 보고하는 **독립 Tier-1 매체** (Reuters/Bloomberg/WSJ/FT/NYT/회사 IR) 가 1 건 이상 추가되면 → `[!fact]` 로 승격되고 [사실 누적] 으로 이동.
3. 같은 기간 안에 **반증** (회사 부인, 정정 보도, 후속 데이터 반대) 이 나오면 → Open Claims 에서 `[~] refuted` 마킹 + 일자별 기록에 반증 노트.
4. 7 일이 지나도 검증/반증 어느 쪽도 없으면 → `aged-out` 으로 마킹하고 Open Claims 에서 제외 (일자별 기록은 그대로 보존).


## Obsidian 파일 생성 규칙

- `routine-news/` 최상위에는 `README.md` · `FORMAT.md` · `glossary.md` · `_dashboard.md` 만 둔다.
  나머지는 전부 `tickers/` · `markets/` · `signals/` 하위로 간다.
- 종목별 자동 로그는 반드시 `routine-news/tickers/{TICKER} - {Company}.md` 로 생성한다.
- **그날의 시그널은 `routine-news/signals/YYYY-MM-DD.md` 새 파일로 만든다.**
  `_dashboard.md` 본문에 `## 오늘의 시그널` 섹션을 덧붙이지 않는다 — 아래 이유 참고.
- watchlist 에 **신규 편입된 종목은 회사 소개를 포함한 스켈레톤 파일을 미리 만들어 둔다**
  (대시보드 시장 지도의 플레이어 클릭이 티커 파일명 매칭으로 이 파일에 연결되기 때문).
  `_dashboard.md` 에는 score `—` (수집 전) 행으로 표시하고, 해당 섹터의 첫 루틴 실행 때 채운다.
- 같은 티커의 회사명이 달라져도 새 파일을 만들지 말고 기존 티커 파일을 갱신한다. 예: `DE - Deere & Company.md` 하나만 유지한다.
  **같은 티커의 파일이 2개 생기면 즉시 병합한다** (2026-07-06 EQIX·PLD 중복 병합 사례).
- 회사 소개조차 없는 빈 스캐폴드(마커만 있는 파일)는 삭제한다.

## 옵시디언에서 보는 법

- 폰에서 빠르게 보고 싶으면 `_dashboard.md` 에 watchlist 전 종목 narrative_score / 핵심 이슈가 섹터별 표로 모여 있음.
- 종목 깊게 보려면 `tickers/{TICKER} - {Company}.md` → 맨 위 [미해결 가설] → 그 아래 [일자별 기록].
- 다른 위키 페이지와 섞이지 않도록 `routine-news` 태그로 필터 가능.

## 사람이 직접 수정해도 되는 부분

- [사실 누적] 섹션의 항목을 `wiki/topics/` 페이지로 승격하면서 출처 boost.
- 장기 투자 판단으로 이어지는 경우 `_templates/news-promotion.md` 로 새 사람-작성 노트를 만든 뒤 원 뉴스 로그를 `sources` 또는 본문 링크에 남긴다.
- [미해결 가설] 의 checkbox 를 수동으로 `[x]` / `[~]` 로 바꾸기 (루틴이 다음 실행에 인식).
- 루틴이 만든 [일자별 기록] 본문은 가급적 수정하지 말고 코멘트로 보강 (`> [!note] 내 의견` 추가).

## 연동 저장소가 고쳐야 할 것

경로가 `wiki/news/` → `routine-news/` 로 바뀌었으므로, **이 저장소에 쓰거나 이 저장소를 읽는
`lukeeee73/Indicator_dashboard` 쪽 코드도 같이 고쳐야 한다.** 고치기 전까지는:

- daily 루틴이 예전 경로에 쓰면 → `wiki/news/` 가 되살아나고 `validate_vault.py` 가 실패한다.
- 대시보드 시장 지도의 "옵시디언 위키 노트" 패널이 티커 파일을 못 찾아 빈 채로 뜬다.

고쳐야 할 지점 (경로 문자열만 바꾸면 된다 — 파일명 규칙과 폴더 구조는 그대로):

| 위치 | 하는 일 | 바꿀 것 |
|---|---|---|
| `daily-market-analysis` 루틴 | 종목 로그·시그널·시장 노드 갱신 후 이 저장소에 커밋 | 쓰기 경로 `wiki/news/` → `routine-news/` |
| `market-research` 루틴 | 시장 노드 종합 페이지 갱신 | 쓰기 경로 `wiki/news/markets/` → `routine-news/markets/` |
| 시장 지도 노트 매칭 | 플레이어 티커 ↔ `{TICKER} - *.md` 자동 매칭 | 읽기 경로 `wiki/news/tickers/` → `routine-news/tickers/` |
| `Sync Wiki Graph` 워크플로 | 위키 그래프 동기화 | `wiki/**` 만 스캔한다면 `routine-news/**` 포함 여부를 결정 |

> [!tip] 뉴스 수집을 아예 멈추기로 했다면
> 위 경로들을 고치는 대신 `Indicator_dashboard` 에서 daily 루틴의 **이 저장소 push 단계만 제거**하면 된다.
> 그러면 `routine-news/` 는 마지막 수집일(2026-08-07) 기준으로 얼어붙은 아카이브가 되고,
> `wiki/` 는 계속 사람이 쓰는 위키로 남는다. 이미 쌓인 내용은 그대로 읽을 수 있다.

## 구조 검증

루틴 또는 수동 정리 후 다음 명령으로 뉴스 격리가 깨지지 않았는지 확인한다.

```bash
python scripts/validate_vault.py
```
