---
title: "Finance Domain Index"
created: 2026-05-02
updated: 2026-06-09
domain: finance
type: index
weight: foundational
confidence: high
tags: [도메인, 투자, 포트폴리오, 매크로, 금융]
sources: []
---

# Finance — 도메인 인덱스

투자, 포트폴리오, 자산배분, 매크로경제 관련 모든 페이지의 진입점.
**판단이 필요할 때 이 페이지에서 시작한다** — 원칙 → 프레임워크 → 데이터 → 내 판단 순으로 읽는다.

---

## 핵심 원칙 (최우선 참조)

의사결정의 1차 근거. 이것이 틀리면 결론이 바뀐다.

- [Risk Parity (위험 균형)](../principles/risk-parity.md) — 자산 금액이 아닌 위험 기여도를 균등하게 맞추는 자산배분 원리
- [2×2 경제 환경 프레임](../principles/economic-quadrants.md) — 성장/인플레 4분면, 시장 기대 대비 서프라이즈가 자산 가격을 결정한다

---

## 프레임워크 / 개념

세상을 설명하는 서술적 모델. 원칙을 이해하는 맥락.

- [Big Cycle (대순환)](../concepts/big-cycle.md) — Ray Dalio의 제국 흥망 500년 역사 패턴
- [레버리지와 파생상품](../concepts/leverage-and-derivatives.md) — 선물·스왑·레버리지 ETF의 메커니즘과 위험

---

## 전문가 주장 / 분석 (출처 기반, 검증 필요)

- [Ray Dalio - 세계대전과 Big Cycle 분석](../topics/ray-dalio-world-war-big-cycle.md) — 현재 세계 질서가 대전환점에 있다는 분석 (`confidence: medium`)
- [Ray Dalio All Weather Portfolio](../topics/all-weather-portfolio.md) — All Weather의 설계 원리와 실제 구성

---

## 내 판단 / 종합

내가 원칙+사실+의견을 종합해 내린 판단.

- [개인 투자자용 All Weather 변형](../syntheses/personal-all-weather-variant.md) — 레버리지 없이 4분면을 커버하는 개인용 포트폴리오
- [반도체·AI 칩 가치사슬 종합](../syntheses/semiconductor-ai-chip-value-chain.md) — 모래에서 AI 칩까지, 어디에 협상력·마진·해자가 집중되는가 (`domain: finance, ai`)

---

## 반도체·AI 칩 가치사슬 (`domain: finance, ai`)

AI 반도체 투자 판단을 위한 가치사슬 지도. 진입점은 위 [종합 페이지](../syntheses/semiconductor-ai-chip-value-chain.md).

- **기업**: [TSMC](../entities/tsmc.md) · [엔비디아](../entities/nvidia.md) · [브로드컴](../entities/broadcom.md) · [마벨](../entities/marvell.md)
- **기술/개념**: [EUV 노광(ASML)](../concepts/euv-lithography.md) · [CoWoS](../concepts/cowos.md) · [HBM](../concepts/hbm.md) · [CUDA](../concepts/cuda.md) · [SerDes](../concepts/serdes.md)
- **소재 시장**: [폴리실리콘 — 태양광 vs 반도체 분기](../topics/polysilicon.md)

---

## 관련 인물

- [Ray Dalio](../entities/ray-dalio.md) — Bridgewater 창립자, All Weather·Risk Parity·Big Cycle 제안자

---

## Watchlist 뉴스 로그 (루틴 자동 수집, `confidence: low`)

`indicator_dashboard` 의 `daily-market-analysis` 루틴이 매일 누적한다. **검증되지 않은 raw 상태이므로 `news/` 폴더로 격리**되어 있으며, 굳어진 사실만 사람이 직접 `topics/` 로 promote 한다. 자세한 규칙: [news/README.md](../news/README.md).

- [Watchlist News Dashboard](../news/_dashboard.md) — watchlist 전 종목 한눈에 보기 (섹터별, 요일별 라운드로빈)
- 개별 종목 로그는 `news/tickers/`에 격리한다. Finance 도메인 인덱스가 모든 기업 로그를 직접 링크하면 Obsidian graph에서 `finance` 중심의 거대한 중복 덩어리가 생기므로, 이 페이지에서는 대시보드만 진입점으로 둔다.
