# The Batch Issue 347 - Raw Source

**출처**: https://www.deeplearning.ai/the-batch/issue-347/
**제목**: Claude Code's Source Leaks, OpenAI Exits Video Generation, Gemini Adds Music Generation, and more...
**수집일**: 2026-04-05

---

## Andrew Ng의 편지: 음성 기반 AI

- 음성 기반 AI가 빠르게 발전하고 있으나, 대부분의 사람들은 음성 UI가 얼마나 보편화될지 아직 인식하지 못함
- The Voice Stack이 빠르게 개선되고 있음
- 오디오를 직접 입력/생성하도록 훈련된 파운데이션 모델이 성장을 견인
- OpenAI의 RealTime API가 음성 입출력 시스템 개발을 쉽게 만들어줌
- Andrew Ng은 DeepLearning.AI, AI Fund, 협력사들과 함께 음성 기반 애플리케이션 작업 중

---

## 주요 기사 1: Claude Code 소스 코드 유출

**URL**: https://www.deeplearning.ai/the-batch/claude-codes-source-code-leaked-exposing-potential-future-features-kairos-and-autodream/

### 사건 개요
- 날짜: ~2026-03-30
- Anthropic이 Claude Code npm 레지스트리에 버전 2.1.88을 게시하면서 소스 맵 파일을 함께 포함
- 1,900개 파일에 걸쳐 512,000줄 이상의 코드가 노출
- Anthropic 공식 입장: "인간의 실수로 인한 릴리스 패키징 문제이며, 보안 침해가 아님. 사용자/고객 데이터는 노출되지 않음"
- 해당 패키지는 이미 40,000회 이상 포크됨

### 노출된 숨겨진 기능
- **Kairos**: 항상-켜진(always-on) 백그라운드 에이전트 서브시스템 (그리스어로 "적시"를 의미)
- **autoDream**: 메모리 정리 시스템 - 중복 메모리 병합, 모순 제거, 추측 해소, 저장 데이터를 행동에 적합하게 정제
- **음성 인터페이스**: 미공개 음성 UI
- **Ultraplan**: 리소스 집약적 작업을 클라우드로 전송하는 서브에이전트
- **Buddy**: 참여도 향상을 위해 작업에 코멘트하는 페르소나
- **언더커버 모드(Undercover Mode)**: 서명이나 활동 흔적 없이 공개 git 저장소에 파일을 커밋하는 기능

### 엔지니어들의 평가
- Claude Code는 챗봇 래퍼가 아닌 소규모 전용 운영체제처럼 구축되어 있음

---

## 주요 기사 2: OpenAI, Sora 서비스 종료

**URL**: https://www.deeplearning.ai/the-batch/openai-announced-it-would-shut-down-sora-its-once-state-of-the-art-video-model/
**Data Points URL**: https://www.deeplearning.ai/the-batch/sora-no-more-openai-shuts-down-video-maker/

### 종료 일정
- 웹/앱 접근: 2026년 4월 26일 종료
- API: 2026년 9월 24일 종료

### 재정 상황
- 하루 약 $1M(백만 달러) 손실
- 모바일 앱 출시 직후 일일 활성 사용자 약 100만 명 정점, 이후 절반 이하로 감소

### 후속 계획
- Sora 팀 → 월드 모델 및 로보틱스 장기 프로젝트로 재배치
- 발표 전 Sora의 처리 리소스를 코딩/엔터프라이즈 제품 지원 신모델 "Spud"로 전환
- OpenAI는 브라우저, Codex, ChatGPT 앱을 단일 데스크톱 애플리케이션으로 통합 예정

### 파트너십 영향
- Disney 파트너십 사실상 종료 (Disney 캐릭터 라이선스 + Disney 영상으로 모델 훈련, Disney의 최대 $10억 투자 예정이었음)

---

## 주요 기사 3: Google Lyria 3 - 음악 생성 모델

**URL**: https://www.deeplearning.ai/the-batch/google-debuted-lyria-3-an-app-that-turns-text-or-images-into-30-second-songs/

### 개요
- Gemini 앱 사용자에게 무료 제공
- 텍스트 설명 또는 이미지로 30초 오디오 클립 생성

### 기술 구조
- 잠재 확산(Latent Diffusion) 기반: 이미지 생성기처럼 순수 노이즈의 임베딩에서 노이즈를 제거하는 방식을 오디오에 적용
- 시간적 오디오 잠재 변수(temporal audio latents)에 잠재 확산 적용
- 훈련 3단계: 사전훈련 → 지도 미세조정 → RLHF

### 기능
- 악기, 가창 보이스, 가사 생성
- 지원 언어 8개: 영어, 독일어, 스페인어, 프랑스어, 힌디어, 일본어, 한국어, 포르투갈어
- 악기 편성, 스타일, 시대, 보컬 스타일, 템포, 다이나믹스 지정 가능

### 저작권 보호
- 훈련 데이터 라이선스 취득 (Lyria 2는 무단 저작권 음원으로 훈련했다는 보도 있음)
- 저작권 저작물과의 유사성 필터링
- 아티스트 음향적 특성 재현 방지

---

## Data Points: World Labs, Marble + Chisel - 3D 세계 생성

**URL**: https://www.deeplearning.ai/the-batch/world-labs-makes-its-marble-generative-world-model-public-adds-chisel-editing-tool/
**Data Points URL**: https://www.deeplearning.ai/the-batch/generating-persistent-editable-3d-worlds/

### 개요
- Fei-Fei Li가 창립한 AI 스타트업 World Labs의 상업적 생성 월드 모델 공개
- 텍스트 프롬프트, 사진, 비디오, 3D 레이아웃, 파노라마 → 편집 가능한 3D 환경 생성

### Marble 특징
- 경쟁사(Decart, Odyssey, Google Genie)와 달리 영구적(persistent) 3D 공간 생성
- 가우시안 스플랫(Gaussian splats), 메시(meshes), 비디오로 내보내기 가능

### Chisel
- Marble 출력물을 텍스트 프롬프트로 수정하는 통합 에디터
- 처음부터 공간 환경 제작 가능
