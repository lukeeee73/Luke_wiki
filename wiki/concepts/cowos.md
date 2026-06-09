---
title: "CoWoS (Chip-on-Wafer-on-Substrate)"
created: 2026-06-09
updated: 2026-06-09
domain: finance, ai
type: framework
weight: important
confidence: high
tags: [CoWoS, 패키징, 인터포저, HBM, AI칩, TSMC, 반도체투자]
sources: [sources/semiconductor-ai-chip-value-chain.md]
aliases: [CoWoS, 코워스, 2.5D 패키징]
---

# CoWoS (Chip-on-Wafer-on-Substrate)

[TSMC](../entities/tsmc.md)의 **2.5D 첨단 패키징** 기술. GPU 로직 다이와 [HBM](hbm.md) 메모리 스택들을 하나의 **실리콘 인터포저** 위에 나란히 올려 초고대역폭으로 연결한다. AI 칩 공급 전체의 실질적 병목.

## 구조

```
        [HBM 스택]   [GPU 로직 다이]   [HBM 스택]      ← TSMC 제조 / SK하이닉스 등 HBM
        └──────── 실리콘 인터포저 (미세 배선) ────────┘  ← 핵심
        └──────────── 패키지 기판 ───────────────┘
                  ○ ○ ○ ○ (솔더볼)
```

> [!fact] 사실 — 인터포저가 핵심
> **인터포저**는 미세 배선이 가능한 "실리콘 다리"다. 일반 PCB로는 불가능한 수만 핀 연결을 가능케 해 **TB/s급 메모리 대역폭**을 실현한다. "CoWoS 없으면 블랙웰 GPU도 그저 다이 조각 덩어리"일 뿐 → AI 칩의 필수 관문.

## 병목 — 왜 중요한가

> [!claim] 출처 기반 주장
> CoWoS 생산능력: 35K/월(2024) → 70K(2025) → 110K(2026)이지만 사실상 매진. [엔비디아](../entities/nvidia.md)가 50~60%를 선점. TSMC는 $56B 투자로 능력을 2배로 확대 추진. ※ 업계 추정, 분기별 변동.

> [!judgment] 내 판단
> AI 칩 부족의 진짜 원인은 GPU 다이가 아니라 **CoWoS 패키징 능력**인 경우가 많다. 따라서 AI 칩 공급 전망을 볼 때는 웨이퍼 capa가 아니라 CoWoS·[HBM](hbm.md) capa를 봐야 한다.

## 다음 학습 주제

- CoWoS(2.5D) vs SoIC(3D)의 차이 — [가치사슬 종합 §6](../syntheses/semiconductor-ai-chip-value-chain.md)

## 관련 페이지

- [반도체·AI 칩 가치사슬 종합](../syntheses/semiconductor-ai-chip-value-chain.md) §2.2
- [TSMC](../entities/tsmc.md) · [HBM](hbm.md) · [엔비디아](../entities/nvidia.md)
