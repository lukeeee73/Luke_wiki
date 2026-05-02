---
title: "Anthropic 하니스 엔지니어링: 장기 실행 앱 설계"
created: 2026-04-05
updated: 2026-04-05
domain: ai
type: fact-set
weight: important
confidence: high
tags: [anthropic, agent-harness, multi-agent, long-running-agents, generator-evaluator, claude]
sources: [sources/anthropic-harness-design-long-running-apps.md]
---

# Anthropic 하니스 엔지니어링: 장기 실행 앱 설계

Anthropic 엔지니어링 팀이 발표한 두 편의 블로그 포스트를 기반으로, 장기 실행 자율 소프트웨어 개발을 위한 에이전트 하니스 설계 방법론을 정리한 페이지.

**원본 출처**:
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) (2026-04)
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

---

## 배경: 장기 실행 에이전트의 핵심 문제

AI 에이전트가 점점 더 복잡한 작업을 요청받고 있으며, 이는 수 시간 또는 수 일에 걸친 작업을 의미한다. 그러나 여러 context window에 걸쳐 일관된 진행을 유지하는 것은 열린 문제로 남아있었다.

**3가지 근본 제약**:
1. 에이전트는 이산적 세션에서 작업 — 새 세션은 이전 기억이 없음
2. Context window의 한계 — 복잡한 프로젝트는 단일 context로 완료 불가
3. 에이전트의 과도한 욕심 — 한 번에 너무 많이 시도 → context 소진 후 반쯤 구현된 상태로 종료

---

## 해결책 1: 멀티 세션 하니스 (Effective Harnesses 방식)

### 2-에이전트 패턴

**Initializer Agent** (첫 세션 전용)

전용 프롬프트로 기반 인프라 구축. 4가지 핵심 산출물:

| 산출물 | 역할 |
|--------|------|
| `feature_list.json` | 고수준 프롬프트 → 수백 개의 구체적·테스트 가능한 요구사항 |
| `claude-progress.txt` | 세션 간 작업 이력 핸드오프 메커니즘 |
| `init.sh` | 개발 환경 원클릭 시작 스크립트 |
| 초기 git commit | 생성 파일 문서화 및 baseline |

**Coding Agent** (이후 모든 세션)

- 매 세션: 점진적 진행 수행
- 세션 종료 시: `claude-progress.txt`에 구조화된 업데이트 기록
- 세션 시작 시: `claude-progress.txt` + git 이력으로 이전 상태 신속 파악

### 핵심 인사이트: claude-progress.txt

`claude-progress.txt`는 새로운 context window에서 이전 작업 상태를 빠르게 복원하는 **핸드오프 메커니즘**이다. git 이력과 결합하여 연속성을 보장한다.

---

## 해결책 2: Generator-Evaluator 하니스 (Harness Design 방식)

### GAN에서 영감받은 아키텍처

[Generator-Evaluator 루프](../principles/generator-evaluator-loop.md)는 Generative Adversarial Networks(GAN)에서 영감을 받았다. Generator와 Evaluator가 대립적 피드백 루프를 형성하여 품질을 반복적으로 향상시킨다.

### 3-에이전트 구조

```
[사용자 프롬프트]
        ↓
   [Planner]
   raw prompt → 상세 제품 명세
        ↓
   [Generator] ←──────────────┐
   스프린트 단위 구현          │
        ↓                      │
   [Evaluator]                  │
   Playwright로 실제 앱 테스트  │
   개선 제안 생성 ─────────────┘
        ↓ (기준 충족 시)
   [완성된 애플리케이션]
```

**Planner의 역할과 필요성**:
- 사용자의 raw 프롬프트를 상세 제품 명세서로 변환
- Planner 없이는 Generator가 작업 범위를 과소 설정 → 덜 완성된 결과
- 무엇을 만들지, 성공 기준을 어떻게 검증할지 명시

**Generator의 역할**:
- Planner의 명세를 받아 스프린트 단위로 구현
- Evaluator 피드백을 바탕으로 반복 개선
- 최종 제출 전 자체 체크리스트 검토

**Evaluator의 핵심 혁신**:
- 정적 코드 검토가 아닌, **Playwright MCP**로 실행 중인 앱을 직접 조작
- UI 기능 클릭, API 엔드포인트 테스트, 데이터베이스 상태 확인
- 주관적 품질 기준을 명시적·검증 가능한 기준으로 분해

### 프론트엔드 디자인 평가 기준 사례

"이것이 아름다운가?"는 너무 모호하다. Anthropic의 분해 방식:

| 기준 | 측정 방법 |
|------|-----------|
| 디자인 품질 | 5가지 디자인 원칙 준수 (0-5점) |
| 독창성 | AI 슬롭 여부 — generic gradients, stock-photo vibes, predictable layout (0-3점) |
| 장인 정신 | 주요 CTA의 시각적 무게감 (yes/no) |
| 기능성 | 실제 작동 여부 (Playwright 테스트) |

### 성능 비교

| 방식 | 시간 | 비용 | 결과 |
|------|------|------|------|
| Solo Agent (Opus 4.5) | 20분 | $9 | 비기능 요소 포함, 낮은 UX |
| Full 3-Agent Harness | 6시간 | $200 | 완성된 앱, 훨씬 나은 UX |

- 일반적으로 5-15번 반복, 최대 4시간 소요
- 비용 22배 증가 → 품질과 완성도에서 큰 차이 정당화

---

## 하니스 설계의 진화

모델 능력 향상에 따라 하니스 복잡도가 감소했다:

- **초기 모델**: context reset과 구조화된 세션 핸드오프 필수
- **Opus 4.5**: 자체적으로 많은 문제 해결 → context reset 제거 가능
- **Claude Agent SDK**: 자동 컴팩션(automatic compaction)이 context 증가를 처리 → 전체 빌드를 하나의 연속 세션으로 실행 가능

> **추론**: 하니스 복잡도는 모델 약점을 보완하기 위한 것이므로, 모델이 발전할수록 하니스는 단순해진다.

---

## 소프트웨어 개발과의 구조적 매핑

Generator-Evaluator 루프는 자연스럽게 소프트웨어 개발 생명주기에 매핑된다:

| 하니스 역할 | 소프트웨어 개발 역할 |
|-------------|---------------------|
| Planner | 제품 기획/요구사항 정의 |
| Generator | 개발자 (구현) |
| Evaluator | QA 엔지니어 + 코드 리뷰어 |
| claude-progress.txt | 스프린트 회의록 / 릴리스 노트 |
| feature_list.json | 백로그 / 인수 기준 |

---

## 관련 페이지

- [에이전트 하니스](../concepts/agent-harness.md)
- [Generator-Evaluator 루프](../principles/generator-evaluator-loop.md)
- [Anthropic](../entities/anthropic.md)
- [Claude Code](../concepts/claude-code.md)
