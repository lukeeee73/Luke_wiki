---
title: "디자인 프로세스 기초"
created: 2026-04-18
updated: 2026-04-18
domain: design
type: fact-set
weight: important
confidence: high
tags: [design, ui-ux, product-management, fundamentals, workflow]
sources: [sources/design-process-basics.md]
---

# 디자인 프로세스 기초

Claude Design 같은 AI 디자인 도구를 제대로 활용하기 위한 선행 지식. 디자이너와 PM이 실제로 어떻게 일하는지, 왜 그렇게 생각하는지를 이해하면 AI 산출물의 품질을 평가할 수 있는 기준이 생긴다.

## 핵심 테제

- 디자인은 **Discovery → Define → Design → Deliver** 4단계 매크로 흐름을 따른다
- PM은 "무엇을·왜", 디자이너는 "어떻게 보여주고 쓰게 할지"를 담당한다
- 실제 작업은 **Research → Flow → Wireframe → Mockup → Prototype → Handoff** 순서로 세분화된다
- 디자인 시스템(토큰·컴포넌트·가이드라인)이 재사용성과 일관성의 핵심이다
- AI 도구는 와이어프레임~프로토타입 구간을 압축하지만, **판단은 여전히 사람의 몫**

## 1. 매크로 프로세스: 4D 모델

```
Discovery(발견) → Define(정의) → Design(설계) → Deliver(전달)
```

경제학의 "문제 정의 → 모델링 → 실증 → 정책 제언" 흐름과 구조적으로 동일하다. 문제를 잘못 정의하면 뒤의 모든 작업이 무의미해지는 것도 같다.

### 역할 분담

| 역할 | 담당 | 산출물 |
|---|---|---|
| PM | 무엇을·왜 만들 것인가 | PRD (Product Requirements Document) |
| 디자이너 | 어떻게 보여주고 쓰게 할 것인가 | Wireframe, Mockup, Prototype |
| 개발자 | 어떻게 구현할 것인가 | 실제 코드 |

PRD는 경제학자의 정책 보고서와 유사한 구조를 가진다 — "현 상황 → 문제 → 해결 방안 → 성공 지표".

## 2. 디자인 실무 7단계

| 단계 | 목적 | 비유 |
|---|---|---|
| (1) User Research | 인터뷰·설문·관찰로 니즈 파악. Persona 도출 | 설문 기반 실증 연구 |
| (2) User Journey & Flow | 거시(Journey)와 미시(Flow) 경로 설계 | 생애주기 vs 개별 의사결정 트리 |
| (3) Information Architecture | 정보의 분류·계층 구조 설계 | 도서관 분류 체계 |
| (4) Wireframe | 흑백 뼈대 레이아웃 | 건축 도면 |
| (5) Mockup | 색·폰트·이미지를 입힌 정적 시안 | 모델 하우스 사진 |
| (6) Prototype | 클릭·이동이 가능한 인터랙티브 버전 | 모델 하우스 견학 |
| (7) Handoff | 개발자 전달 — 디자인 시스템 기반 | 시공 도면 인도 |

**수정 비용 곡선**: 뒤로 갈수록 수정 비용이 기하급수적으로 증가한다. Wireframe 단계에서 구조를 확정하는 것이 중요한 이유.

## 3. 핵심 개념 묶음

### UI vs UX
- **UI**: 눈에 보이는 것 (버튼 색, 폰트, 레이아웃)
- **UX**: 쓰면서 느끼는 것 (편의성, 스트레스 여부)
- UI ⊂ UX

### [디자인 시스템](../concepts/design-system.md)
재사용 가능한 디자인 요소의 표준화 체계. Design Tokens + Components + Guidelines의 3요소. Material Design, Apple HIG, Shopify Polaris가 대표 사례.

### [Atomic Design](../concepts/atomic-design.md)
Brad Frost의 방법론. Atoms → Molecules → Organisms → Templates → Pages 5계층. 디자인 시스템을 조직화하는 가장 일반적인 멘탈 모델.

### 시각 체계 (Typography / Spacing / Color)
- **Typography**: Font family, weight, line-height, typographic scale
- **Spacing**: 4px 또는 8px 배수만 사용 ("8-point grid") — 해상도 독립성과 시각적 리듬 확보
- **Color**: Primary / Secondary / Neutral / Semantic(success·warning·error·info)

### Hierarchy & White Space
크기·대비·여백으로 시선 순서를 설계. 비움 자체가 디자인 — Apple의 핵심 철학.

### Affordance
"이건 누를 수 있겠다"는 시각적 단서. Don Norman 『디자인과 인간 심리』의 핵심 개념.

### Accessibility (A11y)
WCAG 2.1 표준. 색 대비 4.5:1 이상, alt text, 키보드 내비게이션. 법적 요구사항이 늘어나고 있음.

### Responsive & State
- **Responsive**: Breakpoint (640/768/1024/1280px)에 따른 자동 레이아웃
- **State**: Default / Hover / Active / Disabled / Loading / Focus — 버튼 하나가 6개 상태를 가진다. 모든 상태를 설계하는 것이 프로의 기본

## 4. 도구 생태계

| 도구 | 용도 |
|---|---|
| Figma | 디자인·프로토타이핑·협업의 실질적 표준 |
| Notion / Confluence | PRD 작성 |
| Miro / FigJam | 아이디어 정리, 유저 플로우 스케치 |
| Jira / Linear | 작업 관리, 개발자 연결 |

## 5. AI 디자인 도구가 파고드는 지점

기존 워크플로우에서 AI가 압축하는 구간은 **Wireframe → Mockup → Prototype**. "빠르게 여러 시안을 보고 싶다"는 니즈가 타겟이다. 며칠 걸리던 작업이 분 단위로 단축된다.

반면 **여전히 사람의 영역**:

- 문제 정의의 타당성 (Discovery·Define)
- 사용자 관점의 적절성 판단
- 비즈니스 목표와의 정합성

경제학에서 모델이 결과를 산출해도 해석은 사람이 하는 것과 동일한 구조. AI는 생성기, 사람은 평가기 — [Generator-Evaluator 루프](../principles/generator-evaluator-loop.md)의 또 다른 인스턴스로 볼 수 있다.

## 관련 페이지

- [디자인 시스템](../concepts/design-system.md) — 토큰·컴포넌트·가이드라인 심화
- [Atomic Design](../concepts/atomic-design.md) — Brad Frost의 5계층 방법론
- [Generator-Evaluator 루프](../principles/generator-evaluator-loop.md) — AI 생성과 사람 평가의 역할 분리

## 참고 자료

- Brad Frost, *Atomic Design*
- Don Norman, 『디자인과 인간 심리』
- Material Design Guidelines (Google)
- Human Interface Guidelines (Apple)
- WCAG 2.1 (W3C)
