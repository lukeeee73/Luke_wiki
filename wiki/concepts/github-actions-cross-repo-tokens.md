---
title: "GitHub Actions 저장소 간 자동화 — 토큰과 트리거"
created: 2026-07-05
updated: 2026-07-05
domain: ai
type: framework
weight: reference
confidence: high
tags: [github-actions, automation, ci-cd, tokens, repository-dispatch]
sources: [sources/github-actions-cross-repo-tokens.md]
---

# GitHub Actions 저장소 간 자동화 — 토큰과 트리거

## 핵심 구분: 방향이 다른 두 토큰

> [!principle] 원칙
> 토큰은 항상 "권한을 넘겨주는 저장소"에서 발급되고, "그 권한을 쓸 저장소"에 시크릿으로 저장된다. 같은 "토큰"이어도 방향이 다르면 완전히 다른 물건이다.

| | A가 B를 읽기만 함 | A가 B를 깨움(실행 트리거) |
|---|---|---|
| 토큰 발급 대상 저장소 | B (읽히는 쪽) | B (깨워지는 쪽) |
| 필요한 권한 | Contents: Read-only | Contents: Read and write |
| 토큰을 저장(Secret)하는 위치 | A (읽는 쪽 Settings → Secrets) | A (깨우는 쪽 Settings → Secrets) |
| 이번 사례 이름 | `WIKI_REPO_TOKEN` | `DASHBOARD_DISPATCH_TOKEN` |

## GitHub Actions 트리거 4종

```yaml
on:
  schedule:
    - cron: "0 9 * * 1"      # 정기 폴링 — 느슨하지만 언젠가는 반영됨
  workflow_dispatch:          # Actions 탭에서 사람이 수동 실행
  push:
    branches: ["**"]          # 이 저장소에 푸시되면 (같은 저장소 안에서만 작동)
  repository_dispatch:        # 다른 저장소가 API로 "지금 실행해" 라고 찌를 때
    types: [wiki-updated]
```

> [!fact] 사실
> `push` 트리거는 저장소 경계를 넘지 못한다. 저장소 경계를 넘어 다른 저장소의 워크플로를 깨우려면 `repository_dispatch`가 필요하다.

## 저장소 간 트리거 흐름 (luke_wiki → Indicator_dashboard 사례)

```
[luke_wiki 에 git push]
        ↓
[luke_wiki: notify-dashboard.yml 실행]
   curl -X POST .../repos/{dashboard}/dispatches
   Authorization: Bearer $DASHBOARD_DISPATCH_TOKEN
        ↓
[Indicator_dashboard: wiki-sync.yml 이 repository_dispatch 로 깨어남]
   Checkout luke_wiki (WIKI_REPO_TOKEN 또는 공개면 기본 토큰)
   build_wiki_graph.py 실행
        ↓
[data/wiki/graph.json 갱신 → 커밋 → 대시보드 배포]
```

두 토큰(`WIKI_REPO_TOKEN`, `DASHBOARD_DISPATCH_TOKEN`)은 정반대 방향으로 움직인다 — 하나는 "읽기용", 하나는 "깨우기용"이며 발급처와 저장처가 서로 뒤바뀐 관계다.

> [!judgment] 실패 진단 요령
> 같은 이름·같은 권한으로 아무 저장소에나 토큰을 등록하면 "권한은 있는데 저장소가 틀려서" 조용히 실패한다. 이때 GitHub API는 대개 "권한 없음"이 아니라 404("그런 저장소 없음")를 돌려주므로, 토큰을 발급한 저장소와 시크릿을 등록한 저장소가 서로 반대인지 표로 짚어보면 대부분 여기서 원인이 발견된다.

## 보안 원칙 (최소 권한)

> [!principle] 원칙
> - Repository access는 항상 "Only select repositories" — 대상 저장소 하나만 지정
> - 권한은 실제로 쓰는 최소치만 부여 (읽기면 Read-only)
> - 만료일을 짧게 설정
> - Secrets는 로그에 자동 마스킹되지만, `echo $TOKEN` 같은 코드는 작성하지 않는다
> - 시크릿이 없어도 워크플로가 죽지 않도록 `continue-on-error: true`로 감싸면 토큰 설정 전/후 어느 쪽이든 안전하다

## 관련 페이지

- [에이전트 하니스 (Agent Harness)](./agent-harness.md)
- [Managed Agents](./managed-agents.md)
