---
title: "Claude Code 세션 관리와 1M 컨텍스트"
created: 2026-04-19
updated: 2026-04-19
tags: [claude-code, session-management, context-window, context-rot, anthropic]
sources: [sources/claude-code-session-management-1m-context.md]
---

# Claude Code 세션 관리와 1M 컨텍스트

Anthropic의 Thariq Shihipar(Claude Code 팀)가 2026-04-15에 발행한 공식 가이드. 1M 컨텍스트 GA 출시와 함께 세션을 올바르게 관리하는 방법을 설명한다.

## 왜 1M 컨텍스트만으로는 부족한가

1M 컨텍스트 창으로 이전보다 훨씬 긴 작업(예: 전체 풀스택 앱 빌드)을 더 안정적으로 수행할 수 있게 됐다. 하지만 컨텍스트를 무한정 쌓는 것은 **컨텍스트 롯(Context Rot)** 문제를 일으킨다.

### 컨텍스트 롯이란

> 컨텍스트 크기가 증가할수록 모델 성능이 저하되는 현상

- 어텐션이 많은 토큰에 분산되어 집중도가 낮아짐
- 오래되거나 무관한 내용이 현재 작업을 방해(distract)함
- 초반 탐색·실패 과정이 후반 추론에 노이즈로 작용

## 5가지 전략

### 1. Continue (계속)
가장 단순한 선택. 컨텍스트 창의 **모든 내용이 여전히 필요**한 경우에만 사용.

적합한 경우:
- 이전 도구 출력이나 파일 내용을 다시 참조해야 할 때
- 결정 과정 전체가 현재 작업과 직결될 때

### 2. /rewind (되감기)
- `Esc` 두 번 또는 `/rewind` 실행
- 특정 메시지 시점으로 되돌아가 다시 프롬프트
- 그 이후 메시지 전부 삭제
- 잘못된 방향으로 깊이 들어갔을 때 "체크포인트 복원"

### 3. /compact (압축)
- 세션 전체를 요약 → 그 요약으로 히스토리 교체
- 손실(lossy)이 있지만 중요한 학습·파일은 보존 가능
- 압축 방향 지정 가능: `/compact focus on the auth refactor, drop the test debugging`
- 컨텍스트는 줄이면서 **동일 세션을 계속** 이어갈 때 사용

### 4. /clear (초기화)
- 완전히 새로운 세션 시작
- 이전 컨텍스트가 전혀 필요 없는 **독립적인 새 작업**에 사용
- 작업 간 전환 시 고영향 최적화 전략

### 5. 서브에이전트 (Subagents)
- 다음 작업을 자체 **깨끗한 컨텍스트**를 가진 독립 에이전트에 위임
- 서브에이전트: 독립 실행 → 최종 결과만 상위에 반환
- 상위 에이전트는 중간 탐색 과정 없이 **결론만** 수신

사용 예:
```
"이 스펙 파일을 기반으로 작업 결과를 검증하는 서브에이전트를 실행해줘"
```

## 핵심 판단 기준

> **"이 도구 출력이 다시 필요할까, 아니면 결론만 필요할까?"**

| 상황 | 전략 |
|------|------|
| 모든 컨텍스트가 필요 | Continue |
| 잘못된 방향에서 복귀 | /rewind |
| 컨텍스트를 줄이되 계속 진행 | /compact |
| 완전히 새 작업 | /clear |
| 결론만 필요, 과정은 불필요 | Subagent |

## 함께 출시된 기능

- **`/usage` 명령어**: 세션의 컨텍스트 사용량을 실시간으로 확인
- **1M 컨텍스트 GA**: Opus 4.6 및 Sonnet 4.6에서 표준 API 비용으로 사용 가능

## 관련 페이지

- [Claude Code](../concepts/claude-code.md)
- [Anthropic](../entities/anthropic.md)
- [Managed Agents](../concepts/managed-agents.md) — 서브에이전트 아키텍처와 연결
- [에이전트 하니스](../concepts/agent-harness.md) — 멀티 세션 연속성 패턴
