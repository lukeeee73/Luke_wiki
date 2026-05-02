---
title: "디자인 시스템"
created: 2026-04-18
updated: 2026-04-18
domain: design
type: framework
weight: important
confidence: high
tags: [design, design-system, ui-ux, fundamentals]
sources: [sources/design-process-basics.md]
---

# 디자인 시스템 (Design System)

재사용 가능한 디자인 요소의 **표준화 체계**. 경제학의 표준화된 통계 지표 체계(GDP 산정 방식 등)에 대응한다 — 개별 판단을 줄이고 호환성·비교 가능성을 확보하기 위한 공통 언어.

## 3가지 구성 요소

### 1. Design Tokens
`primary-500`, `spacing-4`, `radius-md` 같은 **변수**. CSS 변수와 1:1로 대응한다.

- 색상 토큰: `color-primary-500`, `color-neutral-100`
- 간격 토큰: `spacing-4`, `spacing-8` (보통 4px/8px 배수)
- 타이포 토큰: `font-size-body`, `line-height-heading`
- 반경 토큰: `radius-sm`, `radius-md`

토큰이 한 곳에서 바뀌면 전 제품에 반영된다. 브랜드 리뉴얼이 수백 화면 수정이 아니라 토큰 테이블 수정으로 끝나는 이유.

### 2. Components
버튼·입력창·카드 등 **조립식 부품**. 토큰을 조합해 만든다.

- 원자 수준: Button, Input, Badge
- 복합 수준: SearchBar (Input + Button), Card (Image + Text + Button)

### 3. Guidelines
언제 어떤 컴포넌트를 써야 하는지에 대한 **규칙**.

- "Primary Button은 화면당 하나만"
- "Error 메시지는 Semantic red-500 사용"
- "Modal은 치명적 결정에만"

컴포넌트만 있고 가이드라인이 없으면 일관성이 무너진다.

## 대표 사례

| 회사 | 시스템 |
|---|---|
| Google | Material Design |
| Apple | Human Interface Guidelines (HIG) |
| Shopify | Polaris |
| IBM | Carbon |
| Atlassian | Atlassian Design System |

## 효과

- **일관성**: 화면마다 다른 디자인을 방지
- **속도**: 매번 처음부터 만들지 않음
- **협업**: 디자이너·개발자가 같은 단어로 대화
- **유지보수**: 중앙에서 바꾸면 전 제품에 반영

## 관련 페이지

- [디자인 프로세스 기초](../topics/design-process-basics.md)
- [Atomic Design](atomic-design.md) — 디자인 시스템을 조직하는 멘탈 모델
