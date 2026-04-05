---
title: "Anthropic"
created: 2026-04-05
updated: 2026-04-05
tags: [anthropic, AI-company, Claude, coding-agent, agent-harness]
sources: [sources/the-batch-issue-347.md, sources/anthropic-harness-design-long-running-apps.md]
---

# Anthropic

AI 안전 연구 회사. Claude 언어 모델 및 Claude Code 코딩 에이전트를 개발한다.

## 주요 제품

- **Claude**: 대형 언어 모델 시리즈
- **Claude Code**: AI 코딩 에이전트 ([상세 페이지](../concepts/claude-code.md))

## 주요 사건

### Claude Code 소스 코드 유출 (2026-03-30)
- npm 릴리스 패키징 실수로 512,000줄 이상의 Claude Code 소스 코드가 공개됨
- Kairos, autoDream, 언더커버 모드 등 미공개 기능 노출
- Anthropic 입장: "인간의 실수, 보안 침해 아님, 사용자 데이터 미노출"
- 상세 내용: [Claude Code](../concepts/claude-code.md)

## 엔지니어링 연구

### 에이전트 하니스 설계 (2026-04)
- 장기 실행 자율 소프트웨어 개발을 위한 멀티 에이전트 하니스 설계 발표
- **Planner-Generator-Evaluator** 3-에이전트 구조 (GAN에서 영감)
- Evaluator가 Playwright MCP로 실행 중인 앱을 직접 테스트
- 프론트엔드 디자인 평가 기준 분해: 디자인 품질, 독창성, 장인 정신, 기능성
- Solo 에이전트($9, 20분) vs 전체 하니스($200, 6시간): 완성도에서 큰 차이
- 멀티 세션 연속성: `claude-progress.txt`, `feature_list.json`, `init.sh`로 context 재시작 문제 해결
- 상세 내용: [Anthropic 하니스 엔지니어링](../topics/anthropic-harness-engineering.md)

## 관련 페이지

- [Claude Code](../concepts/claude-code.md)
- [에이전트 하니스](../concepts/agent-harness.md)
- [Generator-Evaluator 루프](../concepts/generator-evaluator-loop.md)
- [Anthropic 하니스 엔지니어링](../topics/anthropic-harness-engineering.md)
- [The Batch Issue 347](../topics/the-batch-issue-347.md)
