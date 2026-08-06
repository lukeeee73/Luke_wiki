# Luke Wiki

Obsidian으로 공부한 내용을 오래 보존하고, 자동 뉴스 수집 결과는 별도 격리해서 관리하는 개인 지식 저장소입니다.

## Vault 지도

| 위치 | 용도 | 사람이 직접 쓰는가? |
|---|---|---|
| `inbox/` | 아직 분류하지 않은 임시 메모, 모바일 캡처, 빠른 아이디어 | 예 |
| `sources/` | 원문, 기사, 강의, 논문, 코드 등 가공 전 자료 | 예 |
| `wiki/` | 정제된 지식 노트. 개념·원칙·주제·엔티티·종합 판단으로 분리 | 예 |
| `wiki/news/` | 자동 뉴스 수집 루틴의 대시보드와 가이드. 종목별 원본 로그는 `wiki/news/tickers/`, 날짜별 시그널은 `wiki/news/signals/`에 격리 | 원칙적으로 루틴이 씀 |
| `wiki/logs/` | 월별 작업 이력 (`logs/YYYY-MM.md`). `wiki/log.md`는 색인 | 예 |
| `_templates/` | Obsidian Templates 플러그인용 템플릿 | 예 |
| `scripts/` | vault 구조 검증 등 보조 도구 | 예 |

## 추천 사용 흐름

1. 빠른 생각은 `inbox/`에 적는다.
2. 공부 자료 원문은 `sources/`에 저장한다.
3. 정리된 지식은 `wiki/` 하위의 적절한 폴더로 승격한다.
4. 자동 수집 뉴스는 `wiki/news/` 안에만 두되, 종목별 원본 로그는 `wiki/news/tickers/`, 그날의 시그널은 `wiki/news/signals/YYYY-MM-DD.md` 로 생성한다.
5. 뉴스에서 장기적으로 중요한 내용만 검증 후 `wiki/topics/`, `wiki/entities/`, `wiki/syntheses/`로 승격한다.

## 구조 검증

```bash
python scripts/validate_vault.py
```

검증 스크립트는 다음을 확인합니다.

- 루틴 뉴스 태그가 `wiki/news/` 밖으로 새지 않았는지
- 주요 위키 페이지가 YAML frontmatter를 갖고 있는지
- 빈 루트 노트, 최상위 `news/`, 빈 자동 뉴스 스캐폴드, 중복 티커 파일, 불필요한 `.gitkeep` 같은 혼란스러운 파일이 다시 생기지 않았는지
