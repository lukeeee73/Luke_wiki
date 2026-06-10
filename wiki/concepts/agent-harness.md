---
title: "에이전트 하니스 (Agent Harness)"
created: 2026-04-05
updated: 2026-06-09
domain: ai
type: framework
weight: important
confidence: high
tags: [agent-harness, multi-agent, agentic-systems, LLM]
sources: [sources/anthropic-harness-design-long-running-apps.md]
---

# 에이전트 하니스 (Agent Harness)

## 정의

에이전트 하니스는 LLM 에이전트가 복잡한 작업을 수행할 수 있도록 감싸는 **제어 구조(control structure)**다. 단일 에이전트 루프를 넘어서 여러 에이전트의 역할 분담, 세션 간 상태 관리, 반복적 개선 루프를 조율한다.

비유: 말을 제어하는 마구(馬具, harness)처럼, 에이전트 하니스는 AI 에이전트의 행동을 목표 방향으로 조율하고 제어하는 장치다.

## 하니스가 필요한 이유

단일 에이전트 단일 프롬프트 방식의 한계:
- Context window 제한으로 장기 작업 불가
- 세션 간 기억 없음 → 진행 상태 손실
- 자체 검증 약점 → 품질 저하
- 범위 과소 설정 경향 (Planner 없을 때)

## 주요 하니스 패턴

### 1. Generator-Evaluator 패턴

GAN(Generative Adversarial Network)에서 영감받은 구조:
- **Generator**: 결과물 생성
- **Evaluator**: 평가 및 피드백 제공
- 반복적 피드백 루프로 품질 향상

상세: [Generator-Evaluator 루프](../principles/generator-evaluator-loop.md)

### 2. Initializer-Coder 패턴

장기 멀티 세션 작업을 위한 구조:
- **Initializer**: 첫 세션에서 기반 인프라 구축 (feature_list.json, claude-progress.txt, init.sh)
- **Coder**: 이후 세션에서 점진적 진행 및 상태 업데이트

### 3. Planner-Generator-Evaluator 패턴

Anthropic의 완전한 3-에이전트 하니스:
- **Planner**: raw 프롬프트 → 상세 명세
- **Generator**: 명세 기반 구현
- **Evaluator**: 실행 중인 앱 테스트

## 하니스 설계 원칙

1. **역할 분리**: 각 에이전트에 명확한 책임 부여
2. **검증 가능한 기준**: 주관적 품질을 명시적·측정 가능한 기준으로 분해
3. **상태 지속성**: 세션 간 상태를 구조화된 파일로 유지
4. **점진적 접근**: 한 번에 전체를 완성하려 하지 않음
5. **모델에 맞는 복잡도**: 강한 모델일수록 단순한 하니스로 충분

## 하니스 복잡도와 모델 능력의 관계

> 하니스의 복잡도는 **모델의 약점을 보완**하기 위한 것이다. 모델이 발전할수록 하니스는 단순해질 수 있다.

Anthropic 사례: Opus 4.5 이후 context reset 불필요, Claude Agent SDK 자동 컴팩션으로 전체 빌드를 단일 세션으로 실행 가능.

### 4. 메타-하니스 패턴 (Managed Agents)

플랫폼 수준에서 세션·하니스·샌드박스를 가상화한 구조 (2026-04-08 출시):

- **Session**: append-only 이벤트 로그, 하니스 외부에 영속 저장
- **Harness**: 무상태 제어 루프, 도구 호출 라우팅
- **Sandbox**: 지연 프로비저닝 격리 실행 환경

핵심 원칙: "뇌(Claude)와 손(실행환경)의 분리" — 컨테이너는 필요할 때만 프로비저닝됨.
성능 효과: p50 TTFT 60% 감소, p95 TTFT 90%+ 감소.

상세: [Managed Agents](./managed-agents.md)

## 관련 페이지

- [Generator-Evaluator 루프](../principles/generator-evaluator-loop.md)
- [Managed Agents](./managed-agents.md)
- [Anthropic 하니스 엔지니어링](../topics/anthropic-harness-engineering.md)
- [Anthropic Managed Agents](../topics/anthropic-managed-agents.md)
- [Claude Code](./claude-code.md)
