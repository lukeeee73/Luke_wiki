---
title: "Google DeepMind"
created: 2026-04-05
updated: 2026-04-05
domain: ai
type: entity
weight: reference
confidence: high
tags: [google, deepmind, AI-company, Gemini, Lyria]
sources: [sources/the-batch-issue-347.md]
---

# Google DeepMind

Google의 AI 연구 부문. Gemini 언어 모델, Lyria 음악 생성 모델 등을 개발한다.

## 주요 제품/모델

- **Gemini**: 대형 언어 모델 및 멀티모달 AI 플랫폼
- **Lyria**: 음악 생성 모델 시리즈
- **Genie**: 생성 월드 모델 (World Labs Marble의 경쟁 제품)

## Lyria 3 (2026년 출시)

Gemini 앱에 무료 통합된 음악 생성 모델.

### 기술 구조
- **잠재 확산(Latent Diffusion)** 기반: 시간적 오디오 잠재 변수에서 노이즈 제거
- 이미지 생성기(latent diffusion)의 원리를 오디오에 적용
- 훈련 3단계: 사전훈련 → 지도 미세조정 → RLHF

### 기능
- 텍스트 설명 또는 이미지 → 30초 오디오 클립 생성
- 악기, 가창 보이스, 가사 포함 가능
- 지원 언어: 영어, 독일어, 스페인어, 프랑스어, 힌디어, 일본어, 한국어, 포르투갈어 (8개)
- 악기 편성, 스타일, 시대, 보컬 스타일, 템포, 다이나믹스 지정 가능

### 저작권 전략
- 훈련 데이터 라이선스 취득 (Lyria 2는 무단 저작권 음원 사용 논란이 있었음)
- 저작권 저작물 유사성 필터 적용
- 아티스트 음향적 특성(sonic likeness) 재현 방지

## 관련 페이지

- [The Batch Issue 347](../topics/the-batch-issue-347.md)
