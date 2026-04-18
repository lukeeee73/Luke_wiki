---
title: "디자인 프로세스 기초 — 디자이너와 PM의 협업 방식"
aliases: [디자인 기초, UI/UX 용어, 디자인 워크플로우]
tags: [design, ui-ux, product-management, fundamentals]
created: 2026-04-18
updated: 2026-04-18
status: reference
related: [Claude-Design, Figma-MCP, PRD-작성법]
---

# 디자인 프로세스 기초

> Claude Design 같은 AI 디자인 도구를 제대로 활용하기 위한 선행 지식.
> 디자이너·PM이 실제로 어떻게 일하는지, 왜 그렇게 생각하는지를 이해한다.

## TL;DR

- 디자인은 **Discovery → Define → Design → Deliver** 흐름을 따른다
- PM은 "무엇을·왜", 디자이너는 "어떻게 보여주고 쓰게 할지"를 담당한다
- 실제 작업은 **Research → Flow → Wireframe → Mockup → Prototype → Handoff** 순서로 진행된다
- 디자인 시스템(토큰·컴포넌트·가이드라인)이 재사용성과 일관성의 핵심이다
- AI 도구는 와이어프레임~프로토타입 구간을 압축하지만, **판단은 여전히 사람의 몫**이다

---

## 1. 전체 프로세스 흐름

### 4단계 매크로 구조

```
Discovery(발견) → Define(정의) → Design(설계) → Deliver(전달)
```

경제학의 "문제 정의 → 모델링 → 실증 → 정책 제언" 흐름과 구조적으로 동일하다.
문제를 잘못 정의하면 뒤의 모든 작업이 무의미해지는 것도 같다.

### 역할 분담

| 역할 | 담당 | 산출물 |
|---|---|---|
| PM | 무엇을·왜 만들 것인가 | PRD (Product Requirements Document) |
| 디자이너 | 어떻게 보여주고 쓰게 할 것인가 | Wireframe, Mockup, Prototype |
| 개발자 | 어떻게 구현할 것인가 | 실제 코드 |

PRD는 경제학자의 정책 보고서와 유사한 구조를 가진다:
"현 상황 → 문제 → 해결 방안 → 성공 지표".

---

## 2. 디자인 실무 7단계

### (1) User Research — 사용자 조사

- 인터뷰·설문·행동 관찰로 니즈 파악
- 경제학의 설문 기반 실증 연구에 대응
- 산출물: **Persona**(가상의 대표 사용자 프로필)

### (2) User Journey & User Flow

- **User Journey**: 제품을 만나기 전부터 사용 후까지의 감정·행동 전체 여정 (거시)
- **User Flow**: 특정 작업 완료까지의 화면 간 이동 경로 (미시)
- 경제학 비유: Journey는 생애주기 소비 패턴, Flow는 개별 거래의 의사결정 트리

### (3) Information Architecture (IA)

- 정보의 분류·계층 구조 설계
- 도서관 분류 체계와 동일한 개념
- 메뉴 구조·카테고리 위계가 여기서 확정됨

### (4) Wireframe — 와이어프레임

- 색·폰트·이미지 없는 **흑백 뼈대 레이아웃**
- "여기에 제목, 여기에 버튼, 여기에 리스트"만 표시
- 건축 도면에 해당. 이 단계에서 구조를 확정해야 이후 수정 비용이 줄어든다

### (5) Mockup — 목업

- 와이어프레임에 색·폰트·이미지를 입힌 **정적 시안**
- 실제 화면처럼 보이지만 상호작용은 없음

### (6) Prototype — 프로토타입

- 목업을 연결해 실제로 클릭·이동이 가능한 **인터랙티브 버전**
- Figma의 핵심 기능
- 사용자 테스트에 활용

### (7) Design System & Handoff

- 완성된 디자인을 개발자에게 전달
- 이때 디자인 시스템이 결정적 역할

---

## 3. 핵심 용어 사전

### UI vs UX

- **UI (User Interface)**: 눈에 보이는 것 — 버튼 색, 폰트, 레이아웃
- **UX (User Experience)**: 쓰면서 느끼는 것 — 편의성, 스트레스 여부
- UI ⊂ UX

### Design System — 디자인 시스템

재사용 가능한 디자인 요소의 표준화 체계.
경제학의 표준화된 통계 지표 체계(GDP 산정 방식 등)에 대응.

구성:

- **Design Tokens**: `primary-500`, `spacing-4` 같은 변수. CSS 변수와 1:1 대응
- **Components**: 버튼·입력창·카드 등 조립식 부품
- **Guidelines**: 언제 어떤 컴포넌트를 쓰는지에 대한 규칙

대표 사례:

- Google — Material Design
- Apple — Human Interface Guidelines
- Shopify — Polaris

### Atomic Design — 원자적 디자인

Brad Frost의 방법론. 화학 비유 기반:

| 계층 | 대응 |
|---|---|
| Atoms | 버튼, 라벨 등 최소 단위 |
| Molecules | 검색창 (입력창 + 버튼) |
| Organisms | 헤더 (로고 + 메뉴 + 검색창) |
| Templates | 페이지 레이아웃 |
| Pages | 실제 콘텐츠가 담긴 최종 화면 |

### Grid System — 그리드

- 보이지 않는 격자로 화면을 분할해 요소를 정렬
- 통상 **12 컬럼 그리드** 사용
- 신문 레이아웃과 동일한 원리

### Typography — 타이포그래피

- **Font family**: 폰트 종류 (Pretendard, Inter 등)
- **Font weight**: 굵기 (300 / 400 / 500 / 700)
- **Line height**: 줄 간격 (본문 기준 1.5배)
- **Typographic scale**: 크기 비율 체계 (예: 12 / 14 / 16 / 20 / 24 / 32px)

### Spacing System — 간격 체계

- 4px 또는 8px의 배수만 사용 (4, 8, 12, 16, 24, 32…)
- "8-point grid"라 부름
- 이유: 다양한 해상도에서 깨지지 않고, 시각적 리듬이 생김

### Color Palette

- **Primary**: 브랜드 핵심 색
- **Secondary**: 보조 색
- **Neutral**: 회색 계열 (글자·테두리)
- **Semantic**: 의미 부여된 색 — success / warning / error / info

### Hierarchy — 시각적 위계

- 크기·색 대비·여백으로 시선 순서를 설계
- 신문 1면의 헤드라인이 큰 이유와 동일

### White Space / Negative Space

- 의도적으로 비워둔 공간
- 비움 자체가 디자인이라는 철학 — Apple의 핵심

### Affordance — 행동유도성

- "이건 누를 수 있겠다"는 시각적 단서
- 버튼의 그림자, 입력창의 테두리 등
- Don Norman 『디자인과 인간 심리』의 핵심 개념

### Accessibility (A11y) — 접근성

- 색맹·시각장애인·키보드 사용자까지 포괄하는 설계
- 국제 표준: **WCAG** (Web Content Accessibility Guidelines)
- 주요 요소: 색 대비비율 4.5:1 이상, alt text, 키보드 내비게이션

### Responsive Design — 반응형

- 화면 크기에 따라 레이아웃이 자동 변경
- **Breakpoint** 기준: 640px / 768px / 1024px / 1280px

### State — 상태

하나의 요소가 가질 수 있는 여러 모습. 버튼의 경우:

- Default (기본)
- Hover (마우스 올림)
- Active / Pressed (눌림)
- Disabled (비활성)
- Loading (로딩 중)
- Focus (키보드 포커스)

모든 상태를 빠짐없이 설계하는 것이 프로의 기본.

---

## 4. 주요 도구

| 도구 | 용도 |
|---|---|
| Figma | 디자인·프로토타이핑·협업의 실질적 표준 |
| Notion / Confluence | PRD 작성 |
| Miro / FigJam | 아이디어 정리, 유저 플로우 스케치 |
| Jira / Linear | 작업 관리, 개발자와의 연결 |

---

## 5. AI 디자인 도구의 위치

기존 워크플로우에서 AI가 파고드는 지점은 **와이어프레임 → 목업 → 프로토타입** 구간이다.
특히 "빠르게 여러 시안을 보고 싶다"는 니즈를 타겟한다.
기존에 며칠 걸리던 작업을 분 단위로 단축.

단, 다음은 여전히 사람의 영역:

- 문제 정의의 타당성
- 사용자 관점의 적절성 판단
- 비즈니스 목표와의 정합성

경제학에서 모델이 결과를 산출해도 해석은 사람이 하는 것과 동일한 구조.

---

## 관련 문서

- Claude-Design — Claude의 디자인 생성 기능
- Figma-MCP — Figma와 Claude 연동
- PRD-작성법 — 제품 요구사항 문서 템플릿
- Design-Tokens — 디자인 토큰 심화
- WCAG-가이드 — 접근성 표준

## 참고 자료

- Brad Frost, *Atomic Design*
- Don Norman, 『디자인과 인간 심리』
- Material Design Guidelines (Google)
- Human Interface Guidelines (Apple)
- WCAG 2.1 (W3C)
