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

Anthropic이 npm 레지스트리에 버전 2.1.88을 게시하면서 소스 맵 파일을 함께 포함하는 실수를 저질렀다.

- **규모**: 1,900개 파일, 512,000줄 이상의 코드
- **원인**: Anthropic 공식 입장 - "인간의 실수로 인한 릴리스 패키징 문제"
- **영향**: 발견 후 40,000회 이상 포크됨
- **데이터 피해**: 없음 (사용자/고객 데이터 미노출)

## 유출로 밝혀진 미공개 기능

### Kairos
- 상시 동작(always-on) 백그라운드 에이전트 서브시스템
- 이름의 의미: 그리스어로 "적시(timely)"
- autoDream 로직 시스템을 포함

### autoDream
- 메모리 관리 및 정제 시스템
- 기능: 중복 메모리 병합, 모순 제거, 추측 해소, 저장 데이터를 행동에 적합하게 정제

### Ultraplan
- 리소스 집약적 작업을 클라우드로 전송하는 서브에이전트

### Buddy
- 사용자의 작업에 코멘트하는 페르소나
- 목적: 사용자 참여도(engagement) 향상

### 음성 인터페이스
- 미공개 음성 UI

### 언더커버 모드 (Undercover Mode)
- 공개 git 저장소에 서명이나 활동 흔적 없이 파일을 커밋하는 기능
- AI 에이전트가 저장소에 활동했다는 흔적을 남기지 않음

## 관련 페이지

- [Anthropic](../entities/anthropic.md)
- [The Batch Issue 347](../topics/the-batch-issue-347.md)
