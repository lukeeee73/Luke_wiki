---
title: "RAG vs LLM Wiki 패턴"
created: 2026-04-05
updated: 2026-04-05
domain: ai
type: framework
weight: important
confidence: high
tags: [비교, RAG, LLM, 지식관리]
sources: [sources/karpathy-llm-wiki-pattern.md]
---

# RAG vs LLM Wiki 패턴

두 접근법 모두 LLM과 외부 지식을 결합하지만, 근본적인 차이가 있다.

## 비교

| 항목 | RAG | LLM Wiki |
|------|-----|----------|
| **처리 시점** | 질의 시점 (query time) | 수집 시점 (ingest time) |
| **지식 형태** | 원본 청크 그대로 | 구조화된 요약 + 교차 참조 |
| **유지보수** | 인덱스 자동 관리 | LLM이 위키 전체 유지보수 |
| **모순 처리** | 없음 | 명시적 모순 기록 |
| **지식 축적** | 검색 품질에 의존 | 점진적 통합 및 축적 |
| **투명성** | 낮음 (블랙박스 검색) | 높음 (읽을 수 있는 마크다운) |

## 각각의 장점

### RAG의 장점
- 설정이 간단하고 즉시 사용 가능
- 원본 데이터의 최신성 유지
- 대규모 문서에 효율적

### LLM Wiki의 장점
- 지식이 구조화되어 축적됨
- 교차 참조와 종합 분석 가능
- 모순과 정보 공백을 명시적으로 추적
- 인간이 직접 위키를 읽고 탐색 가능

## 관련 페이지

- [LLM Wiki 패턴](../principles/llm-wiki-pattern.md)
