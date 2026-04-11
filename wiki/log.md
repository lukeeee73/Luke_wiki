---
title: "Wiki Log"
created: 2026-04-05
updated: 2026-04-11
tags: [log, meta]
sources: []
---


# Wiki Log

위키의 모든 작업 이력을 시간순으로 기록합니다.

---

## 2026-04-11 (3차 업데이트)

### [INGEST] Ray Dalio "The Big Thing: We Are In A World War" LinkedIn 아티클

- **작업**: Ray Dalio의 LinkedIn/Substack 장문 분석 수집 및 위키 통합
- **원본 URL**: https://www.linkedin.com/pulse/big-thing-we-world-war-isnt-going-end-anytime-soon-ray-dalio-sbrqe
- **Substack URL**: https://raydalio.substack.com/p/the-big-thing-we-are-in-a-world-war
- **원본 발행일**: 2026-04-07 (추정)
- **수집 방법**: LinkedIn 직접 접근 불가(403)로 다수 매체 보도 종합 (Time, Yahoo Finance, Benzinga, IBTimes 등)
- **생성된 파일**:
  - `sources/ray-dalio-world-war-big-thing.md` - 원본 자료 종합 요약
  - `wiki/topics/ray-dalio-world-war-big-cycle.md` - 세계대전과 Big Cycle 분석 주제 페이지
  - `wiki/entities/ray-dalio.md` - Ray Dalio 엔티티 페이지
  - `wiki/concepts/big-cycle.md` - Big Cycle (대순환) 개념 페이지
- **업데이트된 파일**:
  - `wiki/index.md` - 신규 페이지 3개 추가 (concepts 1, entities 1, topics 1)
- **주요 내용**:
  1. 세계는 이미 세계대전 상태: 4개의 실전(러시아-우크라이나, 이스라엘-가자, 예멘-수단, 미국-이란) + 다수의 비실전(무역·경제·기술전)
  2. Big Cycle 13단계 중 9단계(동시다발적 다전역 분쟁)에 위치, 1913-14년·1938-39년과 유사
  3. 동맹 양극화: 중국·러시아·이란·북한 vs 미국·유럽·이스라엘·GCC·일본·호주
  4. 미국 과잉 확장: 750-800개 해외 기지(70-80개국) vs 중국 1개
  5. 확률 평가: 5년 내 주요 분쟁 >50%, 미중 충돌 30-40% (최고 위험: 2028년)
  6. 시장은 이러한 지정학적 리스크를 전혀 가격에 반영하지 않고 있음
- **비고**: 위키 최초의 지정학/매크로 경제 분야 자료. 기존 AI/ML 중심에서 주제 다양화.

---

## 2026-04-11 (2차 업데이트)

### [INGEST] Anthropic 인프라 노이즈 블로그 포스트

- **작업**: Anthropic 엔지니어링 블로그 "Quantifying infrastructure noise in agentic coding evals" 수집 및 위키 통합
- **원본 URL**: https://www.anthropic.com/engineering/infrastructure-noise
- **원본 발행일**: 2026-02
- **생성된 파일**:
  - `sources/anthropic-infrastructure-noise.md` - 원본 자료 요약
  - `wiki/topics/anthropic-infrastructure-noise.md` - 블로그 포스트 통합 분석
  - `wiki/concepts/agentic-evals.md` - 에이전트 Eval 방법론 개념 페이지
- **업데이트된 파일**:
  - `wiki/entities/anthropic.md` - 인프라 노이즈 연구 섹션 추가
  - `wiki/index.md` - 신규 페이지 2개 추가
- **주요 내용**:
  1. Terminal-Bench 2.0을 GKE에서 6가지 자원 구성으로 실행 → 1x 엄격 ~ 무제한 간 6pp 격차 (p < 0.01)
  2. 인프라 오류율: 1x 엄격 5.8% → 무제한 0.5% (단조 감소)
  3. 두 효과 구분: ~3x 이하 = 안정성 효과(spurious failure 제거), ~3x 초과 = 역량 효과(새 문제 풀이 가능)
  4. 최상위 모델 간 리더보드 격차(1~3pp)가 6pp 노이즈 범위 내 → 인프라 통제 없이 순위 신뢰 불가
  5. 권고: 자원 구성을 1등급 실험 변수로 문서화; 3pp 이하 격차는 구성 일치 확인 전 유보

---

## 2026-04-11

### [INGEST] Anthropic Managed Agents 블로그 포스트

- **작업**: Anthropic 엔지니어링 블로그 "Scaling Managed Agents: Decoupling the brain from the hands" 수집 및 위키 통합
- **원본 URL**: https://www.anthropic.com/engineering/managed-agents
- **원본 발행일**: 2026-04-08
- **생성된 파일**:
  - `sources/anthropic-managed-agents.md` - 원본 자료 요약
  - `wiki/topics/anthropic-managed-agents.md` - 블로그 포스트 통합 분석
  - `wiki/concepts/managed-agents.md` - Managed Agents 개념 페이지
- **업데이트된 파일**:
  - `wiki/concepts/agent-harness.md` - 메타-하니스 패턴 섹션 추가
  - `wiki/entities/anthropic.md` - Managed Agents 출시 섹션 추가, 제품 목록 업데이트
  - `wiki/index.md` - 신규 페이지 2개 추가
- **주요 내용**:
  1. Managed Agents = Session·Harness·Sandbox 3요소 가상화 → "뇌(Claude)와 손(실행환경) 분리"
  2. 지연 프로비저닝으로 p50 TTFT 60%↓, p95 TTFT 90%+↓ 성능 개선
  3. Session: append-only 이벤트 로그, `getEvents()`로 위치 기반 컨텍스트 조회
  4. 메타-하니스 철학: 인터페이스(session + sandbox)에만 의견, 특정 하니스에는 무관심
  5. 멀티-에이전트: 서브에이전트(동일 세션) vs 에이전트 팀(독립 컨텍스트)
  6. Claude Code SDK → Claude Agent SDK로 이름 변경
  7. 서비스: 공개 베타, $0.08/세션시간 + 표준 토큰 비용

---

## 2026-04-05 (2차 업데이트)

### [INGEST] Anthropic 하니스 엔지니어링 블로그 포스트

- **작업**: Anthropic 엔지니어링 블로그 2편 수집 및 위키 통합
- **원본 URL 1**: https://www.anthropic.com/engineering/harness-design-long-running-apps
- **원본 URL 2**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **생성된 파일**:
  - `sources/anthropic-harness-design-long-running-apps.md` - 원본 자료 요약
  - `wiki/topics/anthropic-harness-engineering.md` - 두 블로그 포스트 통합 분석
  - `wiki/concepts/agent-harness.md` - 에이전트 하니스 개념 페이지
  - `wiki/concepts/generator-evaluator-loop.md` - Generator-Evaluator 루프 개념 페이지
- **업데이트된 파일**:
  - `wiki/entities/anthropic.md` - 하니스 엔지니어링 섹션 추가
  - `wiki/index.md` - 신규 페이지 3개 추가
- **주요 내용**:
  1. GAN에서 영감받은 Planner-Generator-Evaluator 3-에이전트 하니스 설계
  2. Evaluator가 Playwright MCP로 실행 중인 앱 직접 테스트 (정적 코드 검토 대신)
  3. 프론트엔드 평가 기준 분해: 디자인 품질·독창성·장인정신·기능성
  4. 성능 비교: Solo($9, 20분) vs Full Harness($200, 6시간) — 완성도에서 큰 차이
  5. 멀티 세션 연속성 패턴: claude-progress.txt, feature_list.json, init.sh
  6. 모델 발전에 따른 하니스 단순화 경향 (Opus 4.5 이후)

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
