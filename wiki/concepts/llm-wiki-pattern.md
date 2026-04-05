---
title: "LLM Wiki 패턴"
created: 2026-04-05
updated: 2026-04-05
tags: [LLM, 지식관리, 위키, 패턴]
sources: [sources/karpathy-llm-wiki-pattern.md]
---

# LLM Wiki 패턴

LLM을 활용하여 개인 지식 베이스를 점진적으로 구축하고 유지 관리하는 패턴.

## 핵심 개념

기존 RAG(Retrieval-Augmented Generation)가 질의 시점에 관련 청크를 검색하는 것과 달리, LLM Wiki 패턴은 **자료를 수집하는 시점에** LLM이 적극적으로 읽고, 핵심 정보를 추출하고, 기존 위키에 통합한다.

이를 통해 지식이 흩어지지 않고 **구조화된 형태로 축적**된다.

## 3계층 구조

| 계층 | 역할 | 소유자 |
|------|------|--------|
| Raw Sources | 원본 자료 (불변) | 인간 |
| Wiki | 구조화된 마크다운 페이지 | LLM |
| Schema | 운영 규칙 및 구조 정의 | 인간 + LLM |

## 핵심 작업

- **Ingest**: 새 자료 → 읽기 → 요약 → 관련 페이지 업데이트 → 인덱스/로그 갱신
- **Query**: 질문 → 관련 페이지 검색 → 출처 기반 답변 종합
- **Lint**: 주기적 정합성 검사 (모순, 오래된 정보, 고아 페이지 등)

## 효과

인간이 위키를 포기하는 주된 이유인 **유지보수 부담**(교차 참조, 요약 최신화, 일관성 유지)을 LLM이 대신 처리한다.

## 관련 페이지

- [RAG vs LLM Wiki](../comparisons/rag-vs-llm-wiki.md)
- [Andrej Karpathy](../entities/andrej-karpathy.md)
