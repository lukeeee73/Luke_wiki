---
title: "Atomic Design"
created: 2026-04-18
updated: 2026-04-18
domain: design
type: framework
weight: important
confidence: high
tags: [design, design-system, methodology, brad-frost]
sources: [sources/design-process-basics.md]
---

# Atomic Design (원자적 디자인)

Brad Frost가 제안한 **화학 비유 기반** 디자인 시스템 방법론. UI를 5개의 계층으로 분해해 조합·재사용 가능한 구조로 만든다.

## 5계층 구조

| 계층 | 정의 | 예시 |
|---|---|---|
| **Atoms** (원자) | 더 이상 쪼갤 수 없는 최소 단위 | 버튼, 라벨, 입력 필드, 아이콘 |
| **Molecules** (분자) | Atom의 작은 조합 | 검색창 (입력창 + 버튼) |
| **Organisms** (유기체) | Molecule·Atom의 복합 블록 | 헤더 (로고 + 메뉴 + 검색창) |
| **Templates** (템플릿) | 콘텐츠 없는 페이지 레이아웃 | 상품 상세 페이지 뼈대 |
| **Pages** (페이지) | 실제 콘텐츠가 담긴 최종 화면 | "아이폰 15 Pro" 상품 페이지 |

## 핵심 아이디어

### 구성 가능성 (Composability)
작은 단위를 조합해 큰 단위를 만든다. 같은 Atom(Button)이 여러 Molecule(SearchBar, Form)에 재사용된다.

### 추상화의 연속성
Templates까지는 **추상**, Pages부터는 **구체**. 이 경계가 재사용성의 분기점이다.

### [디자인 시스템](design-system.md)과의 관계
Atomic Design은 디자인 시스템을 **어떻게 조직할지**에 대한 방법론이다. Design Tokens가 Atom 이전의 원료(색·간격·폰트)라면, Atoms부터가 조립 가능한 부품이다.

## 실전 활용

- Figma의 Component / Variant 구조가 Atoms~Organisms를 모델링하기 위해 설계됨
- React / Vue 같은 컴포넌트 프레임워크와 자연스럽게 대응
- 스토리북(Storybook) 같은 도구는 계층별 독립 렌더링을 지원

## 한계

- 모든 UI가 깔끔하게 5계층으로 분해되지는 않음
- Molecule과 Organism의 경계가 모호할 때가 많음
- 레이아웃(Template)과 페이지 상태(Page)의 구분이 실무에서 흐려짐

## 관련 페이지

- [디자인 시스템](design-system.md)
- [디자인 프로세스 기초](../topics/design-process-basics.md)

## 참고 자료

- Brad Frost, *Atomic Design* (bradfrost.com/blog/post/atomic-web-design)
