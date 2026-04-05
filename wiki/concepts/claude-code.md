---
title: "Claude Code"
created: 2026-04-05
updated: 2026-04-05
tags: [claude-code, anthropic, AI-agent, coding-tool, source-leak]
sources: [sources/the-batch-issue-347.md]
---

# Claude Code

Anthropic이 개발한 AI 코딩 에이전트. 2026년 3월 소스 코드 유출 사건을 통해 내부 아키텍처가 공개됐다.

## 아키텍처

엔지니어들의 분석에 따르면 Claude Code는 **챗봇 래퍼가 아닌 소규모 전용 운영체제(small, dedicated operating system)**처럼 구축되어 있다.

## 유출 사건 (2026-03-30)

Anthropic이 npm 레지스트리에 버전 2.1.88을 게시하면서 소스 맵(`.map`) 파일을 함께 포함하는 실수를 저질렀다. 소스 맵은 번들링/난독화된 JavaScript를 원본 소스로 복원하는 해독 키 역할을 한다.

- **발견자**: Chaofan Shou (블록체인 스타트업 Solayer Labs 인턴) — X(구 트위터)에 공개
- **규모**: 1,900개 파일, 512,000줄 이상의 코드
- **원인**: Anthropic 공식 입장 — "인간의 실수로 인한 릴리스 패키징 문제"
- **영향**: 발견 후 40,000회 이상 포크됨
- **데이터 피해**: 없음 (사용자/고객 데이터 미노출)

## 유출로 밝혀진 미공개 기능

### Kairos (카이로스)
- 상시 동작(always-on) 백그라운드 데몬 에이전트 서브시스템
- 이름의 의미: 그리스어로 "적시(the right moment)"
- 유휴 시간 동안 자율적으로 실행하며 메모리를 통합하고 관찰 내용을 병합
- autoDream 로직 시스템을 포함

### autoDream
- Kairos의 메모리 관리 및 정제 시스템
- 기능: 중복 메모리 병합, 모순 제거, 추측 해소, 저장 데이터를 행동에 적합하게 정제

### Ultraplan
- 리소스 집약적 작업을 클라우드로 전송하는 서브에이전트

### Buddy
- 사용자의 작업에 코멘트하는 AI "펫" 페르소나
- 목적: 사용자 참여도(engagement) 향상

### 음성 인터페이스
- 미공개 음성 상호작용 모드

### 언더커버 모드 (Undercover Mode)
- 공개/오픈소스 저장소 작업 시 커밋, PR 제목, 본문에서 Anthropic 브랜딩을 제거
- AI 에이전트가 작성한 것이 아닌 인간 개발자가 작성한 것처럼 보이게 함
- 시스템 프롬프트 내용: *"Do not blow your cover."*

### 가짜 도구 주입 (Fake Tool Injection / Anti-Distillation)
- API 요청에 `anti_distillation: ['fake_tools']`를 전송
- 서버가 시스템 프롬프트에 미끼 도구 정의를 조용히 주입
- 목적: 경쟁사가 Claude Code 출력을 스크래핑하여 훈련 데이터로 사용하려 할 때 데이터를 오염시킴

### Coordinator 모드
- Claude를 병렬 워커 서브에이전트를 관리하는 오케스트레이터로 전환

### Auto 모드
- AI 분류기를 사용하여 도구 권한을 자동으로 승인

## 관련 페이지

- [Anthropic](../entities/anthropic.md)
- [The Batch Issue 347](../topics/the-batch-issue-347.md)
