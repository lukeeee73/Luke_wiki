---
title: "AI Domain Index"
created: 2026-05-02
updated: 2026-05-02
domain: ai
type: index
weight: foundational
confidence: high
tags: [도메인, AI, LLM, 에이전트, 프롬프트]
sources: []
---

# AI — 도메인 인덱스

AI/LLM, 에이전트, 프롬프트 엔지니어링, AI 제품 관련 모든 페이지의 진입점.
**원칙 → 프레임워크 → 사례 → 엔티티** 순으로 읽는다.

---

## 핵심 원칙 (최우선 참조)

- [Generator-Evaluator 루프](../principles/generator-evaluator-loop.md) — 생성자와 평가자를 분리하면 반복 피드백으로 품질이 향상된다
- [LLM Wiki 패턴](../principles/llm-wiki-pattern.md) — LLM이 유지보수 비용을 대신 처리함으로써 지식이 구조화된 형태로 축적된다

---

## 프레임워크 / 개념

- [에이전트 하니스 (Agent Harness)](../concepts/agent-harness.md) — 에이전트 조율 구조의 설계 패턴
- [Managed Agents](../concepts/managed-agents.md) — Anthropic의 뇌(오케스트레이터)와 손(서브에이전트) 분리 패턴
- [에이전트 Eval 방법론](../concepts/agentic-evals.md) — 에이전트 성능 평가의 인프라 노이즈 문제와 방법론
- [Claude Code](../concepts/claude-code.md) — Anthropic의 CLI 코딩 에이전트 개요
- [음성 기반 AI](../concepts/voice-based-ai.md) — Voice-first AI 트렌드와 기술 스택

---

## 사례 / 분석 (출처 기반)

- [Anthropic 하니스 엔지니어링](../topics/anthropic-harness-engineering.md) — 장기 실행 앱 설계, Generator-Evaluator 실전 사례
- [Anthropic Managed Agents](../topics/anthropic-managed-agents.md) — Managed Agents 아키텍처 상세
- [Anthropic: Eval 인프라 노이즈 정량화](../topics/anthropic-infrastructure-noise.md) — Terminal-Bench 기반 노이즈 측정 연구
- [Claude Code 세션 관리와 1M 컨텍스트](../topics/claude-code-session-management.md) — 긴 세션의 컨텍스트 관리 전략
- [The Batch Issue 347 요약](../topics/the-batch-issue-347.md) — 2026년 AI 뉴스 스냅샷

---

## 비교

- [RAG vs LLM Wiki 패턴](../comparisons/rag-vs-llm-wiki.md) — 질의 시 검색 vs 수집 시 통합의 트레이드오프

---

## 관련 인물 / 조직

- [Anthropic](../entities/anthropic.md)
- [Andrej Karpathy](../entities/andrej-karpathy.md)
- [Andrew Ng](../entities/andrew-ng.md)
- [OpenAI](../entities/openai.md)
- [Google DeepMind](../entities/google-deepmind.md)
- [World Labs](../entities/world-labs.md)
