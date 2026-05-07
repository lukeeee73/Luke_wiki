---
title: "Andrej Karpathy"
created: 2026-04-05
updated: 2026-05-07
domain: ai
type: entity
weight: reference
confidence: high
tags: [인물, AI, 딥러닝, LLM, autoresearch]
sources: [sources/karpathy-llm-wiki-pattern.md, sources/karpathy-autoresearch-train.py]
---

# Andrej Karpathy

AI 연구자이자 교육자. 컴퓨터 비전, 딥러닝, LLM 분야의 저명한 인물.

## 주요 경력

- Stanford 박사 (Fei-Fei Li 연구실)
- OpenAI 창립 멤버
- Tesla AI Director (Autopilot)
- 현재 독립 연구/교육 활동 (nanoGPT, nanochat, autoresearch 등)

## 이 위키와의 관련성

### LLM Wiki 패턴 (2026-04 ingest)

- [LLM Wiki 패턴](../principles/llm-wiki-pattern.md)의 제안자
- 이 지식 저장소의 구조적 토대를 제공한 gist 작성

### Autoresearch (2026-05 ingest)

- [Karpathy Autoresearch](../topics/karpathy-autoresearch.md) — AI 에이전트가 단일 GPU에서 자율적으로 ML 실험을 수행하는 630줄 프로젝트
- [Muon Optimizer](../concepts/muon-optimizer.md) — autoresearch `train.py`의 핵심 옵티마이저 (Polar Express + NorMuon + Cautious WD)
- 시사점: [Generator-Evaluator 루프](../principles/generator-evaluator-loop.md)를 결정론적 평가지표(`val_bpb`)로 극단적으로 단순화한 자율 연구 사례

## 출처

- [LLM Wiki 패턴 원본](../../sources/karpathy-llm-wiki-pattern.md)
- [autoresearch/train.py](../../sources/karpathy-autoresearch-train.py)
