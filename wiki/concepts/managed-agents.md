---
title: "Managed Agents"
created: 2026-04-11
updated: 2026-04-11
domain: ai
type: framework
weight: important
confidence: high
tags: [managed-agents, meta-harness, session, sandbox, harness, anthropic, multi-agent]
sources: [sources/anthropic-managed-agents.md]
---

# Managed Agents

## 정의

**Managed Agents**는 Anthropic이 2026-04-08 출시한 호스팅 에이전트 인프라 서비스다.
에이전트의 세 구성요소—**세션(Session)**, **하니스(Harness)**, **샌드박스(Sandbox)**—를 가상화하여,
개발자가 에이전트 로직에만 집중할 수 있도록 공통 인프라를 플랫폼 수준에서 추상화한다.

핵심 슬로건: **"뇌(brain)와 손(hands)의 분리 (Decoupling the brain from the hands)"**

## 핵심 구성요소

### Session (세션)

- 에이전트 인터랙션의 **append-only 이벤트 로그**
- 하니스 외부에 영속 저장 — Claude의 context window 밖에 존재
- `getEvents()` 인터페이스로 brain이 위치 기반 슬라이스를 선택하여 조회
- 운영 체제의 파일 시스템과 유사: 프로세스(Claude)가 종료돼도 데이터 유지

### Harness (하니스)

- **무상태(stateless)** 제어 루프
- Claude를 호출하고 도구 호출을 실행 환경으로 라우팅
- 메타-하니스: 특정 하니스 로직에 무관심, 일반 인터페이스 제공

### Sandbox (샌드박스)

- Claude가 코드 실행 및 파일 조작을 수행하는 격리된 환경
- **지연 프로비저닝**: `execute(name, input) → string` 도구 호출 시에만 컨테이너 생성
- 성능 효과: p50 TTFT ~60% 감소, p95 TTFT 90%+ 감소

## 설계 철학: 메타-하니스

Managed Agents는 특정 하니스에 의견을 갖지 않는 **메타-하니스**다.
의견을 갖는 것은 Claude 주변의 **인터페이스**뿐:

1. Claude는 **상태를 조작**할 수 있어야 한다 → Session
2. Claude는 **계산을 수행**할 수 있어야 한다 → Sandbox
3. Claude는 **많은 brain과 많은 hands로 확장**할 수 있어야 한다 → Multi-agent

운영 체제 비유: OS가 다양한 애플리케이션을 위한 메모리·프로세스·I/O 추상화를 제공하듯,
Managed Agents는 다양한 미래 하니스를 위한 일반 인터페이스를 제공한다.

## Claude Agent SDK

Managed Agents와 함께 **Claude Code SDK**가 **Claude Agent SDK**로 이름 변경됨.
- 코딩을 넘어 광범위한 에이전트 역량을 반영한 명칭
- 서브에이전트 기본 지원

## 이전 하니스 패턴과의 관계

Managed Agents 이전, Anthropic은 수동으로 관리하는 하니스 패턴을 발표했다:

| 문제 | 이전 방식 | Managed Agents |
|------|----------|----------------|
| 세션 연속성 | `claude-progress.txt` 수동 관리 | Session 이벤트 로그 자동화 |
| 실행 환경 | 로컬 설정 직접 구성 | Sandbox 지연 프로비저닝 |
| 멀티-에이전트 | 커스텀 오케스트레이션 | Subagents / Agent Teams |

관련 개념: [에이전트 하니스](./agent-harness.md)

## 관련 페이지

- [에이전트 하니스](./agent-harness.md)
- [Generator-Evaluator 루프](./generator-evaluator-loop.md)
- [Anthropic 하니스 엔지니어링](../topics/anthropic-harness-engineering.md)
- [Anthropic Managed Agents (토픽)](../topics/anthropic-managed-agents.md)
- [Anthropic](../entities/anthropic.md)
