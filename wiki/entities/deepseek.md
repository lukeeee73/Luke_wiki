---
title: "DeepSeek"
created: 2026-06-20
updated: 2026-06-28
domain: ai, finance
type: entity
weight: reference
confidence: medium
tags: [DeepSeek, LLM, 중국AI, AI칩, 화웨이, Ascend, 미중경쟁]
sources: [sources/asml-smic-deepseek-v4-chips.md]
aliases: [DeepSeek, 딥시크, DeepSeek V4]
---

# DeepSeek

중국의 프런티어 LLM 개발사. 미·중 AI 반도체 격차 논의의 중심에 있는데, **어떤 칩으로 학습했는가**가 수출통제·제재 우회 논쟁의 핵심 쟁점이기 때문이다.

## V4 학습 칩 — 비공개, 논쟁 중

> [!claim] 출처 기반 주장
> DeepSeek 공식 입장은 V4 학습 칩 **비공개**. 부인 성명에서는 **H800 + Ascend 910C** 사용을 주장하고, 미 행정부의 "블랙웰 밀반입" 주장은 부인했다. V4-Pro 사전학습 코퍼스는 **32조 토큰 이상**으로 보고됐다.

> [!judgment] 핵심 구분 — 추론 ≠ 학습
> 화웨이 Ascend로 옮겨간 것은 **추론·사후학습**이며, "1,000개 Ascend 910C 작업"도 사후학습이다. 프런티어 **사전학습**은 여전히 [엔비디아](../entities/nvidia.md) 의존으로 보는 것이 컨센서스. 자세한 분석은 [중국 반도체 격차 — DeepSeek V4 학습 칩](../topics/china-chip-gap-deepseek-v4.md).

## V4 추론 효율 — DSpark

> [!fact] 사실
> DeepSeek는 V4와 함께 **DSpark**(speculative decoding) 알고리즘과 **DeepSpec** 저장소를 공개했다. `DeepSeek-V4-Pro-DSpark`는 V4-Pro와 동일한 가중치에 드래프트 모듈만 부착한 버전으로, 출력 품질은 그대로 둔 채 Decode 단계를 가속한다. 자세한 메커니즘은 [DSpark & Speculative Decoding](../concepts/speculative-decoding.md).

## 관련 페이지

- [중국 반도체 격차 — ASML EUV 의혹 · SMIC/화웨이 · DeepSeek V4](../topics/china-chip-gap-deepseek-v4.md)
- [DSpark & Speculative Decoding](../concepts/speculative-decoding.md) — V4-Pro-DSpark, Decode 메모리 대역폭 가속
- [LLM 서빙 스택 — 계층 구조](../concepts/llm-serving-stack.md) — MLA 같은 새 어텐션 구조가 벤더별 전용 커널을 요구하는 이유
- [엔비디아 (NVIDIA)](nvidia.md) · [TSMC](tsmc.md)
- [반도체·AI 칩 가치사슬 종합](../syntheses/semiconductor-ai-chip-value-chain.md)
