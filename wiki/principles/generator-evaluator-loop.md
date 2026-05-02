---
title: "Generator-Evaluator 루프"
created: 2026-04-05
updated: 2026-05-02
domain: ai
type: principle
weight: foundational
confidence: high
tags: [generator-evaluator, GAN, multi-agent, feedback-loop, quality-improvement, 원칙]
sources: [sources/anthropic-harness-design-long-running-apps.md]
---

# Generator-Evaluator 루프

> [!principle] 핵심 원칙
> 단일 에이전트가 생성과 평가를 동시에 수행하면 자기 편향(self-bias)에 빠진다. 생성자와 평가자를 분리하면 대립적 피드백 구조가 생겨 결과물 품질이 반복적으로 향상된다.

## 정의

Generator-Evaluator 루프는 두 에이전트(또는 두 역할)가 대립적 피드백 구조를 형성하여 결과물 품질을 반복적으로 향상시키는 멀티 에이전트 패턴이다.

## GAN과의 유사성

Generative Adversarial Networks(GAN)에서 영감:
- **GAN**: Generator(생성자)와 Discriminator(판별자)가 경쟁하며 생성 품질 향상
- **에이전트 루프**: Generator(생성 에이전트)와 Evaluator(평가 에이전트)가 협력/경쟁하며 출력 품질 향상

차이점: GAN은 동시 학습(adversarial training)이지만, 에이전트 루프는 순차적 반복(iterative refinement)이다.

## 구조

```
입력 (프롬프트/명세)
      ↓
 [Generator]
  결과물 생성
      ↓
 [Evaluator]
  결과물 평가
  개선 사항 도출
      ↓
 기준 충족?
  Yes → 완료
  No  → Generator로 피드백 전달 (반복)
```

## Evaluator 설계의 핵심

> [!principle] 원칙
> Evaluator는 **검증 가능한 기준**으로 평가해야 한다. 모호한 기준은 일관성 없는 피드백을 낳고, 루프가 수렴하지 않는다.

Anthropic의 프론트엔드 디자인 평가 사례:

| 모호한 기준 | 검증 가능한 기준 |
|-------------|-----------------|
| "아름답다" | 5가지 디자인 원칙 준수 여부 (0-5점) |
| "창의적이다" | AI 슬롭(generic gradients, predictable layout) 부재 (0-3점) |
| "잘 작동한다" | Playwright로 UI/API/DB 직접 테스트 |

## 실전 평가 방법: Playwright MCP 활용

Anthropic Evaluator의 혁신: **정적 코드 리뷰 대신 동적 앱 테스트**

- Playwright MCP로 실제 실행 중인 앱을 사용자처럼 조작
- UI 버튼 클릭, 폼 제출, 네비게이션 테스트
- API 엔드포인트 호출 및 응답 검증
- 데이터베이스 상태 확인

> [!fact] 사실
> Anthropic 사례(Opus 4.5 기반 3-에이전트 하니스): 일반적으로 5-15번 반복, 최대 4시간 소요. Solo 에이전트 대비 시간 18배, 비용 22배 증가 → 완성도와 UX에서 큰 차이.

## 소프트웨어 개발과의 매핑

Generator-Evaluator 루프는 기존 소프트웨어 개발 생명주기에 자연스럽게 매핑된다:

| 루프 역할 | 소프트웨어 역할 |
|-----------|----------------|
| Generator | 개발자 (구현) |
| Evaluator | QA 엔지니어 + 코드 리뷰어 |
| 반복 | 스프린트 사이클 |
| 완료 기준 | 인수 기준 (Acceptance Criteria) |

## 적용 분야

- 프론트엔드 UI 디자인 및 구현
- 풀스택 애플리케이션 개발
- 코드 품질 개선
- 콘텐츠 생성 (글쓰기, 번역 등)

## 관련 페이지

- [에이전트 하니스](../concepts/agent-harness.md)
- [Anthropic 하니스 엔지니어링](../topics/anthropic-harness-engineering.md)
