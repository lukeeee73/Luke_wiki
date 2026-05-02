---
title: "Anthropic: 에이전트 코딩 Eval의 인프라 노이즈 정량화"
created: 2026-04-11
updated: 2026-04-11
domain: ai
type: fact-set
weight: reference
confidence: high
tags: [anthropic, eval, benchmark, infrastructure, agentic-coding, Terminal-Bench, kubernetes]
sources: [sources/anthropic-infrastructure-noise.md]
---

# Anthropic: 에이전트 코딩 Eval의 인프라 노이즈 정량화

> 원본: [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise) (Anthropic Engineering Blog, 2026-02)

## 문제 제기

공개 에이전트 코딩 벤치마크에서 모델 순위가 실제 역량 차이가 아니라 **평가 인프라 구성의 차이** 때문에 바뀔 수 있다. Anthropic은 이 가설을 Terminal-Bench 2.0으로 체계적으로 검증했다.

## 발견 경위

Anthropic이 Google Kubernetes Engine(GKE)에서 Terminal-Bench 2.0을 실행했더니 공식 리더보드와 점수가 달랐다. 원인을 추적하니 GKE가 per-task 자원 스펙을 **보장 하한선이자 하드 상한선**으로 처리하기 때문이었다. 순간 메모리 스파이크가 발생하면 컨테이너가 OOM-kill되어 모델 역량과 무관하게 태스크가 실패했다.

## 실험 설계

| 변수 | 내용 |
|------|------|
| 벤치마크 | Terminal-Bench 2.0 |
| 플랫폼 | Google Kubernetes Engine |
| 자원 구성 | 6단계: 1x 엄격 적용 → 무제한 |
| 통제 | 동일 모델 · 하니스 · 태스크 세트 |

## 핵심 결과

### 인프라 오류율

| 자원 구성 | 인프라 오류율 |
|-----------|--------------|
| 1x (엄격 적용) | **5.8%** (pod 크래시, OOM-kill) |
| 무제한 | **0.5%** |

인프라 오류율은 자원 증가에 따라 **단조 감소**. 모델 역량과 무관한 순수 인프라 원인 실패가 5.8%에 달함.

### 총 점수 격차

- 1x 엄격 ~ 무제한: **+6 퍼센트포인트** (p < 0.01)
- 이 격차는 최상위 프론티어 모델 간 통상적인 리더보드 차이(1~3pp)를 초과

## 두 가지 효과의 분리

```
자원 증가
1x ──────────── ~3x ──────────── 무제한
     안정성 효과          역량 효과
     (infra noise 제거)   (새 문제 풀이 가능화)
```

### 안정성 효과 (~3x 이하)
- 순간 자원 스파이크로 인한 **spurious failure** 제거
- eval의 "난이도" 자체는 변하지 않음
- Terminal-Bench 공식 리더보드의 샌드박싱 제공자도 암묵적으로 이 수준의 버퍼 제공 중

### 역량 효과 (~3x 초과)
- 추가 자원이 에이전트가 **원래 풀지 못했던 문제**를 풀 수 있게 만듦
- 이 구간부터 eval이 무엇을 측정하는지 자체가 달라짐
- 자원 제한이 평가 대상(측정하는 역량)을 암묵적으로 규정하게 됨

## 리더보드 해석에 대한 함의

최상위 프론티어 모델들은 리더보드에서 보통 **1~3포인트** 차이로 순위가 갈린다. 이 격차가 6포인트 인프라 노이즈 범위 안에 있기 때문에, 자원 구성이 동일하게 통제되지 않는 한 해당 순위는 **역량 차이가 아니라 인프라 차이를 반영**할 수 있다.

## 권고사항

1. **자원 구성 = 1등급 실험 변수**: 프롬프트 형식, 샘플링 온도와 같은 수준으로 문서화·통제
2. **3pp 이하 격차 회의론**: eval 구성이 문서화·일치될 때까지 보류
3. **투명한 보고**: 에이전트 eval 결과 발표 시 자원 구성 반드시 명시

## 관련 페이지

- [에이전트 Eval 방법론](../concepts/agentic-evals.md)
- [Anthropic](../entities/anthropic.md)
- [Anthropic 하니스 엔지니어링](anthropic-harness-engineering.md)
- [Anthropic Managed Agents](anthropic-managed-agents.md)
