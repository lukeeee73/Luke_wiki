# Luke Wiki

Obsidian으로 공부한 내용을 오래 보존하는 개인 지식 저장소입니다.
**내가 쓴 것과 자동 수집한 뉴스는 최상위 폴더 단위로 완전히 갈라져 있습니다.**

## Vault 지도

### 사람이 쓰는 곳

| 위치 | 용도 |
|---|---|
| `inbox/` | 아직 분류하지 않은 임시 메모, 모바일 캡처, 빠른 아이디어 |
| `sources/` | 원문, 기사, 강의, 논문, 코드 등 가공 전 자료 |
| `wiki/` | 정제된 지식 노트. 개념·원칙·주제·엔티티·종합 판단으로 분리 |
| `wiki/logs/` | 월별 작업 이력 (`logs/YYYY-MM.md`). `wiki/log.md`는 색인 |
| `_templates/` | Obsidian Templates 플러그인용 템플릿 |
| `scripts/` | vault 구조 검증 등 보조 도구 |

### 루틴이 쓰는 곳 (2026-08-07 분리)

| 위치 | 용도 |
|---|---|
| `routine-news/` | `indicator_dashboard` 루틴의 자동 뉴스 수집 결과. 종목 로그(`tickers/`) · 시장 노드 종합(`markets/`) · 날짜별 시그널(`signals/`) |

`routine-news/`는 예전에 `wiki/news/`에 있었습니다. 그 결과 `wiki/` 안 노트 320개 중 249개(78%)가
자동 수집물이고 사람이 쓴 건 71개뿐이라, 옵시디언 검색·그래프·태그 창이 검증되지 않은
`confidence: low` 뉴스에 잠식됐습니다. 이제 `wiki/`는 내가 쓴 것만 담고, `routine-news/`는
`.obsidian/app.json`의 `userIgnoreFilters`로 검색·그래프에서 제외됩니다.

**링크는 한 방향으로만 흐릅니다** — `routine-news/` → `wiki/`는 허용, `wiki/` → `routine-news/`는 금지.
뉴스를 근거로 쓰려면 승격 절차를 거쳐 원 출처 URL을 사람-작성 페이지의 `sources:`에 직접 넣습니다.

## 추천 사용 흐름

1. 빠른 생각은 `inbox/`에 적는다.
2. 공부 자료 원문은 `sources/`에 저장한다.
3. 정리된 지식은 `wiki/` 하위의 적절한 폴더로 승격한다.
4. 자동 수집 뉴스는 `routine-news/` 안에만 둔다 — 종목 로그는 `routine-news/tickers/`,
   그날의 시그널은 `routine-news/signals/YYYY-MM-DD.md`.
5. 뉴스에서 장기적으로 중요한 내용만 **원 출처를 검증한 뒤** `wiki/topics/`, `wiki/entities/`,
   `wiki/syntheses/`로 승격한다 (절차: `CLAUDE.md`의 Promotion 섹션).

## 구조 검증

```bash
python scripts/validate_vault.py
```

검증 스크립트는 다음을 확인합니다.

- 루틴 뉴스가 `wiki/news/`나 최상위 `news/`로 되살아나지 않았는지
- `routine-news` 태그가 사람-작성 영역(`wiki/`·`inbox/`·`sources/`·`_templates/`)으로 새지 않았는지
- 사람-작성 페이지가 `routine-news/`를 링크하지 않는지 (한 방향 규칙)
- 옵시디언 `userIgnoreFilters`에 `routine-news/`가 남아 있는지
- 주요 페이지가 YAML frontmatter를 갖고 있는지
- 빈 자동 뉴스 스캐폴드, 중복 티커 파일, 불필요한 `.gitkeep` 같은 혼란스러운 파일이 다시 생기지 않았는지
