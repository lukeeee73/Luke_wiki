# The Batch Issue 347 - Raw Source

**출처**: https://www.deeplearning.ai/the-batch/issue-347/
**제목**: Claude Code's Source Leaks, OpenAI Exits Video Generation, Gemini Adds Music Generation, and more...
**수집일**: 2026-04-05

---

## Andrew Ng의 편지: "The Voice Stack is Improving Rapidly"

- 음성 기반 AI가 빠르게 발전하고 있으나, 대부분의 사람들은 음성 UI가 얼마나 보편화될지 아직 인식하지 못함
- 마우스 → 포인트-앤-클릭 앱, 터치/스와이프 → 모바일 앱처럼, 음성은 전혀 새로운 종류의 애플리케이션을 열 것
- **두 가지 아키텍처 접근법**:
  - 엔드-투-엔드 모델 (음성 입출력 통합): 낮은 지연, 하지만 제어 어려움/신뢰성 낮음
  - STT → LLM/에이전트 AI → TTS 파이프라인: 높은 신뢰성, 하지만 과도한 지연
- DeepLearning.AI, RealAvatar 등이 파이프라인 지연을 ~0.5~1초로 단축 (자연 대화 지연: 0.3~1초)
- 기법: 전체 응답 전 빠른 "사전 응답(pre-response)" 생성
- Claude Code로 수학 퀴즈 앱에 음성 기능 추가 (1시간 이내)
- **Vocal Bridge** (AI Fund 포트폴리오) 주목: CEO Ashwyn Sharma가 음성 UI 통합 개발자 도구 구축 중; AI Dev 26 연사

---

## 주요 기사 1: Claude Code 소스 코드 유출

**URL**: https://www.deeplearning.ai/the-batch/claude-codes-source-code-leaked-exposing-potential-future-features-kairos-and-autodream/

### 사건 개요
- 날짜: 2026-03-30
- Anthropic이 Claude Code npm 레지스트리에 버전 2.1.88을 게시하면서 `.map` 소스 맵 파일을 함께 포함
- 소스 맵 = 번들링/난독화된 JS를 원본으로 복원하는 해독 키
- **발견자**: Chaofan Shou (블록체인 스타트업 Solayer Labs 인턴) → X에 공개
- 1,900개 파일에 걸쳐 512,000줄 이상의 코드가 노출
- Anthropic 공식 입장: "인간의 실수로 인한 릴리스 패키징 문제이며, 보안 침해가 아님. 사용자/고객 데이터는 노출되지 않음"
- 해당 패키지는 이미 40,000회 이상 포크됨
- 평가: "챗봇 래퍼가 아닌 소규모 전용 운영체제처럼 구축"

### 노출된 숨겨진 기능
- **Kairos**: 상시 동작(always-on) 백그라운드 데몬 에이전트. 유휴 시 자율 실행, 메모리 통합. autoDream 포함
- **autoDream**: Kairos의 메모리 로직 — 중복 병합, 모순 제거, 추측 해소
- **음성 인터페이스**: 미공개 음성 UI
- **Ultraplan**: 리소스 집약적 작업을 클라우드로 전송하는 서브에이전트
- **Buddy**: 작업에 코멘트하는 AI "펫" 페르소나 (참여도 향상 목적)
- **언더커버 모드**: 공개 저장소에서 Anthropic 브랜딩 제거, 인간 개발자처럼 보이게 함. 시스템 프롬프트: "Do not blow your cover."
- **가짜 도구 주입(Anti-Distillation)**: `anti_distillation: ['fake_tools']` — 경쟁사 스크래핑 시 훈련 데이터 오염용 미끼 도구 주입
- **Coordinator 모드**: 병렬 워커 서브에이전트 오케스트레이터
- **Auto 모드**: AI 분류기로 도구 권한 자동 승인

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

### 내부 의사결정
- Sora 팀은 ChatGPT 통합 신규 비디오 모델 훈련을 제안했으나 경영진이 비용 이유로 전면 취소
- 발표 전 처리 리소스를 신모델 "Spud"(코딩/엔터프라이즈)로 이전
- Sora 팀 → 월드 모델, 로보틱스 장기 프로젝트 재배치

### Disney 파트너십 붕괴
- 2025년 말 체결: Disney 최대 $10억 투자 + OpenAI의 Disney 캐릭터 라이선스/영상 훈련 + Sora의 Disney+ 활용
- 공개 1시간 이내 Disney에 통보 ("충격적인 비즈니스 결례")
- Sam Altman: Josh D'Amaro(Disney CEO)에게 알리는 것이 "끔찍했다(felt terrible)"

### 기타
- OpenAI는 브라우저, Codex, ChatGPT 앱을 단일 데스크톱 앱으로 통합 예정

---

## 주요 기사 3: Google Lyria 3 - 음악 생성 모델

**URL**: https://www.deeplearning.ai/the-batch/google-debuted-lyria-3-an-app-that-turns-text-or-images-into-30-second-songs/

### 개요
- Google DeepMind 개발. Gemini 앱 무료 제공. Plus/Pro/Ultra 구독자 더 높은 사용 한도
- 텍스트 설명 또는 이미지로 30초 오디오 클립 생성

### 기술 구조
- 잠재 확산(Latent Diffusion): 시간적 오디오 잠재 변수에서 노이즈 제거 (이미지 생성기 원리의 오디오 적용)
- 훈련 3단계: 사전훈련 → 지도 미세조정 → RLHF
- 훈련 데이터: 다양한 수준의 텍스트 캡션이 달린 오디오, 품질/중복/안전 필터링

### 기능
- 악기, 가창 보이스, 가사 생성
- 지원 언어 8개: 영어, 독일어, 스페인어, 프랑스어, 힌디어, 일본어, 한국어, 포르투갈어
- 악기 편성, 스타일, 시대, 보컬 스타일, 템포, 다이나믹스 지정 가능
- Lyria 2 대비 음질 및 프롬프트 적합도 향상 (Google 인간/자동 평가 기준)

### 저작권 보호
- 훈련 데이터 라이선스 취득 (Lyria 2는 무단 저작권 음원 사용 논란)
- 저작권 저작물과의 유사성 필터링
- 아티스트 음향적 특성(sonic likeness) 재현 방지

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

---

## 이벤트: AI Dev 26

- 의제 공개
- 일시: 2026년 4월 28~29일
- 장소: Pier 48, San Francisco
- 진행: Andrew Ng
- 연사/스폰서: Google DeepMind, Oracle, AMD, Actian Corp, Neo4j, Arm 등
- 형식: 강연, 워크샵, 실습 데모, AI 스타트업 트랙, 네트워킹

---

## 주요 인물

- **Andrew Ng**: DeepLearning.AI 창립자, AI Fund 창립자, The Batch 저자
- **Chaofan Shou**: Solayer Labs 인턴, Claude Code 소스 맵 발견자
- **Ashwyn Sharma**: Vocal Bridge CEO/창업자, AI Fund EIR, AI Dev 26 연사
- **Sam Altman**: OpenAI CEO
- **Josh D'Amaro**: Disney CEO
- **Fei-Fei Li**: World Labs 창립자, Stanford 교수
