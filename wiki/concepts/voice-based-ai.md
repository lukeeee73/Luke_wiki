---
title: "음성 기반 AI (Voice-based AI)"
created: 2026-04-05
updated: 2026-04-05
tags: [voice-AI, voice-UI, foundation-models, Andrew-Ng, latency, STT, TTS]
sources: [sources/the-batch-issue-347.md]
---

# 음성 기반 AI (Voice-based AI)

음성을 통해 사용자와 상호작용하는 AI 시스템. Andrew Ng은 The Batch Issue 347에서 음성 UI의 급속한 발전과 보편화 가능성을 강조했다.

## Andrew Ng의 관점 (2026-04)

> "음성 기반 AI가 빠르게 발전하고 있으나, 대부분의 사람들은 음성 UI가 얼마나 보편화될지 아직 인식하지 못한다."

마우스가 포인트-앤-클릭 앱을, 터치/스와이프가 모바일 앱을 열었듯이, **음성은 전혀 새로운 종류의 애플리케이션**을 열 것이라고 주장한다.

## 두 가지 아키텍처 접근법

| 방식 | 구성 | 장점 | 단점 |
|------|------|------|------|
| **엔드-투-엔드** | 음성 입력/출력 통합 모델 | 낮은 지연 | 제어 어려움, 신뢰성 낮음 |
| **파이프라인** | STT → LLM/에이전트 AI → TTS | 높은 신뢰성 | 과도한 지연 |

## 지연(Latency) 문제와 해결

- 자연스러운 인간 대화 지연: **약 0.3~1초**
- DeepLearning.AI, RealAvatar 등의 팀이 파이프라인 지연을 **~0.5~1초** 수준으로 단축 성공
- 기술: 전체 응답이 준비되기 전에 빠른 "사전 응답(pre-response)"을 먼저 생성하여 사용자 확인

## 개발 접근성

Andrew Ng은 **Claude Code**를 사용하여 수학 퀴즈 앱에 음성 기능을 1시간 이내에 추가한 사례를 언급하며, 음성 개발이 얼마나 접근하기 쉬워졌는지를 보여줬다.

## 주목 기업

### Vocal Bridge
- AI Fund 포트폴리오 기업
- CEO/창업자: **Ashwyn Sharma** (AI Dev 26 연사)
- 개발자들이 음성 UI를 통합할 수 있도록 하는 개발자 도구 구축

## 관련 페이지

- [Andrew Ng](../entities/andrew-ng.md)
- [The Batch Issue 347](../topics/the-batch-issue-347.md)
