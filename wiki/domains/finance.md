---
title: "Finance Domain Index"
created: 2026-05-02
updated: 2026-07-11
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
- [AI 신약 개발 — 발굴은 압축, 임상은 불변](../topics/ai-drug-discovery.md) — AI 신약 투자의 50:1 바이오벅스 비율, 임상 미입증을 시장이 가격에 반영 (`domain: ai, finance`, 2026-06)

---

## 내 판단 / 종합

내가 원칙+사실+의견을 종합해 내린 판단.

- [개인 투자자용 All Weather 변형](../syntheses/personal-all-weather-variant.md) — 레버리지 없이 4분면을 커버하는 개인용 포트폴리오
- [반도체·AI 칩 가치사슬 종합](../syntheses/semiconductor-ai-chip-value-chain.md) — 모래에서 AI 칩까지, 어디에 협상력·마진·해자가 집중되는가 (`domain: finance, ai`)
- [AI 데이터센터 전력 인프라 종합](../syntheses/ai-datacenter-power-infrastructure.md) — 발전~송배전 병목 + SemiAnalysis grid headroom/ELCC 보강; 병목 = 가격 결정력, 효율이 아니라 속도 (`domain: finance, ai`)
- [ECTC 2026 AI 반도체 시스템 공동설계 전환](../syntheses/ai-semiconductor-system-codesign-ectc-2026.md) — GPU 단품 성능에서 패키징·HBM·전력·냉각·네트워크 공동 최적화 경쟁으로 이동 (`domain: finance, ai`)

---

## 반도체·AI 칩 가치사슬 (`domain: finance, ai`)

AI 반도체 투자 판단을 위한 가치사슬 지도. 진입점은 위 [종합 페이지](../syntheses/semiconductor-ai-chip-value-chain.md).

- **기업**: [TSMC](../entities/tsmc.md) · [엔비디아](../entities/nvidia.md) · [브로드컴](../entities/broadcom.md) · [마벨](../entities/marvell.md) · [DeepSeek](../entities/deepseek.md)
- **기술/개념**: [EUV 노광(ASML)](../concepts/euv-lithography.md) · [CoWoS](../concepts/cowos.md) · [HBM](../concepts/hbm.md) · [CUDA](../concepts/cuda.md) · [SerDes](../concepts/serdes.md)
- **추론 효율 → HBM 수요**: [DSpark & Speculative Decoding](../concepts/speculative-decoding.md) — Decode 메모리 대역폭 병목과 HBM 수요 함수의 연결 (2026-06)
- **소재 시장**: [폴리실리콘 — 태양광 vs 반도체 분기](../topics/polysilicon.md)
- **빅테크 컴퓨트 수요**: [Meta Superintelligence — 1년 진행 업데이트](../topics/meta-superintelligence-1yr-progress.md) — Titan 클러스터 컴퓨트 램프, Hyperion SPV 오프밸런스시트 파이낸싱 (`confidence: low`, 2026-07)
- **시스템 공동설계**: [ECTC 2026 AI 반도체 시스템 공동설계 전환](../syntheses/ai-semiconductor-system-codesign-ectc-2026.md) — ECTC 2026/SemiAnalysis 기반 첨단 패키징·Custom HBM·직접 실리콘 냉각·광 인터커넥트 병목 정리
- **미·중 격차**: [중국 반도체 격차 — ASML EUV 의혹·SMIC/화웨이·DeepSeek V4 학습 칩](../topics/china-chip-gap-deepseek-v4.md) — 추론은 화웨이로, 사전학습은 엔비디아 의존 (2026-06)

---

## AI 데이터센터 전력 인프라 (`domain: finance, ai`)

AI 데이터센터의 전력 확보 경쟁을 발전→송배전→부하 가치사슬로 본 투자 지도. 진입점은 위 [종합 페이지](../syntheses/ai-datacenter-power-infrastructure.md).

- **발전 (가스터빈)**: [GE Vernova](../entities/ge-vernova.md)(빅3 1위) · [두산에너빌리티](../entities/doosan-enerbility.md)(납기 추격자)
- **발전 (연료전지)**: [Bloom Energy](../entities/bloom-energy.md)(SOFC, 변압기 우회)
- **송·배전 (전력기기)**: [LS일렉트릭](../entities/ls-electric.md)(K전력기기 빅3, 국내 DC ~70%)

---

## 관련 인물

- [Ray Dalio](../entities/ray-dalio.md) — Bridgewater 창립자, All Weather·Risk Parity·Big Cycle 제안자

---

## Watchlist 뉴스 로그는 여기 없다 (2026-08-07 분리)

> [!info] 루틴 뉴스는 `routine-news/` 로 완전히 빠졌다
> 예전에는 이 섹션에 watchlist 130여 종목의 뉴스 로그 링크가 나열되어 있었다. 그 링크는
> 대부분 이미 끊어져 있었고(`news/AAPL.md` 처럼 옛 파일명 그대로 남아 있었다),
> 검증되지 않은 `confidence: low` 자동 수집물이 도메인 인덱스의 절반을 차지하고 있었다.
>
> 이 도메인 인덱스는 이제 **내가 쓴 페이지만** 다룬다. 자동 수집 뉴스가 필요하면
> 최상위 `routine-news/` 폴더를 파일 탐색기에서 직접 연다 (옵시디언 검색·그래프에서는 제외되어 있다).
> 거기서 사실로 굳어진 항목만 사람이 검증해 `topics/` · `entities/` · `syntheses/` 로 승격하고,
> 그때 비로소 이 인덱스에 올라온다 — 뉴스 로그 파일을 링크하는 게 아니라 원 출처 URL 을 `sources:` 에 박는다.
