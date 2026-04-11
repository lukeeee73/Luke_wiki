---
title: "Generator-Evaluator 루프를 모바일/웹 Claude 환경에서 웹 디자인에 적용하기"
created: 2026-04-11
updated: 2026-04-11
tags: [generator-evaluator, web-design, claude-code, mobile, workflow, synthesis]
sources: [wiki/concepts/generator-evaluator-loop.md, wiki/topics/anthropic-harness-engineering.md, wiki/concepts/agent-harness.md]
---

# Generator-Evaluator 루프를 모바일/웹 Claude 환경에서 웹 디자인에 적용하기

## 문제 정의

Anthropic의 [Generator-Evaluator 루프](../concepts/generator-evaluator-loop.md)는 Playwright MCP로 실행 중인 앱을 직접 조작하는 자동화된 평가를 핵심으로 한다. 그러나 **모바일 Claude Code + 웹 Claude**라는 제약된 환경에서는 Playwright 같은 자동화 도구를 쓸 수 없다.

이 문서는 그 격차를 어떻게 메울 수 있는지를 다룬다.

---

## 핵심 제약과 자산

### 가용 자산

| 도구 | 할 수 있는 것 | 못 하는 것 |
|------|-------------|-----------|
| **모바일 Claude Code** | 코드 생성/편집, git 조작, CLI 명령 실행, 파일 읽기/쓰기 | GUI 브라우저 조작, 스크린샷 캡처 |
| **웹 Claude** | 장문 대화, 이미지 분석(스크린샷 평가), 구조화된 계획 수립 | 코드 실행, 파일 시스템 접근 |
| **사용자(나)** | 브라우저로 앱 확인, 스크린샷 촬영, 두 도구 사이의 피드백 전달 | (시간과 에너지가 한정적) |

### 핵심 격차: 자동화된 평가가 없다

Anthropic 하니스에서 Evaluator는 Playwright로 **코드를 보지 않고 실행 중인 앱을 직접 테스트**했다. 우리 환경에서는 **사용자가 이 다리 역할**을 해야 한다.

---

## 적용 아키텍처: Human-Bridged Generator-Evaluator

```
[웹 Claude: Planner]
  raw 아이디어 → 상세 명세 + 평가 루브릭
          ↓
[모바일 Claude Code: Generator] ←─────────────┐
  코드 생성 → git push → deploy preview       │
          ↓                                     │
[사용자: Bridge]                                 │
  배포된 앱 확인, 스크린샷 촬영                  │
          ↓                                     │
[웹 Claude: Evaluator]                           │
  스크린샷 기반 평가, 구체적 피드백 생성 ────────┘
          ↓ (기준 충족 시)
[완성된 웹 디자인]
```

Anthropic의 3-에이전트 구조에서 **Planner와 Evaluator를 웹 Claude가**, **Generator를 모바일 Claude Code가**, 그리고 **Playwright의 역할을 사용자가** 담당한다.

---

## 단계별 워크플로우

### Phase 1: Planning (웹 Claude)

웹 Claude에서 대화를 통해 다음을 생성한다:

**1. 제품 명세서**
```
프로젝트: [이름]
목적: [한 문장]
타겟 사용자: [누구]
핵심 페이지/기능:
  1. ...
  2. ...
기술 스택: [HTML/CSS/JS, React, etc.]
배포 방식: [GitHub Pages, Vercel, Netlify]
```

**2. 평가 루브릭 (이것이 핵심)**

"아름답다"가 아니라, 검증 가능한 기준으로 분해한다:

| 기준 | 측정 방법 | 합격 기준 |
|------|-----------|----------|
| **레이아웃** | 시각적 위계, 그리드 정렬 | 명확한 3단계 이상의 위계 |
| **타이포그래피** | 폰트 크기 체계, 가독성 | 본문 16px 이상, 제목 차등 |
| **색상** | 컬러 팔레트 일관성, 대비 | WCAG AA 충족 (4.5:1 이상) |
| **반응형** | 모바일/데스크톱 레이아웃 | 양쪽 모두 깨지지 않음 |
| **AI 슬롭 부재** | 뻔한 그라데이션, 스톡 느낌 | 고유한 디자인 아이덴티티 존재 |
| **기능 작동** | 클릭, 네비게이션, 폼 | 핵심 경로 모두 작동 |

> **추론**: Anthropic 위키에서 강조하듯, Evaluator의 품질은 기준의 구체성에 비례한다. 루브릭이 모호하면 피드백도 모호해진다.

**3. 스프린트 단위 분해**

한 번에 전체를 만들지 않는다. Generator가 context를 소진하지 않도록 작은 단위로 나눈다:

```
Sprint 1: HTML 구조 + 기본 레이아웃
Sprint 2: 타이포그래피 + 색상 시스템
Sprint 3: 반응형 처리
Sprint 4: 인터랙션 + 애니메이션
Sprint 5: 폴리싱 + 엣지 케이스
```

### Phase 2: Generation (모바일 Claude Code)

Planning에서 나온 명세와 현재 스프린트 목표를 Claude Code에 전달한다.

**프롬프트 템플릿:**
```
다음 명세에 따라 [Sprint N] 구현해줘.

[명세 붙여넣기]

현재 스프린트 목표:
- [구체적 목표 1]
- [구체적 목표 2]

이전 평가 피드백: (첫 스프린트면 생략)
- [피드백 1]
- [피드백 2]

완료되면 commit하고 push해줘.
```

**배포 자동화 설정 (한 번만):**
- **GitHub Pages**: 가장 간단. `git push`만 하면 자동 배포
- **Vercel/Netlify**: GitHub 연동 설정 후 push마다 preview URL 생성
- 이 설정은 첫 세션에서 Claude Code로 처리 가능

### Phase 3: Evaluation (사용자 + 웹 Claude)

**사용자가 하는 일 (Bridge 역할):**
1. 배포된 URL을 브라우저에서 연다
2. **데스크톱 뷰** 스크린샷 1-2장
3. **모바일 뷰** 스크린샷 1-2장 (브라우저 개발자 도구 또는 실제 모바일)
4. **주요 인터랙션** 직접 테스트 (버튼 클릭, 네비게이션 등)

**웹 Claude에게 전달:**
```
Phase 1에서 만든 평가 루브릭 기준으로 이 스크린샷들을 평가해줘.

[스크린샷 첨부]

현재 스프린트 목표: [목표]
평가 루브릭: [루브릭 붙여넣기 또는 참조]

각 기준별로 점수와 구체적인 개선 사항을 알려줘.
기준 충족 여부도 판단해줘.
```

**웹 Claude의 평가 출력 형식:**
```
## 평가 결과 (Sprint N)

| 기준 | 점수 | 상태 | 비고 |
|------|------|------|------|
| 레이아웃 | 4/5 | ✅ | 히어로 섹션 위계 명확 |
| 타이포그래피 | 2/5 | ❌ | 본문 14px, 제목 차등 부족 |
| ... | ... | ... | ... |

## 다음 반복에서 수정할 사항 (우선순위순)
1. 본문 폰트 16px로 변경, h1/h2/h3 명확한 크기 차등
2. ...

## 기준 충족 여부: ❌ (2개 미달)
```

### Phase 4: Iteration

평가 결과를 다시 모바일 Claude Code에 전달 → 수정 → push → 재평가. **기준 충족까지 반복**.

---

## Anthropic 원본과의 차이점

| 요소 | Anthropic 하니스 | 모바일/웹 Claude 적용 |
|------|------------------|---------------------|
| Planner | 전용 에이전트 | 웹 Claude 대화 |
| Generator | Claude Code (로컬) | 모바일 Claude Code |
| Evaluator | Playwright MCP 자동화 | 웹 Claude + 사용자 스크린샷 |
| 반복 자동화 | 완전 자동 (5-15회) | 수동 (사용자가 Bridge) |
| 소요 시간 | ~4시간 연속 | 여러 세션에 분산 가능 |
| 비용 | $200 (Opus 4.5 기준) | 구독 범위 내 |

### 장점

- **비용 효율적**: 별도 API 비용 없이 구독만으로 가능
- **유연한 시간 배분**: 모바일이므로 틈틈이 진행 가능
- **인간 감각 포함**: 스크린샷 평가에 사용자의 직감이 추가됨
- **세션 독립적**: 각 Phase가 독립된 세션이므로 context 소진 문제 완화

### 단점과 완화 방법

| 단점 | 완화 방법 |
|------|-----------|
| 사용자가 Bridge 역할을 해야 함 | 평가 루브릭을 구체적으로 만들어 Bridge 부담 최소화 |
| 자동화 반복 불가 | 스프린트를 작게 나눠 한 번에 처리할 양 줄이기 |
| 세션 간 컨텍스트 손실 | `claude-progress.txt` 패턴 활용 |
| 모바일 코딩의 불편함 | Claude Code가 대부분 작성, 사용자는 지시만 |

---

## 실전 팁

### 1. `claude-progress.txt` 활용

[Anthropic 하니스 엔지니어링](../topics/anthropic-harness-engineering.md)의 핵심 인사이트를 차용한다. 프로젝트 루트에 진행 상태 파일을 유지:

```markdown
# Web Design Progress

## 현재 상태
Sprint 3 진행 중 - 반응형 처리

## 완료된 스프린트
- Sprint 1: HTML 구조 + 레이아웃 ✅
- Sprint 2: 타이포그래피 + 색상 ✅ (평가 통과)

## 마지막 평가 피드백
- 모바일에서 네비게이션 햄버거 메뉴 필요
- 카드 컴포넌트 간격 좁힘 필요

## 다음 할 일
- 768px 이하 브레이크포인트 추가
- 모바일 네비게이션 구현
```

모바일 Claude Code 새 세션 시작 시 이 파일을 읽으면 즉시 맥락을 복원할 수 있다.

### 2. 평가 루브릭을 파일로 저장

루브릭을 프로젝트에 `evaluation-rubric.md`로 저장해두면, 웹 Claude에 매번 붙여넣을 필요 없이 참조할 수 있다.

### 3. 스크린샷 체크리스트

매 평가마다 동일한 뷰를 캡처하면 일관된 비교가 가능하다:

- [ ] 데스크톱 전체 페이지
- [ ] 모바일 (375px) 전체 페이지
- [ ] 핵심 인터랙션 전/후
- [ ] 다크모드 (해당 시)

### 4. Git 커밋을 스프린트 경계로 사용

각 스프린트 완료 시 태그를 달면 이전 버전과 비교하기 쉽다:
```
git tag sprint-1-complete
git tag sprint-2-complete
```

---

## 요약: 최소 실행 가능 루프

가장 간단한 형태로 줄이면:

1. **웹 Claude에서 계획** → 명세 + 평가 기준
2. **모바일 Claude Code에서 구현** → push
3. **배포된 결과를 스크린샷** → 웹 Claude에 평가 요청
4. **피드백을 Claude Code에 전달** → 수정 → push
5. **기준 충족까지 3-4 반복**

Generator-Evaluator의 본질은 도구가 아니라 **"생성과 평가를 분리하고, 검증 가능한 기준으로 반복한다"**는 구조에 있다. Playwright가 없어도 이 구조는 유지할 수 있다.

---

## 관련 페이지

- [Generator-Evaluator 루프](../concepts/generator-evaluator-loop.md)
- [에이전트 하니스](../concepts/agent-harness.md)
- [Anthropic 하니스 엔지니어링](../topics/anthropic-harness-engineering.md)
