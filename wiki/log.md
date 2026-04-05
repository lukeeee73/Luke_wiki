---
title: "Wiki Log"
created: 2026-04-05
updated: 2026-04-05
tags: [log, meta]
sources: []
---

# Wiki Log

위키의 모든 작업 이력을 시간순으로 기록합니다.

---

## 2026-04-05

### [INIT] 위키 저장소 초기화

- **작업**: 지식 저장소 초기 구조 생성
- **설명**: Andrej Karpathy의 LLM Wiki 패턴을 기반으로 3계층 구조(Sources/Wiki/Schema) 설정
- **생성된 파일**:
  - `CLAUDE.md` - Schema Layer (위키 운영 규칙)
  - `wiki/index.md` - 위키 인덱스
  - `wiki/log.md` - 작업 이력 (이 파일)
  - `sources/.gitkeep` - 원본 자료 디렉토리
  - 위키 하위 디렉토리: concepts, entities, topics, comparisons, syntheses

---

### [INGEST] The Batch Issue 347

- **작업**: DeepLearning.AI The Batch 347호 수집 및 위키 통합
- **원본 URL**: https://www.deeplearning.ai/the-batch/issue-347/
- **이슈 제목**: Claude Code's Source Leaks, OpenAI Exits Video Generation, Gemini Adds Music Generation, and more...
- **생성된 파일**:
  - `sources/the-batch-issue-347.md` - 원본 자료 요약
  - `wiki/topics/the-batch-issue-347.md` - 이슈 전체 요약
  - `wiki/concepts/claude-code.md` - Claude Code 아키텍처 및 소스 유출 사건
  - `wiki/concepts/voice-based-ai.md` - 음성 기반 AI 동향 (Andrew Ng 관점)
  - `wiki/entities/anthropic.md` - Anthropic 엔티티 페이지
  - `wiki/entities/openai.md` - OpenAI 엔티티 페이지 (Sora 종료 포함)
  - `wiki/entities/google-deepmind.md` - Google DeepMind 엔티티 페이지 (Lyria 3 포함)
  - `wiki/entities/world-labs.md` - World Labs 엔티티 페이지 (Marble, Chisel)
  - `wiki/entities/andrew-ng.md` - Andrew Ng 엔티티 페이지
- **업데이트된 파일**:
  - `wiki/index.md` - 신규 페이지 9개 추가
- **주요 내용**:
  1. Claude Code 소스 유출 (Kairos, autoDream, 언더커버 모드 등 미공개 기능 노출)
  2. OpenAI Sora 종료 (2026-04-26 웹/앱, 2026-09-24 API)
  3. Google Lyria 3 출시 (텍스트/이미지 → 음악, 잠재 확산 기반)
  4. World Labs Marble + Chisel 공개 (영구적 편집 가능 3D 세계 생성)
  5. Andrew Ng의 음성 UI 부상 전망
