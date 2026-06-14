"""
Update Luke_wiki for 2026-06-14 (Sunday) daily-market-analysis routine.
Sectors: 소비재 (10), 산업재/방산 (14), 통신/미디어 (10)
"""
import os, re
from pathlib import Path

WIKI = Path("/home/user/Luke_wiki/wiki/news")
TICKERS_DIR = WIKI / "tickers"
DATE = "2026-06-14"

# ── Ticker update data ────────────────────────────────────────────────────────
# Each entry: (ticker, company, sector_kr, competitors_str, narrative_score,
#              key_events_str, risks_str, news_claims, open_claim_today, open_claim_update)
#
# open_claim_update: dict mapping old claim text pattern → new status line
# news_claims: list of (source, claim_text, impact, category) tuples
# open_claim_today: new claim to add (or None)

DATA = {
  "WMT": {
    "company": "Walmart Inc.",
    "sector_kr": "소비재",
    "competitors": "COST, AMZN",
    "score": "+0.60",
    "key_events": "드론배달 7개 시장 신규 확장, 시총 $1조 돌파 임박 (YTD +37%), 월튼 가문 $2억 내부자 매도",
    "risks": "월튼 가문 대규모 매도 오버행, 아마존 식료품 경쟁 심화, 소비자 경기 둔화 시 방어주 쏠림 한계",
    "claims": [
      ("Walmart Newsroom, 2026-06-12", "드론배달 Wing 협력 통해 7개 추가 지역 확장 — 미국 내 총 22개 시장", "+", "product"),
      ("Reuters, 2026-06-13", "WMT 주가 사상 최고치 갱신, 시총 $1조 임박 — YTD +37%", "+", "other"),
      ("Bloomberg, 2026-06-13", "월튼 가문 최고가에 $2억 매도 — 내부자 차익실현 신호", "neutral", "other"),
    ],
    "competitors_context": "COST: 5월 순매출 +14.5% YoY, 회원 갱신률 92.9% 역대 최고 → 대형 유통 소비 수요 견조 확인\n- AMZN: Amazon Fresh 15개 신규 도시 2시간 배달 보장 확대 → WMT 이커머스 식료품과 직접 경쟁 심화",
    "old_claim_update": {"강한 실적에도 주가 하락은 소비 경기 고점": "refuted — 6/14 기준 WMT YTD +37%, $1조 시총 임박 → 단순 밸류에이션 조정으로 판정"},
    "new_claim": "드론배달 22개 시장 확장 + $1조 시총 임박 → 이커머스 리더십 프리미엄 지속될 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "COST": {
    "company": "Costco Wholesale",
    "sector_kr": "소비재",
    "competitors": "WMT",
    "score": "+0.55",
    "key_events": "5월 순매출 +14.5% YoY, 회원 갱신률 92.9% 역대 최고, Oppenheimer Outperform 재확인 목표가 $975",
    "risks": "밸류에이션 프리미엄 (P/E 55x), 소비 경기 둔화 시 트래픽 감소 가능성, WMT 드론배달 확장으로 경쟁 심화",
    "claims": [
      ("Costco IR, 2026-06-14", "5월 순매출 +14.5% — 회원제 갱신률 92.9% 역대 최고, 트래픽 +9%", "+", "earnings"),
      ("Oppenheimer, 2026-06-14", "3분기 EPS $4.02 컨센서스 상회, Outperform 재확인 — 목표가 $975", "+", "earnings"),
    ],
    "competitors_context": "WMT: 드론배달 7개 시장 확장, 시총 $1조 임박 → 대형 유통 소비 수요 견조 COST도 공유",
    "old_claim_update": {"COST 실적 서프라이즈에도 주가 하락": "refuted — 5월 매출 +14.5% 서프라이즈로 성장 모멘텀 유효 확인, 소비 둔화보다 단기 밸류에이션 조정"},
    "new_claim": "회원 갱신률 92.9% 역대 최고 — 경기 불확실성에도 COST 해자 강화 추세 지속될 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "KO": {
    "company": "The Coca-Cola Company",
    "sector_kr": "소비재",
    "competitors": "PEP",
    "score": "+0.52",
    "key_events": "2026 FIFA 월드컵 공식 음료 파트너 확정, 인도 보틀링 법인 2027 IPO 추진, Morgan Stanley 목표가 $89 상향",
    "risks": "달러 강세로 신흥시장 매출 환산 손실, 설탕세 강화 규제 글로벌 확산, 무설탕 경쟁 심화",
    "claims": [
      ("FIFA / Coca-Cola IR, 2026-06-14", "2026 FIFA 월드컵 공식 음료 파트너 — 미국·캐나다·멕시코 공동 개최로 글로벌 노출 최대", "+", "product"),
      ("Bloomberg, 2026-06-13", "인도 보틀링 법인 2027년 IPO 추진 — 신흥시장 성장 자본화 전략", "+", "other"),
      ("Morgan Stanley, 2026-06-14", "목표가 $89 상향 — 월드컵 마케팅 레버리지와 신흥시장 성장 근거", "+", "other"),
    ],
    "competitors_context": "PEP: 북미 음료 판매량 -2.5% YoY, 스낵 가격 최대 15% 인하 → KO 북미 음료 상대적 경쟁 우위 부각",
    "old_claim_update": {},
    "new_claim": "FIFA 월드컵 마케팅이 KO 글로벌 브랜드 모멘텀과 신흥시장 점유율 확대로 이어질 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "PEP": {
    "company": "PepsiCo, Inc.",
    "sector_kr": "소비재",
    "competitors": "KO",
    "score": "+0.23",
    "key_events": "북미 음료 판매량 -2.5% YoY, 스낵 가격 최대 15% 인하 결정, Q2 실적 발표 7월 9일 예정",
    "risks": "가격 인하로 마진율 추가 압박, 건강 트렌드 가속화로 전통 음료·스낵 장기 수요 감소, KO FIFA 파트너십 대비 브랜드 노출 열위",
    "claims": [
      ("PepsiCo IR, 2026-06-14", "북미 음료 판매량 -2.5% — 소비자 가격 저항과 건강 트렌드로 전통 탄산 수요 둔화", "-", "earnings"),
      ("WSJ, 2026-06-14", "스낵 부문 가격 최대 15% 인하 — 판매량 회복 시도, 단기 마진 압박 불가피", "-", "product"),
    ],
    "competitors_context": "KO: 2026 FIFA 월드컵 공식 음료 파트너 확정 → PEP 글로벌 음료 브랜드 노출 열위",
    "old_claim_update": {},
    "new_claim": "스낵 15% 가격 인하가 판매량 회복으로 이어질 것인가 vs 마진 악화만 남을 것인가 (7월 9일 Q2 실적에서 확인)",
    "verified_fact": None,
  },
  "PG": {
    "company": "Procter & Gamble Co.",
    "sector_kr": "소비재",
    "competitors": "",
    "score": "+0.42",
    "key_events": "UBS 목표가 $172 상향, Native Surf Club Gen Z 브랜드 론칭, 주간 +5.4% 소비재 로테이션 수혜",
    "risks": "신흥시장 환율 역풍 (달러 강세), 원자재 비용 재상승 시 마진 압박, Gen Z 신제품 시장 침투율 불확실",
    "claims": [
      ("UBS, 2026-06-14", "목표가 $172로 상향 — 가격 전가력 회복과 신흥시장 볼륨 반등 근거", "+", "other"),
      ("P&G Newsroom, 2026-06-14", "Native Surf Club 브랜드 론칭 — Gen Z 자연주의 퍼스널케어 시장 공략", "+", "product"),
    ],
    "competitors_context": "",
    "old_claim_update": {},
    "new_claim": "Gen Z 신제품 Native Surf Club이 프리미엄 소비재 시장 침투에 성공할 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "MO": {
    "company": "Altria Group, Inc.",
    "sector_kr": "소비재",
    "competitors": "",
    "score": "+0.28",
    "key_events": "on! PLUS 니코틴 파우치 신규 출시, 배당락일 6월 15일 — 분기 $1.06, FDA NJOY 멘톨 금지 지속",
    "risks": "담배 소비량 구조적 감소 추세, FDA 추가 규제 확대 가능성, 연기 없는 제품 경쟁 심화",
    "claims": [
      ("Altria IR, 2026-06-14", "on! PLUS 니코틴 파우치 신규 향 추가 전국 출시 — 연기 없는 제품 포트폴리오 확대", "+", "product"),
      ("Altria IR, 2026-06-14", "배당락일 6월 15일 — 분기 배당 $1.06, 연간 배당수익률 ~8.3%", "+", "other"),
      ("Reuters, 2026-06-14", "FDA NJOY 멘톨 금지 지속 — MO 직접 영향 제한적이나 규제 불확실성 상존", "-", "regulation"),
    ],
    "competitors_context": "",
    "old_claim_update": {},
    "new_claim": "on! PLUS 신규 출시가 연기 없는 제품 점유율 확대로 이어질 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "MCD": {
    "company": "McDonald's Corporation",
    "sector_kr": "소비재",
    "competitors": "SBUX",
    "score": "+0.57",
    "key_events": "FIFA 월드컵 글로벌 마케팅 캠페인 론칭, AI 드라이브스루 정확도 90% — 500개 매장, Q1 동일매장 +9.4% 어닝 서프라이즈",
    "risks": "소비자 절약 트렌드로 외식 지출 감소 가능성, 원자재(소고기·포장재) 비용 재상승, 글로벌 지역별 동일매장 편차 심화",
    "claims": [
      ("McDonald's IR, 2026-06-14", "FIFA 월드컵 글로벌 캠페인 론칭 — McDelivery 프로모션·한정 메뉴로 Q2-Q3 매출 견인 기대", "+", "product"),
      ("CNBC, 2026-06-13", "AI 드라이브스루 주문 정확도 90% 달성 — 500개 매장 확대 후 인건비 절감 효과 가시화", "+", "product"),
      ("McDonald's IR, 2026-06-14", "Q1 글로벌 동일 매장 +9.4% — 앱 기반 충성 고객 증가 효과", "+", "earnings"),
    ],
    "competitors_context": "SBUX: 일본 지분 매각·IPO 검토 ($2.5B) + 중국 60% 알리바바 JV 매각 완료 ($4B) → SBUX 구조 개편으로 커피 포지션 불확실 — MCD McCafé 틈새 기회",
    "old_claim_update": {},
    "new_claim": "FIFA 월드컵 캠페인 + AI 드라이브스루 90%가 Q2-Q3 동일매장 성장 가속으로 이어질 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "HD": {
    "company": "The Home Depot, Inc.",
    "sector_kr": "소비재",
    "competitors": "",
    "score": "+0.44",
    "key_events": "Q1 매출 $41.8B (+4.8%) 가이던스 유지, 미국 기존 주택 거래 2022년 이후 최고, Pro 세그먼트 5분기 연속 DIY 상회",
    "risks": "모기지 금리 재상승 시 주택 시장 위축, 관세로 수입 건자재 비용 상승, SRS Distribution 인수 통합 비용",
    "claims": [
      ("Home Depot IR, 2026-06-14", "Q1 매출 $41.8B (+4.8%), Pro 고객 매출 +9% — 연간 가이던스 유지", "+", "earnings"),
      ("NAR, 2026-06-14", "미국 기존 주택 거래량 2022년 이후 최고 — 모기지 금리 6.7%로 소폭 하락 효과", "+", "macro"),
    ],
    "competitors_context": "",
    "old_claim_update": {},
    "new_claim": "주택 거래 회복과 Pro 고객 강세가 하반기 동일매장 성장 회복으로 이어질 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "NKE": {
    "company": "NIKE, Inc.",
    "sector_kr": "소비재",
    "competitors": "",
    "score": "-0.27",
    "key_events": "RBC Sector Perform 하향 — 목표가 $50, YTD -30.3% 언더퍼폼 지속, Q4 실적 발표 6월 30일",
    "risks": "중국 회복 지연 — 현지 브랜드 리닝·안타 약진, 직접판매(DTC) 전략 과도로 채널 파트너 이탈, 재고 증가로 추가 할인 마진 압박",
    "claims": [
      ("RBC Capital Markets, 2026-06-14", "투자의견 Sector Perform 하향, 목표가 $50 — 중국 회복 지연·직접판매 전략 리스크", "-", "other"),
      ("Reuters, 2026-06-14", "YTD -30.3% — 브랜드 리셋 중 채널 재편·디지털 직판 전략 혼선 지속", "-", "other"),
    ],
    "competitors_context": "",
    "old_claim_update": {"월드컵 중심 턴어라운드": "pending — 6/14 기준 RBC 투자의견 추가 하향, Q4 실적 6/30에서 첫 확인 필요"},
    "new_claim": "Q4 실적 6월 30일 — 채널 정상화·브랜드 리셋 효과가 수치로 확인될 것인가 (6/30 실적에서 판단)",
    "verified_fact": None,
  },
  "SBUX": {
    "company": "Starbucks Corporation",
    "sector_kr": "소비재",
    "competitors": "MCD",
    "score": "+0.29",
    "key_events": "일본 지분 매각·IPO 검토 ($2.5B), 중국 60% 지분 알리바바 JV 매각 완료 ($4B), YTD +22.7% 턴어라운드 모멘텀",
    "risks": "중국·일본 지분 매각 후 성장 엔진 약화 우려, 북미 동일매장 매출 회복 속도 불확실, MCD McCafé 등 저가 커피 경쟁 심화",
    "claims": [
      ("FT, 2026-06-14", "일본 사업 지분 매각·IPO 검토 — 최대 $25억 조달 목표, 자본 효율화 전략", "+", "m&a"),
      ("Reuters, 2026-06-14", "중국 사업 60% 지분 알리바바 JV에 $40억 매각 완료 — 현금 유입 및 운영 리스크 분산", "+", "m&a"),
    ],
    "competitors_context": "MCD: FIFA 월드컵 글로벌 캠페인 론칭 → 패스트푸드 커피 소비 유도로 SBUX 프리미엄 포지션 경쟁",
    "old_claim_update": {"AI 재고관리 폐기·기관 41.9% 매도·1개월 -9%": "refuted — 6/14 기준 YTD +22.7% 강세로 Brian Niccol 턴어라운드 신뢰도 회복"},
    "new_claim": "중국·일본 자산 구조조정 완료 후 북미 동일매장 회복이 YTD 강세를 정당화할 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "CAT": {
    "company": "Caterpillar Inc.",
    "sector_kr": "산업재 / 방산",
    "competitors": "DE",
    "score": "+0.53",
    "key_events": "AI 데이터센터 2GW 전력 컨소시엄 참여, 수주잔고 $62.7B 역대 최고, 배당 8% 인상",
    "risks": "관세로 해외 매출 환산 감소, 광산 투자 사이클 정점 이후 수요 감소 우려, 중국 인프라 투자 둔화",
    "claims": [
      ("CAT IR, 2026-06-14", "GE·HON과 AI 데이터센터 2GW 전력 인프라 컨소시엄 참여 — 비상발전·UPS 장기 수주 기반", "+", "product"),
      ("CAT IR, 2026-06-14", "수주잔고 역대 최고 $62.7B 달성, 배당 8% 인상 — 중장기 성장 신뢰도 확인", "+", "earnings"),
    ],
    "competitors_context": "DE: 건설장비 +29% YoY 서프라이즈이나 대형 농기계 부진·관세 $1.2B → CAT 건설기계 동반 수요 확인, 채굴장비는 독보적 강세",
    "old_claim_update": {},
    "new_claim": "AI 데이터센터 전력 컨소시엄이 CAT 비상발전 장기 수주 가시화될 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "DE": {
    "company": "Deere & Company",
    "sector_kr": "산업재 / 방산",
    "competitors": "CAT",
    "score": "+0.11",
    "key_events": "건설장비 +29% YoY 서프라이즈, FY26 관세 비용 $1.2B 추정, 대형 농기계 수요 부진 지속",
    "risks": "글로벌 곡물 가격 추가 하락 시 농기계 수요 급감, 관세 비용 마진 압박 심화, 중국 농업 보조금 정책 변화",
    "claims": [
      ("Deere IR, 2026-06-14", "건설장비 매출 +29% YoY — 인프라 지출 수혜, 대형 농기계는 부진 지속", "+", "earnings"),
      ("WSJ, 2026-06-14", "FY26 관세 비용 $12억 추정 — 철강·부품 관세로 대형 농기계 마진 압박", "-", "macro"),
    ],
    "competitors_context": "CAT: 수주잔고 $62.7B 역대 최고, 배당 8% 인상 → DE 건설기계 동반 수요 확인",
    "old_claim_update": {},
    "new_claim": "건설장비 +29% 강세가 지속될 것인가 vs 관세 $1.2B 역풍이 대형 농기계 둔화와 겹쳐 전체 어닝 압박 (7일 검증 대기)",
    "verified_fact": None,
  },
  "BA": {
    "company": "The Boeing Company",
    "sector_kr": "산업재 / 방산",
    "competitors": "LMT, RTX, NOC",
    "score": "+0.02",
    "key_events": "5월 인도 60대 (+28% MoM), 777X 신규 조립 라인 가동, $9.85억 우간다항공 수주",
    "risks": "737 MAX 품질 감시 지속 — FAA 생산 cap 유지, 부채 $57B 재무 부담으로 신규 투자 여력 제한, 에어버스 대비 가격·납기 경쟁력 열위",
    "claims": [
      ("Boeing IR, 2026-06-14", "5월 인도 60대 (+28% MoM) — 생산 정상화 진행 중이나 737 MAX 누적 백로그 여전", "+", "other"),
      ("Bloomberg, 2026-06-13", "777X 신규 조립 라인 에버렛 공장 가동 시작 — 7월 1호기 출고 목표", "+", "product"),
    ],
    "competitors_context": "LMT: 주간 $100억 수주 행진 → BA 방산 부문 방어예산 확대 공유\nNOC: B-21 생산율 25% 확대 $4.5B 투자 → 차세대 항공기 예산 경쟁 관계",
    "old_claim_update": {},
    "new_claim": "777X 7월 1호기 출고 달성 여부 — 생산 정상화 속도가 시장 신뢰 회복의 선행 지표 (7일 검증 대기)",
    "verified_fact": None,
  },
  "LMT": {
    "company": "Lockheed Martin Corp.",
    "sector_kr": "산업재 / 방산",
    "competitors": "RTX, NOC, BA",
    "score": "+0.62",
    "key_events": "주간 PAC-3·F-35·MH-60R 계약 합계 ~$100억, $5.14억 우주군 위성 계약, Deutsche Bank Buy 업그레이드 목표가 $610",
    "risks": "F-35 공급망 병목으로 인도 지연, 방산 예산 지속성 — 정치 사이클 의존, 원가 초과(cost overrun) 고정가 계약 리스크",
    "claims": [
      ("DoD / LMT IR, 2026-06-14", "PAC-3 미사일·F-35·MH-60R 등 주간 계약 합계 약 $100억 — 미사일방어 수요 급증", "+", "earnings"),
      ("DoD, 2026-06-14", "$5.14억 우주군 위성 계약 — 우주 인프라 포트폴리오 확장", "+", "earnings"),
      ("Deutsche Bank, 2026-06-14", "Buy 업그레이드, 목표가 $610 — 유럽 재무장 사이클 직접 수혜 근거", "+", "other"),
    ],
    "competitors_context": "RTX: $5.15억 SPY-6 레이더 양산 계약 → 미사일방어 예산 확대로 LMT PAC-3와 동반 수혜\nNOC: B-21 생산율 25% 확대 → 방산 예산 확대 공유",
    "old_claim_update": {},
    "new_claim": "주간 $100억 수주 행진이 FY2026 전체 수주잔고 사상 최고 갱신으로 이어질 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "RTX": {
    "company": "RTX Corporation",
    "sector_kr": "산업재 / 방산",
    "competitors": "LMT, NOC, BA",
    "score": "+0.57",
    "key_events": "$5.15억 SPY-6 레이더 양산 계약, $1억 LTAMDS 레이더 생산시설 개소, DBS Buy 업그레이드 목표가 $145",
    "risks": "Pratt & Whitney GTF 엔진 리콜 비용 잔존, 방산 공급망 인력 부족 생산 병목, 금리 상승으로 정부 조달 예산 압박",
    "claims": [
      ("DoD, 2026-06-14", "$5.15억 육군 SPY-6 레이더 양산 계약 — 이지스 방어 업그레이드 수요 강화", "+", "earnings"),
      ("RTX IR, 2026-06-14", "$1억 LTAMDS 레이더 생산시설 개소 — 다중위협 대응 미사일방어 용량 확대", "+", "product"),
      ("DBS, 2026-06-14", "Buy 업그레이드 목표가 $145 — NATO 재무장 사이클 방산전자 직접 수혜", "+", "other"),
    ],
    "competitors_context": "LMT: PAC-3 ~$100억 수주 강세 → 미사일방어 예산 확대로 RTX SPY-6 레이더와 동반 수혜\nNOC: B-21 생산 가속 → RTX P&W 엔진 수요 간접 자극",
    "old_claim_update": {},
    "new_claim": "LTAMDS 신시설과 SPY-6 양산이 RTX 방산전자 마진율 개선으로 이어질 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "NOC": {
    "company": "Northrop Grumman Corp.",
    "sector_kr": "산업재 / 방산",
    "competitors": "LMT, RTX, BA",
    "score": "+0.52",
    "key_events": "B-21 레이더 73일 비행시험 완료 (180일 목표 순항), B-21 생산율 25% 확대 $4.5B 투자, 분기 배당 +6.9% → $2.30",
    "risks": "B-21 프로그램 고정가 계약 원가 초과 리스크, Space 세그먼트 위성 지연 여파, 정부 지속적 예산 해결 지연 리스크",
    "claims": [
      ("Northrop IR / Air Force, 2026-06-14", "B-21 레이더 73일 비행시험 완료 — 180일 목표 순항 중, FAA 인증 일정 유지", "+", "product"),
      ("Bloomberg, 2026-06-13", "B-21 생산율 25% 확대 계획 — $45억 투자로 팜데일 시설 증설, 2027년 납기 가속", "+", "earnings"),
      ("NOC IR, 2026-06-14", "분기 배당 +6.9% → $2.30 — 주주환원 지속 의지 확인", "+", "other"),
    ],
    "competitors_context": "LMT: $100억 수주 + DB Buy 업그레이드 → 방산 예산 확대 공유로 NOC B-21 예산도 동반 수혜\nRTX: LTAMDS·SPY-6 강세 → 방산전자 투자 확대로 NOC B-21 생산 병행 가속",
    "old_claim_update": {},
    "new_claim": "B-21 생산율 25% 확대 $4.5B 투자가 2027년 납기 가속으로 이어질 것인가 (7일 검증 대기)",
    "verified_fact": None,
  },
  "HON": {
    "company": "Honeywell International Inc.",
    "sector_kr": "산업재 / 방산",
    "competitors": "GE, RTX",
    "score": "+0.44",
    "key_events": "HONA 스핀오프 6월 29일 확정 (1:2 역분할), 배당락일 6월 15일 — 분기 $1.13, 2026 연간 가이던스 유지",
    "risks": "스핀오프 후 HON 항공우주 집중 구조에서 성장 다변화 약화, 항공 여행 수요 감소 시 항공우주 노출 리스크, HON·HONA 분리 비용 예상 초과",
    "claims": [
      ("Honeywell IR, 2026-06-14", "HONA 스핀오프 6월 29일 확정 — 주식 1:2 역분할 비율 공개, HON 주주에 HONA 주식 배분", "+", "other"),
      ("Honeywell IR, 2026-06-14", "배당락일 6월 15일 — 분기 배당 $1.13, HONA 스핀오프 전 마지막 합산 배당", "+", "other"),
      ("Honeywell IR, 2026-06-14", "2026 연간 가이던스 유지 — 스핀오프 분리 비용 반영 후에도 EPS 가이던스 불변", "+", "earnings"),
    ],
    "competitors_context": "GE: Q1 수주 +87% → $23B, LEAP 엔진 인도 +63% → HON 항공 소재·시스템 부문 간접 수요 유발\nRTX: LTAMDS·방산전자 투자 확대 → HON 방산 소재 공급 수요 증가로 연결",
    "old_claim_update": {"Honeywell Aerospace 분사 기준일 6/15·완료 6/29": "verified — HONA 스핀오프 6/29 확정, 배당락일 6/15 공식 발표"},
    "new_claim": "HONA 스핀오프 완료 후 HON 항공우주 집중 구조에서 마진 개선이 실현될 것인가 (6/29 스핀오프 완료 후 확인)",
    "verified_fact": "HONA 스핀오프 6월 29일 완료 확정, 기준일(배당락) 6월 15일, 1:2 역분할 비율 공식 발표 (Honeywell IR, 2026-06-14)",
  },
  "GE": {
    "company": "GE Aerospace",
    "sector_kr": "산업재 / 방산",
    "competitors": "RTX, HON, BA",
    "score": "+0.41",
    "key_events": "Q1 수주 +87% → $23B, LEAP 엔진 인도 +63%, Wolfspeed SiC MOU + $1B 미국 제조 투자",
    "risks": "항공사 수요 둔화 시 LEAP 신규 주문 감소, 공급망 부품 부족으로 인도 지연 리스크, SiC 기술 개발 지연으로 차세대 로드맵 밀림",
    "claims": [
      ("GE Aerospace IR, 2026-06-14", "Q1 수주 +87% → $23B, LEAP 엔진 인도 +63% — 항공 여행 회복 수요 폭증 수혜", "+", "earnings"),
      ("GE Aerospace, 2026-06-14", "Wolfspeed과 SiC 전력모듈 MOU — 차세대 하이브리드 전기 항공기 전력계통 공동 개발", "+", "product"),
    ],
    "competitors_context": "RTX: P&W 엔진·LTAMDS 방산전자 확장 → GE LEAP 엔진과 민간항공 시장 양강 체제 확인\nHON: 스핀오프 후 항공우주 집중 → GE 항공부품 공급망에 긍정적",
    "old_claim_update": {},
    "new_claim": "LEAP 엔진 인도 +63% 폭증이 지속될 것인가 vs 공급망 병목으로 둔화 (7일 검증 대기)",
    "verified_fact": None,
  },
  "UPS": {
    "company": "United Parcel Service, Inc.",
    "sector_kr": "산업재 / 방산",
    "competitors": "FDX, AMZN",
    "score": "-0.16",
    "key_events": "30,000명 감원·24개 시설 폐쇄, 아마존 물량 50%+ 감소 확인, 국제 부문 +6% YoY 견조",
    "risks": "아마존 물량 이탈 구조적 — 대체 화주 확보 시간 필요, 인건비 구조 고정화로 단기 수익성 압박, 경기 둔화 시 B2B 물량 추가 감소",
    "claims": [
      ("UPS IR, 2026-06-14", "30,000명 감원·24개 시설 폐쇄 — USPS 계약 종료와 아마존 물량 감소에 대응한 비용 구조 재편", "-", "earnings"),
      ("WSJ, 2026-06-14", "아마존 물량 50%+ 감소 — 아마존 자체 배송망(AMZ Logistics) 내재화 완료 여파", "-", "other"),
    ],
    "competitors_context": "FDX: Freight 스핀오프 완료, 조종사 합의 타결 → FDX 구조 단순화로 UPS와 기업 화주 시장 경쟁 심화 예상\nAMZN: Amazon Logistics 자체 배송망 완성 → UPS 핵심 물량 이탈 구조적 원인",
    "old_claim_update": {"아마존 물량 50%+ 감축 가속·화물기 사고 조사": "verified — 아마존 물량 50%+ 감소 확정, 30,000명 감원·24개 시설 폐쇄로 구조적 대응 착수"},
    "new_claim": "30,000명 감원·시설 폐쇄가 수익성 회복으로 이어지는 시점은 언제인가 (Q2 실적에서 확인)",
    "verified_fact": "UPS 30,000명 감원 및 24개 시설 폐쇄 결정 공식 발표 — 아마존 물량 50%+ 감소에 대응한 구조조정 (UPS IR / WSJ, 2026-06-14)",
  },
  "FDX": {
    "company": "FedEx Corporation",
    "sector_kr": "산업재 / 방산",
    "competitors": "UPS, AMZN",
    "score": "+0.13",
    "key_events": "FedEx Freight 독립 상장 완료 (NYSE: FDXF)",
    "risks": "아마존 자체 배송 확장으로 e커머스 물량 구조적 감소, 유가 상승 시 항공 연료비 마진 압박, 경기 침체 시 국제 특급 물량 감소",
    "claims": [
      ("FedEx IR, 2026-06-14", "FedEx Freight 독립 상장 완료 (NYSE: FDXF) — FDX는 특급·국제 물류 집중 구조로 재편", "+", "other"),
      ("Reuters, 2026-06-09", "ALPA 조종사 잠정 합의 타결 — 파업 리스크 해소, 운영 안정성 확보", "+", "other"),
    ],
    "competitors_context": "UPS: 30,000명 감원·24개 시설 폐쇄 → UPS 구조조정으로 FDX가 기업 화주 물량 흡수 기회\nAMZN: Amazon Logistics 완성 → FDX는 아마존 의존도 낮아 직접 영향 제한",
    "old_claim_update": {"연간 가이던스 상향·분사 계획 발표": "verified — FedEx Freight 스핀오프 NYSE:FDXF로 독립 상장 완료 (2026-06-01)"},
    "new_claim": "Freight 스핀오프 완료 후 FDX 핵심 사업 마진이 개선될 것인가 (Q4 FY2026 실적에서 확인)",
    "verified_fact": "FedEx Freight 스핀오프 완료 — NYSE:FDXF로 독립 상장 시작 (2026-06-01), ALPA 조종사 합의 타결 (2026-06-09)",
  },
}

# AVAV and KTOS need new files
AVAV_DATA = {
  "company": "AeroVironment, Inc.",
  "sector_kr": "산업재 / 방산",
  "competitors": "KTOS, LMT, NOC",
  "description": "소모성 드론·배회폭탄 퓨어플레이. Switchblade 300/600 배회폭탄과 P550 JUMP UAS 운용. BlueHalo 인수로 대드론·레이저·우주 영역 확장. 美 '드론 우위(Drone Dominance)' 조달 정책의 직접 수혜주.",
  "score": "+0.42",
  "key_events": "$1.17억 P550 JUMP UAS 육군 양산 계약, 대만 Ubiqconn Switchblade 수출 MOU, Switchblade 연내 500% 증산 목표",
  "risks": "소모성 드론 생산 병목으로 납기 지연 가능, 중국제 드론 저가 경쟁 심화, 수출 규제 변화로 대만 MOU 실행 지연",
  "claims": [
    ("AeroVironment IR / DoD, 2026-06-14", "$1.173억 P550 JUMP UAS 육군 양산 계약 — 소형 드론 배회폭탄 수요 급증 직접 수혜", "+", "earnings"),
    ("Reuters, 2026-06-14", "대만 Ubiqconn과 Switchblade 드론 수출 MOU — 인도태평양 방어망 확대 핵심", "+", "product"),
    ("Bloomberg, 2026-06-13", "Switchblade 300/600 생산량 연내 500% 증산 목표 — 우크라이나·대만 수요 반영", "+", "product"),
  ],
  "competitors_context": "KTOS: JPM Overweight 업그레이드, 해병대 CCA 공식 선정 → AVAV 소형 드론과 KTOS 대형 CCA 드론 — 무인기 예산 양극화로 상호보완\nLMT: 주간 ~$100억 수주 → 방산 예산 확대가 AVAV 소형 드론 공급망 수요 간접 자극",
  "new_claim": "$1.2억 P550 수주와 Switchblade 500% 증산이 AVAV 분기 매출 최고치 경신으로 이어질 것인가 (7일 검증 대기)",
}

KTOS_DATA = {
  "company": "Kratos Defense & Security Solutions, Inc.",
  "sector_kr": "산업재 / 방산",
  "competitors": "AVAV, NOC, GE",
  "description": "저가 소모성 무인전투기(CCA) 퓨어플레이. XQ-58A Valkyrie 스텔스 드론·표적드론·Spartan 소형 제트엔진 전문. 해병대 CCA 공식 프로그램 선정으로 대량생산 진입. '소모 가능한 무인 윙맨' 테마의 핵심 상장주.",
  "score": "+0.48",
  "key_events": "JPMorgan Overweight 업그레이드 목표가 $82, Spartan 소형 제트엔진 3,000대 생산 달성, 해병대 CCA 공식 프로그램 선정",
  "risks": "CCA 프로그램 예산 승인 지연 리스크, XQ-58 고정가 계약 원가 초과 가능성, 경쟁사 (Boeing MQ-28 등) 수주 리스크",
  "claims": [
    ("JPMorgan, 2026-06-14", "JP모간 Overweight 업그레이드, 목표가 $82 — XQ-58 CCA 프로그램 규모 확대 기대", "+", "other"),
    ("Kratos IR, 2026-06-14", "Spartan 소형 제트엔진 누적 3,000대 생산 달성 — 저가 무인기 엔진 공급 능력 확인", "+", "product"),
    ("DoD / USMC, 2026-06-14", "해병대 CCA(협동 전투기) 공식 프로그램 기록 선정 — 대규모 양산 계약 기반 확보", "+", "earnings"),
  ],
  "competitors_context": "AVAV: $1.17억 P550 수주, 500% 증산 → AVAV 소형 드론과 KTOS CCA 대형 드론 상호보완 — 무인기 예산 확대로 동반 수혜\nNOC: B-21 생산 가속 → NOC 표적드론·소모성 윙맨 수요 간접 자극",
  "new_claim": "해병대 CCA 공식 선정이 구체적인 양산 계약 규모와 일정으로 가시화될 것인가 (7일 검증 대기)",
}

# Korean defense stocks
DATA["012450.KS"] = {
  "company": "Hanwha Aerospace",
  "sector_kr": "산업재 / 방산",
  "competitors": "079550.KS, 042660.KS, LMT",
  "score": "-0.28",
  "key_events": "대전 2사업장 폭발사고 5명 사망, CEO 중대재해처벌법 위반 혐의 입건, 9개 사업장 안전점검 일시 중단",
  "risks": "수출 납기 차질 — 폴란드·루마니아 계약 이행 리스크, 추가 사상자 발생 시 형사 책임 확대, 기업 이미지 손상으로 신규 수주 경쟁력 약화",
  "claims": [
    ("연합뉴스, 2026-06-14", "대전 2사업장 폭발 사고로 5명 사망 — 중대재해처벌법 위반 혐의 CEO 입건", "-", "regulation"),
    ("한국경제, 2026-06-14", "CEO 입건 및 전국 9개 사업장 안전점검 강제 중단 — K9 자주포·천무 납기 차질 우려", "-", "regulation"),
    ("매일경제, 2026-06-14", "방사청 계약 이행 긴급 점검 — 폴란드·루마니아 수출 납기 영향 여부 확인 중", "-", "regulation"),
  ],
  "competitors_context": "079550.KS: UAE 천궁-II 92% 요격 성공, 말레이시아 해궁 $9,400만 수출 → 경쟁사 강세로 한화에어로 사고로 인한 K-방산 이미지 손상 부분 상쇄\nLMT: 주간 $100억 수주 강세 → 글로벌 방산 수요 견조 확인 — 한화에어로 차질 기간 일부 대체 수요 이동 가능",
  "old_claim_update": {},
  "new_claim": "폭발 사고로 9개 사업장 중단 — 폴란드·루마니아 수출 납기가 실제로 차질을 빚을 것인가 (30일 추적 필요)",
  "verified_fact": "대전 2사업장 폭발사고 5명 사망, CEO 중대재해처벌법 위반 혐의 입건, 9개 사업장 일시 운영 중단 (연합뉴스·한국경제, 2026-06-14)",
}

DATA["079550.KS"] = {
  "company": "LIG Nex1",
  "sector_kr": "산업재 / 방산",
  "competitors": "012450.KS, LMT, RTX",
  "score": "+0.53",
  "key_events": "천궁-II UAE 실전 92% 요격 성공률, 말레이시아 해궁 $9,400만 수출 계약, LIG Defense & Aerospace 리브랜딩",
  "risks": "UAE 실전 성능 추가 검증 필요 — 샘플 사례로 일반화 한계, 원화 강세로 수출 수익 환산 감소, 차기 대형 수출 계약 파이프라인 구체화 지연",
  "claims": [
    ("연합뉴스, 2026-06-14", "UAE 실전 운용 중 드론·순항미사일 요격 성공률 92% — 글로벌 방산 시장 레퍼런스 확보", "+", "product"),
    ("매일경제, 2026-06-14", "말레이시아 해군 해궁 $9,400만 수출 계약 체결 — 동남아 해군 무기 수출 첫 사례", "+", "earnings"),
    ("한국경제, 2026-06-14", "LIG Defense & Aerospace로 리브랜딩 — 중형무인기·대드론·우주 부문 전략적 확장 공식화", "+", "other"),
  ],
  "competitors_context": "012450.KS: 대전 폭발 5명 사망, CEO 입건 → 경쟁사 사업 차질로 LIG Nex1 K-방산 수출 브랜드 상대적 부각\nRTX: $5.15억 SPY-6 수주 → 미사일방어 예산 확대 배경 공유로 천궁 수요도 동반 강화",
  "old_claim_update": {},
  "new_claim": "UAE 92% 요격 성공 레퍼런스가 중동·동남아 추가 수출 계약으로 이어질 것인가 (7일 검증 대기)",
  "verified_fact": "천궁-II UAE 실전 배치 92% 요격 성공률 확인 (연합뉴스, 2026-06-14), 말레이시아 해군 해궁 $9,400만 수출 계약 체결 (매일경제, 2026-06-14)",
}

# Telecom/Media
DATA["VZ"] = {
  "company": "Verizon Communications Inc.",
  "sector_kr": "통신 / 미디어",
  "competitors": "T, TMUS",
  "score": "+0.44",
  "key_events": "Frontier 인수 완료 — 광케이블 3,000만+ 가구, 3대 통신사 위성-셀룰러 JV 출범, 기업 광케이블 매출 +12% YoY",
  "risks": "Frontier 통합 비용 및 고객 이탈 리스크, TMUS 모바일 가격 경쟁으로 무선 수익 압박, 금리 유지로 인프라 투자 이자 부담",
  "claims": [
    ("Verizon IR, 2026-06-14", "Frontier 인수 완료 — 광케이블 통과 가구 3,000만+ 달성, 미국 최대 광네트워크 사업자", "+", "m&a"),
    ("Reuters, 2026-06-10", "Verizon·T-Mobile·AT&T 3대 통신사 위성-셀룰러 JV 설립 — 농촌·재난 지역 커버리지 공백 해소", "+", "product"),
    ("Verizon IR, 2026-06-14", "기업 광케이블 매출 +12% YoY — AI 데이터센터 연결 수요 급증 수혜", "+", "earnings"),
  ],
  "competitors_context": "T: Q1 광케이블 순증 584K 역대 최고 → VZ Frontier 통합 경쟁 압박 — 광케이블 시장 양강 체제 형성\nTMUS: Q1 EPS 비트, FWA 500K+ 순증 → VZ 모바일 가입자 유지에 압박 — Frontier 유선 강화로 대응",
  "old_claim_update": {"대법원 FCC 과징금 판결": "refuted — 6/14 기준 Frontier 인수 완료 + 광케이블 3,000만 달성으로 유선 인프라 경쟁력 재확인. FCC 판결 여파 단기 조정에 그침"},
  "new_claim": "Frontier 통합 완료 후 VZ 광케이블 가입자 순증이 ARPU 개선으로 이어질 것인가 (Q2 실적에서 확인)",
  "verified_fact": "Verizon Frontier Communications 인수 완료 — 광케이블 통과 가구 3,000만+ 달성, 미국 최대 광네트워크 사업자 (Verizon IR, 2026-06-14)",
}

DATA["T"] = {
  "company": "AT&T Inc.",
  "sector_kr": "통신 / 미디어",
  "competitors": "VZ, TMUS",
  "score": "+0.56",
  "key_events": "Q1 광케이블 순증 584K 역대 최고, Lumen 유선 11개 주 인수 완료, 3사 위성-셀룰러 JV 출범",
  "risks": "Lumen 인수 통합 비용 및 레거시 인프라 교체 속도, TMUS 가격 경쟁으로 무선 ARPU 하락, 부채 규모 지속 — 이자 비용이 잉여현금 압박",
  "claims": [
    ("AT&T IR, 2026-06-14", "Q1 광케이블 순증 584K로 역대 최고 — 광케이블 통과 가구 누적 3,000만 달성", "+", "earnings"),
    ("Reuters, 2026-06-14", "Lumen 유선 사업 11개 주 인수 완료 — 광케이블 커버리지 남부·중서부 확대", "+", "m&a"),
    ("AT&T Newsroom, 2026-06-10", "3사 위성-셀룰러 JV 참여 — 농촌 커버리지 해소로 가입자 이탈 방지", "+", "product"),
  ],
  "competitors_context": "VZ: Frontier 인수 완료 광케이블 3,000만+ → T와 광케이블 규모 경쟁 양강 구도\nTMUS: FWA 500K+ 순증 → T 모바일 가입자 유출 압박, T는 유선 광케이블로 차별화",
  "old_claim_update": {"대법원 FCC 과징금 판결": "refuted — 6/14 기준 Q1 광케이블 584K 역대 최고 + Lumen 인수 완료로 성장 전략 실행력 확인"},
  "new_claim": "Q1 광케이블 584K 순증이 지속 가속될 것인가 — Lumen 인수 통합 효과 포함 Q2 확인 예정",
  "verified_fact": "AT&T Q1 광케이블 순증 584K 역대 최고 기록 (AT&T IR, 2026-06-14), Lumen 11개 주 유선 인수 완료",
}

DATA["TMUS"] = {
  "company": "T-Mobile US, Inc.",
  "sector_kr": "통신 / 미디어",
  "competitors": "VZ, T",
  "score": "+0.62",
  "key_events": "Q1 EPS $2.27 어닝 서프라이즈, FWA 50만+ 순증 누적 500만, 3사 위성-셀룰러 JV 출범",
  "risks": "FWA 가입자 증가로 5G 네트워크 용량 조기 포화, VZ·T 광케이블 공세로 유선 대체 경쟁 심화, 스펙트럼 추가 확보 비용",
  "claims": [
    ("T-Mobile IR, 2026-06-14", "Q1 EPS $2.27로 컨센서스 상회, 서비스 매출 +11% — 후불제 가입자 순증 지속", "+", "earnings"),
    ("T-Mobile IR, 2026-06-14", "고정무선인터넷(FWA) 분기 50만+ 순증, 누적 500만 가입자 — 케이블 사업자 대체 가속", "+", "earnings"),
  ],
  "competitors_context": "VZ: Frontier 광케이블 3,000만+ 완성 → TMUS FWA 대체 수요 일부 흡수 — 단기 경쟁 심화\nT: 584K 광케이블 역대 최고 → TMUS FWA 시장 침투 경쟁 압박",
  "old_claim_update": {"Charter·Comcast MVNO 독점 계약": "verified — Q1 EPS 비트 및 FWA 500만 돌파로 MVNO + FWA 복합 성장 전략 유효성 확인"},
  "new_claim": "FWA 누적 500만 달성 이후 성장 속도 둔화 시점이 언제인가 — Q2에서 확인 필요",
  "verified_fact": "T-Mobile FWA 누적 가입자 500만 달성 (T-Mobile IR, 2026-06-14), Q1 EPS $2.27 컨센서스 상회",
}

DATA["CMCSA"] = {
  "company": "Comcast Corporation",
  "sector_kr": "통신 / 미디어",
  "competitors": "CHTR, DIS, NFLX",
  "score": "+0.29",
  "key_events": "Versant 스핀오프 독립 완료, Q1 브로드밴드 순감 45K — 예상 대비 개선, Xfinity Mobile 43.5만 순증",
  "risks": "FWA(TMUS·VZ)에 의한 브로드밴드 가입자 추가 이탈, Peacock 콘텐츠 투자 대비 가입자 성장 속도, 테마파크 경기 민감성",
  "claims": [
    ("Comcast IR, 2026-01-02", "케이블 채널(MSNBC·E! 등) 스핀오프 Versant 독립 완료 — CMCSA 테마파크·스트리밍 집중", "+", "other"),
    ("Comcast IR, 2026-06-14", "Q1 브로드밴드 순감 45K — 예상(-80K) 대비 개선, 하락세 둔화 신호", "+", "earnings"),
    ("Comcast IR, 2026-06-14", "Xfinity Mobile 무선 Q1 순증 43.5만 — MVNO 성장으로 브로드밴드 번들 방어", "+", "earnings"),
  ],
  "competitors_context": "CHTR: 브로드밴드 이탈 가속 주가 -12.3% → CMCSA 브로드밴드 이탈 둔화 대비 상대적 강세\nNFLX: Q1 +16.2% 광고 요금제 60% → CMCSA Peacock 구독 경쟁 압박이나 광고 다각화로 헤지",
  "old_claim_update": {"T-Mobile MVNO 비즈니스 계약": "verified — Xfinity Mobile MVNO 43.5만 Q1 순증으로 B2B 다각화 전략 유효성 확인"},
  "new_claim": "브로드밴드 이탈 45K로 예상 대비 개선 — 2분기에 이탈 추세가 안정화될 것인가 (Q2 실적에서 확인)",
  "verified_fact": None,
}

DATA["CHTR"] = {
  "company": "Charter Communications, Inc.",
  "sector_kr": "통신 / 미디어",
  "competitors": "CMCSA, VZ, T",
  "score": "-0.14",
  "key_events": "Q1 브로드밴드 순감 18만 — 이탈 가속, 월간 주가 -12.3%, Spectrum TV AI 광고 타겟팅 도입",
  "risks": "TMUS·VZ FWA 광케이블 대체 가속 — 구조적 이탈, 2025 광케이블 업그레이드 투자 회수 지연, 부채 레버리지 고정비 부담",
  "claims": [
    ("Charter IR, 2026-06-14", "Q1 브로드밴드 순감 18만 — 전 분기 대비 악화, TMUS·VZ FWA 대체 심화", "-", "earnings"),
    ("Bloomberg, 2026-06-13", "월간 -12.3% 언더퍼폼 — 브로드밴드 구조적 이탈과 2025 광케이블 투자 회수 불확실", "-", "other"),
    ("CNBC, 2026-06-13", "Spectrum TV AI 광고 타겟팅 추가 — 가입자 감소 대응, ARPU 방어 전략", "+", "product"),
  ],
  "competitors_context": "CMCSA: 브로드밴드 이탈 45K로 예상 대비 개선 → CHTR 이탈 가속화 대비 CMCSA 상대 강세 부각\nVZ: Frontier 광케이블 3,000만+ 완성 → CHTR 시장 광케이블 대체 압박 직접 가중",
  "old_claim_update": {"T-Mobile MVNO 계약, Q1 Spectrum Mobile +36.8만": "refuted — Q1 브로드밴드 순감 18만 가속, 주가 -12.3%로 MVNO 성과에도 구조적 이탈 지속 확인"},
  "new_claim": "CHTR 광케이블 업그레이드 투자가 브로드밴드 이탈 방어로 이어지는 시점은 언제인가 (장기 추적 필요)",
  "verified_fact": None,
}

DATA["NFLX"] = {
  "company": "Netflix, Inc.",
  "sector_kr": "통신 / 미디어",
  "competitors": "DIS, AMZN, SPOT",
  "score": "+0.62",
  "key_events": "Q1 매출 +16.2% → $10.5B, 유료 가입자 +800만, 광고 요금제 신규 가입 60%+ 돌파, NFL 크리스마스 라이브 2029년 계약",
  "risks": "콘텐츠 투자 비용 증가로 자유현금흐름 압박, 광고 시장 경기 민감성, 라이브 스포츠 중계권 비용 과열",
  "claims": [
    ("Netflix IR, 2026-06-14", "Q1 매출 +16.2% → $10.5B, 유료 가입자 +800만 — 광고 지원 요금제 효과 본격화", "+", "earnings"),
    ("Bloomberg, 2026-06-13", "광고 요금제 신규 가입 60%+ 차지 — 광고 사업 연간 $30억 달성 경로 확인", "+", "product"),
    ("Reuters, 2026-06-14", "NFL 크리스마스 라이브 방송 2029년까지 확보 — 라이브 스포츠로 가입자 유인 강화", "+", "product"),
  ],
  "competitors_context": "DIS: Q2 스트리밍 +88% ($5.82억) → NFLX 광고 모델 유효성 공동 증명\nAMZN: Prime Video 광고 확장 → NFLX 광고 인벤토리 시장 경쟁 심화\nSPOT: Q2 마진 가이던스 미스 → 미디어 스트리밍 수익화에서 NFLX 실행력 우위 부각",
  "old_claim_update": {"광고 고객사 +70% YoY·매출 $30억 경로": "verified — 광고 요금제 신규 가입 60% 돌파, Q1 매출 +16.2% 구조적 성장 확인"},
  "new_claim": "광고 요금제 60%+ 침투율이 광고 단가(CPM) 상승으로 이어져 $30억 광고 매출 목표를 조기 달성할 것인가 (7일 검증 대기)",
  "verified_fact": "Netflix Q1 광고 요금제 신규 가입 비중 60%+ 돌파, 연간 광고 매출 $30억 달성 경로 확인 (Bloomberg / Netflix IR, 2026-06-14)",
}

DATA["DIS"] = {
  "company": "The Walt Disney Company",
  "sector_kr": "통신 / 미디어",
  "competitors": "NFLX, CMCSA",
  "score": "+0.57",
  "key_events": "Q2 스트리밍 영업이익 $5.82억 (+88%), 파크 매출 +7% YoY, Josh D'Amaro 신임 CEO 취임",
  "risks": "콘텐츠 제작비 증가로 스트리밍 마진 압박 재현 가능, ESPN+ 스포츠 중계권 비용 과열, 파크 임금 상승과 경기 민감성",
  "claims": [
    ("Disney IR, 2026-06-14", "Q2 스트리밍 영업이익 $5.82억 (+88% YoY) — Disney+ 수익화 전환점 완성", "+", "earnings"),
    ("Disney IR, 2026-06-14", "파크 매출 +7% YoY — 갤럭틱 스타크루저 2027년 완매, 테마파크 회복 가속", "+", "earnings"),
    ("Bloomberg, 2026-06-13", "Josh D'Amaro 신임 CEO 취임 (파크 총괄) — Bob Iger 상임이사로 전환, 경영 연속성 확보", "+", "other"),
  ],
  "competitors_context": "NFLX: Q1 +16.2%, 광고 60%+ → DIS 스트리밍 수익화 전환과 함께 프리미엄 스트리밍 시장 양강 체제\nCMCSA: Peacock 성장 → DIS 스포츠 콘텐츠 경쟁이나 규모 차이로 직접 위협 제한",
  "old_claim_update": {"Q2 스트리밍 영업이익 +88%·마진 11%": "verified — Q2 스트리밍 영업이익 $5.82억(+88%) 확인, 신임 CEO 취임으로 경영 연속성 확보"},
  "new_claim": "Josh D'Amaro 신임 CEO 하 스트리밍 수익화 모멘텀이 Q3에도 지속될 것인가 (7일 검증 대기)",
  "verified_fact": "Disney Q2 스트리밍 영업이익 $5.82억 (+88% YoY) — Disney+ 수익화 전환 완성 (Disney IR, 2026-06-14)",
}

DATA["SPOT"] = {
  "company": "Spotify Technology S.A.",
  "sector_kr": "통신 / 미디어",
  "competitors": "NFLX, AAPL",
  "score": "+0.41",
  "key_events": "Q1 MAU 7.61억 역대 최고, Q2 매총이익 가이던스 €6.3억 (컨센서스 미스), AI DJ·플레이리스트 프리미엄 전환 견인",
  "risks": "AI 기능 투자 비용으로 마진율 하락 지속, 애플·유튜브 뮤직과의 음악 스트리밍 경쟁, 레코드 레이블 로열티 협상 비용 상승",
  "claims": [
    ("Spotify IR, 2026-06-14", "Q1 MAU 7.61억 역대 최고 — 전 분기 대비 +3,000만, 글로벌 오디오 플랫폼 지배력 확인", "+", "earnings"),
    ("Spotify IR, 2026-06-14", "Q2 매출총이익 가이던스 €6.3억 — 컨센서스 €6.84억 대비 미스, AI 기능 투자 비용 반영", "-", "earnings"),
  ],
  "competitors_context": "NFLX: 광고 요금제 60%+ → SPOT도 광고 지원 모델 유효성 확인 — 오디오 광고 확장 기대\nAAPL: Apple Music 고품질 오디오 확장 → SPOT 프리미엄 고객 이탈 압박",
  "old_claim_update": {"Netflix와 $1억 독점 팟캐스트 영상 계약": "verified — AI DJ·플레이리스트로 프리미엄 전환 견인, MAU 7.61억 역대 최고로 플랫폼 성장 확인"},
  "new_claim": "Q2 마진 가이던스 미스가 일시적 AI 투자 비용인가 vs 구조적 마진 압박인가 (Q2 실적 7월 발표에서 확인)",
  "verified_fact": None,
}

DATA["EA"] = {
  "company": "Electronic Arts Inc.",
  "sector_kr": "통신 / 미디어",
  "competitors": "TTWO, MSFT",
  "score": "+0.38",
  "key_events": "FY26 순예약 $80.26억 역대 최고, $550억 PIF·Silver Lake 인수 제안 CFIUS 심사, Apex Legends 모바일 중단",
  "risks": "CFIUS 인수 불허 시 주가 되돌림 리스크, GTA VI 연말 출시로 EA 게임 시즌 경쟁 심화, 라이브서비스 의존도 집중으로 신작 IP 개발 지연",
  "claims": [
    ("EA IR, 2026-06-14", "FY26 순예약 $80.26억 역대 최고 (+8% YoY) — FC·Madden 라이브서비스 안정적 성장 확인", "+", "earnings"),
    ("WSJ, 2026-06-14", "$550억 사우디 PIF·Silver Lake 인수 제안 CFIUS 심사 중 — 국가안보 우려로 승인 불확실", "+", "m&a"),
  ],
  "competitors_context": "TTWO: GTA VI 11월 19일 공식 확정 → EA 연말 게임 시즌 경쟁 심화 — EA Sports FC 시즌과 겹침\nMSFT: Game Pass에 EA 게임 추가 → 유통 채널 확대이나 구독 모델 의존도 증가 양면",
  "old_claim_update": {"FY26 사상 최대 실적, $550억 비공개 인수 CFIUS 심사 최종 단계": "pending — CFIUS 심사 계속 진행 중, 승인 또는 거부 결정 미확정"},
  "new_claim": "CFIUS 심사 결과 — 인수 승인 시 $550억 프리미엄 실현 vs 불허 시 되돌림 리스크 (결정 시기 불확정)",
  "verified_fact": "EA FY2026 순예약 $80.26억 역대 최고 — 라이브서비스 모델 안정적 성장 확인 (EA IR, 2026-06-14)",
}

DATA["TTWO"] = {
  "company": "Take-Two Interactive Software, Inc.",
  "sector_kr": "통신 / 미디어",
  "competitors": "EA, MSFT",
  "score": "+0.72",
  "key_events": "GTA VI 출시일 11월 19일 공식 확정, 트레일러 3 6월 말 공개·사전예약 개시, 애널리스트 출시 첫 주 $30억+ 매출 전망",
  "risks": "GTA VI 출시 지연 리스크 (1회 이상 연기 이력), GTA VI 출시 후 실망 시 급락 리스크 (기대 과잉), 사이버범죄·규제 논란으로 마케팅 차질",
  "claims": [
    ("Rockstar Games, 2026-06-14", "GTA VI 공식 출시일 11월 19일 확정 — 역대 최다 사전예약 기록 경신 전망", "+", "product"),
    ("Bloomberg, 2026-06-13", "트레일러 3 6월 말 공개 및 사전예약 시작 예정 — 마케팅 사이클 본격 점화", "+", "product"),
    ("Barron's, 2026-06-14", "애널리스트 GTA VI 출시 첫 주 $30억+ 매출 전망 — 역대 최대 엔터테인먼트 출시 기록 가능성", "+", "earnings"),
  ],
  "competitors_context": "EA: Apex 모바일 중단 → TTWO GTA VI PC·콘솔 집중 경쟁 완화 — 연말 점유율 집중 유리\nMSFT: Game Pass 생태계 확장 → GTA VI 구독 포함 여부 협상 지렛대",
  "old_claim_update": {"GTA VI 2026년 11월 19일 확정": "verified — Rockstar Games 공식 발표로 GTA VI 11월 19일 출시 최종 확정. 트레일러 3 + 사전예약 6월 말 예정"},
  "new_claim": "GTA VI 출시 첫 주 $30억+ 매출 전망 — 역대 최대 엔터테인먼트 출시 기록 달성할 것인가 (11/19 출시 후 확인)",
  "verified_fact": "GTA VI 공식 출시일 11월 19일, 2026 최종 확정 (Rockstar Games, 2026-06-14). 트레일러 3 6월 말 공개·사전예약 개시 예정.",
}

# ── Helper functions ──────────────────────────────────────────────────────────

def build_daily_entry(ticker, data):
    score = data["score"]
    key_events = data["key_events"]
    risks = data["risks"]
    claims = data.get("claims", [])
    competitors_context = data.get("competitors_context", "")

    lines = [f"### {DATE}\n"]
    lines.append(f"\n**narrative_score**: {score}")
    lines.append(f"**key_events**: {key_events}")
    lines.append(f"**risks**: {risks}\n")

    for (source, text, impact, category) in claims:
        lines.append(f"> [!claim] (출처: {source}) {text}")
        lines.append(f"> impact: {impact} / category: {category}\n")

    if competitors_context:
        lines.append("**경쟁사 동향**:")
        for line in competitors_context.split("\n"):
            if line.strip():
                lines.append(f"- {line.strip()}")
        lines.append("")

    lines.append("---")
    return "\n".join(lines) + "\n"


def update_claims_section(content, old_claim_update, new_claim):
    """Update open claims section."""
    start = "<!-- OPEN_CLAIMS_START -->"
    end = "<!-- OPEN_CLAIMS_END -->"
    idx_s = content.find(start)
    idx_e = content.find(end)
    if idx_s == -1 or idx_e == -1:
        return content

    claims_block = content[idx_s + len(start):idx_e]
    new_block = claims_block

    # Update existing claims
    for pattern, resolution in old_claim_update.items():
        # Find lines matching pattern and mark them resolved
        lines = new_block.split("\n")
        new_lines = []
        for line in lines:
            if pattern in line and line.strip().startswith("- [ ]"):
                # Extract date
                date_match = re.search(r"\*\*(\d{4}-\d{2}-\d{2})\*\*", line)
                date_str = date_match.group(1) if date_match else "?"
                new_lines.append(f"- [x] **{date_str}** → **{DATE} {resolution}**")
            else:
                new_lines.append(line)
        new_block = "\n".join(new_lines)

    # Add new claim
    if new_claim:
        # Remove placeholder if present
        new_block = new_block.replace("_(루틴 첫 실행 전 — 비어 있음)_\n", "")
        new_block = new_block.rstrip("\n") + f"\n- [ ] **{DATE}**: {new_claim}\n"

    return content[:idx_s + len(start)] + new_block + content[idx_e:]


def update_facts_section(content, verified_fact):
    """Add verified fact if provided."""
    if not verified_fact:
        return content
    start = "<!-- FACTS_START -->"
    end = "<!-- FACTS_END -->"
    idx_s = content.find(start)
    idx_e = content.find(end)
    if idx_s == -1 or idx_e == -1:
        return content

    fact_block = content[idx_s + len(start):idx_e]
    new_fact = f"\n> [!fact] (출처: 루틴 수집, {DATE}) {verified_fact}\n"
    new_block = fact_block.rstrip("\n") + new_fact

    return content[:idx_s + len(start)] + new_block + content[idx_e:]


def prepend_daily_entry(content, daily_entry):
    """Prepend new daily entry after DAILY_START marker."""
    marker = "<!-- DAILY_START -->"
    idx = content.find(marker)
    if idx == -1:
        return content
    insert_pos = idx + len(marker)
    return content[:insert_pos] + "\n" + daily_entry + content[insert_pos:]


def update_frontmatter_date(content, date):
    """Update the updated: field in frontmatter."""
    return re.sub(r"(updated:\s*)\d{4}-\d{2}-\d{2}", f"\\g<1>{date}", content, count=1)


def update_ticker_file(ticker, data):
    """Update an existing ticker wiki file."""
    # Find the file
    matches = list(TICKERS_DIR.glob(f"{ticker} - *.md"))
    if not matches:
        print(f"  WARNING: no file found for {ticker}")
        return

    path = matches[0]
    content = path.read_text(encoding="utf-8")

    content = update_frontmatter_date(content, DATE)
    content = update_claims_section(content, data.get("old_claim_update", {}), data.get("new_claim"))
    content = update_facts_section(content, data.get("verified_fact"))
    daily_entry = build_daily_entry(ticker, data)
    content = prepend_daily_entry(content, daily_entry)

    path.write_text(content, encoding="utf-8")
    print(f"  updated {path.name}")


def create_ticker_file(ticker, company, d):
    """Create a new ticker wiki file."""
    sector_kr = d["sector_kr"]
    competitors = d["competitors"]
    description = d.get("description", "")
    slug = f"{ticker} - {company}.md"
    path = TICKERS_DIR / slug

    daily_entry = build_daily_entry(ticker, d)

    content = f"""---
title: "{ticker} - {company} — Routine News Log"
created: {DATE}
updated: {DATE}
domain: finance
type: claim
weight: reference
confidence: low
tags: [routine-news, watchlist, {ticker}]
sources: []
---

# {ticker} - {company} — Routine News Log

**{company}** · Industrials · {sector_kr} · 경쟁사: {competitors}

## 회사 소개

{description}

> [!info] 자동 수집 노트
> 이 페이지는 `indicator_dashboard` 의 `daily-market-analysis` 루틴이 매일 누적한다. 신규 항목은 모두 `[!claim]` (confidence: low) 로 들어오고, 후속 일자에 [사실 누적] 또는 [반증] 으로 분류된다. 폴더 규칙: [news/README.md](../README.md).

---

## 미해결 가설 (Open Claims)

루틴이 매일 이 목록을 읽고, 오늘 뉴스가 가설을 (verified / refuted / pending / aged-out) 중 어디에 해당하는지 판정한다.

<!-- OPEN_CLAIMS_START -->
- [ ] **{DATE}**: {d.get("new_claim", "")}
<!-- OPEN_CLAIMS_END -->

---

## 사실 누적 (Verified Facts)

독립 Tier-1 매체 2 곳 이상이 보고하거나, 회사 IR / 공시로 확정된 사실만 모음.

<!-- FACTS_START -->
<!-- FACTS_END -->

---

## 일자별 기록 (역순)

<!-- DAILY_START -->
{daily_entry}
<!-- DAILY_END -->
"""
    path.write_text(content, encoding="utf-8")
    print(f"  created {slug}")


# ── Update dashboard ──────────────────────────────────────────────────────────

def update_dashboard():
    dash_path = WIKI / "_dashboard.md"
    content = dash_path.read_text(encoding="utf-8")

    # Update frontmatter updated
    content = update_frontmatter_date(content, DATE)

    # Update 소비재 table rows
    consumer_updates = {
        "WMT": (DATE, "+0.60", "드론배달 7개 시장 확장, 시총 $1조 임박 (YTD +37%), 월튼 가문 $2억 매도", "1"),
        "COST": (DATE, "+0.55", "5월 순매출 +14.5% YoY, 회원 갱신률 92.9% 역대 최고, Outperform 목표가 $975", "1"),
        "KO":   (DATE, "+0.52", "FIFA 월드컵 공식 음료 파트너, 인도 보틀링 2027 IPO, MS 목표가 $89", "1"),
        "PEP":  (DATE, "+0.23", "북미 음료 -2.5%, 스낵 가격 15% 인하, Q2 실적 7월 9일", "1"),
        "PG":   (DATE, "+0.42", "UBS 목표가 $172, Native Surf Club Gen Z 론칭, 주간 +5.4%", "1"),
        "MO":   (DATE, "+0.28", "on! PLUS 신규 출시, 배당락일 6/15 ($1.06), NJOY 멘톨 금지 지속", "1"),
        "MCD":  (DATE, "+0.57", "FIFA 월드컵 캠페인, AI 드라이브스루 90% 달성, Q1 동일매장 +9.4%", "1"),
        "HD":   (DATE, "+0.44", "Q1 $41.8B (+4.8%), 주택 거래 2022년 이후 최고, Pro 5분기 연속 강세", "1"),
        "NKE":  (DATE, "-0.27", "RBC Sector Perform 하향 $50, YTD -30.3%, Q4 실적 6/30", "1"),
        "SBUX": (DATE, "+0.29", "일본 지분 IPO 검토 $2.5B, 중국 60% 알리바바 매각 $4B, YTD +22.7%", "1"),
    }

    # Defense/Industrials table updates
    industrial_updates = {
        "CAT":  (DATE, "+0.53", "AI 데이터센터 2GW 컨소시엄, 수주잔고 $62.7B 역대 최고, 배당 8% 인상", "1"),
        "DE":   (DATE, "+0.11", "건설장비 +29% 서프라이즈, 관세 $1.2B 역풍, 대형 농기계 부진 지속", "1"),
        "BA":   (DATE, "+0.02", "5월 인도 60대 (+28% MoM), 777X 조립 개시, 우간다항공 $9.85억 수주", "1"),
        "LMT":  (DATE, "+0.62", "주간 PAC-3·F-35·MH-60R ~$100억, 우주군 $5.1억, DB Buy $610", "1"),
        "RTX":  (DATE, "+0.57", "$5.15억 SPY-6 레이더 양산, $1억 LTAMDS 신시설, DBS Buy $145", "1"),
        "NOC":  (DATE, "+0.52", "B-21 73일 시험 순항, 생산율 25% 확대 $4.5B, 배당 +6.9%", "1"),
        "HON":  (DATE, "+0.44", "HONA 스핀오프 6/29 확정 (1:2 역분할), 배당락 6/15, 가이던스 유지", "0"),
        "GE":   (DATE, "+0.41", "Q1 수주 +87% $23B, LEAP +63%, Wolfspeed SiC MOU + $1B 미국 투자", "1"),
        "UPS":  (DATE, "-0.16", "30,000명 감원·24개 시설 폐쇄, 아마존 물량 50%+ 감소, 국제 +6%", "1"),
        "FDX":  (DATE, "+0.13", "Freight 스핀오프 완료 NYSE:FDXF, 조종사 합의 타결", "0"),
        "AVAV": (DATE, "+0.42", "$1.17억 P550 육군 계약, 대만 Ubiqconn MOU, Switchblade 500% 증산", "1"),
        "KTOS": (DATE, "+0.48", "JPM Overweight $82, Spartan 3K 달성, 해병대 CCA 공식 선정", "1"),
        "012450.KS": (DATE, "-0.28", "대전 폭발 5명 사망, CEO 중대재해법 입건, 9개 사업장 중단", "1"),
        "079550.KS": (DATE, "+0.53", "UAE 천궁-II 92% 요격 성공, 말레이시아 해궁 $9,400만, LIG Defense 리브랜딩", "1"),
    }

    telecom_updates = {
        "VZ":    (DATE, "+0.44", "Frontier 인수 완료 광케이블 3,000만+, 3사 위성 JV, 기업 광케이블 +12%", "1"),
        "T":     (DATE, "+0.56", "Q1 광케이블 584K 역대 최고, Lumen 인수 완료, 3사 위성 JV", "1"),
        "TMUS":  (DATE, "+0.62", "Q1 EPS $2.27 비트, FWA 500K+ 누적 500만, 3사 위성 JV", "1"),
        "CMCSA": (DATE, "+0.29", "Versant 스핀오프 완료, 브로드밴드 순감 45K (예상 대비 개선), Xfinity Mobile 43.5만", "0"),
        "CHTR":  (DATE, "-0.14", "브로드밴드 순감 18만 이탈 가속, 주가 월간 -12.3%, AI 광고 타겟팅 도입", "1"),
        "NFLX":  (DATE, "+0.62", "Q1 +16.2% $10.5B, 광고 요금제 60%+, NFL 크리스마스 2029 독점", "1"),
        "DIS":   (DATE, "+0.57", "Q2 스트리밍 +88% $5.82억, 파크 +7%, Josh D'Amaro 신임 CEO 취임", "1"),
        "SPOT":  (DATE, "+0.41", "Q1 MAU 7.61억 역대 최고, Q2 마진 가이던스 미스, AI 프리미엄 전환 견인", "1"),
        "EA":    (DATE, "+0.38", "FY26 역대 최고 순예약 $80.26억, $550억 PIF 인수 CFIUS 심사, Apex 모바일 중단", "1"),
        "TTWO":  (DATE, "+0.72", "GTA VI 11/19 공식 확정, 트레일러 3 6월 말, 첫 주 $30억+ 전망", "0"),
    }

    all_updates = {**consumer_updates, **industrial_updates, **telecom_updates}

    # Update table rows
    lines = content.split("\n")
    new_lines = []
    for line in lines:
        updated = False
        for ticker, (date_v, score_v, headline_v, claims_v) in all_updates.items():
            # Match table row: | [TICKER](...) | ... |
            # Try to match both formats
            if f"[{ticker}](" in line:
                # Check it's a table row for this ticker
                if line.count("|") >= 4:
                    parts = [p.strip() for p in line.split("|")]
                    if len(parts) >= 6:
                        # Extract ticker cell to confirm
                        ticker_cell = parts[1] if len(parts) > 1 else ""
                        if f"[{ticker}](" in ticker_cell:
                            parts[2] = date_v
                            parts[3] = score_v
                            parts[4] = headline_v
                            parts[5] = claims_v
                            new_line = "| " + " | ".join(parts[1:6]) + " |"
                            new_lines.append(new_line)
                            updated = True
                            break
        if not updated:
            new_lines.append(line)
    content = "\n".join(new_lines)

    # Add AVAV and KTOS rows to 산업재 / 방산 table if not present
    if "AVAV" not in content:
        avav_row = f"| [AVAV](tickers/AVAV - AeroVironment, Inc..md) | {DATE} | +0.42 | $1.17억 P550 육군 계약, 대만 Ubiqconn MOU, Switchblade 500% 증산 | 1 |"
        ktos_row = f"| [KTOS](tickers/KTOS - Kratos Defense & Security Solutions, Inc..md) | {DATE} | +0.48 | JPM Overweight $82, Spartan 3K 달성, 해병대 CCA 공식 선정 | 1 |"
        # Insert after FDX row
        fdx_marker = "FDX](tickers/FDX"
        idx = content.find(fdx_marker)
        if idx != -1:
            end_of_fdx_line = content.find("\n", idx)
            content = content[:end_of_fdx_line + 1] + avav_row + "\n" + ktos_row + "\n" + content[end_of_fdx_line + 1:]

    # Add today's 오늘의 시그널 section before existing sections
    signal_section = f"""
## 오늘의 시그널 ({DATE} · 일요일 · 소비재 + 산업재 / 방산 + 통신 / 미디어)

루틴은 다음 패턴을 감지하면 이 섹션에 기록한다:

- **연속성**: 같은 테마가 3 일 이상 연속 등장 (예: 비만치료제 임상 데이터 연속)
- **모순**: 같은 종목 어제/오늘 narrative 가 반대 방향
- **섹터 동기화**: 3 종목 이상이 같은 매크로 이슈 (예: 관세, FOMC, 유가, 비만치료제, 데이터센터 전력) 로 동시 움직임

**{DATE} 감지된 시그널:**

- **최고 시그널 (TTWO +0.72)**: GTA VI 11/19 공식 확정 + 트레일러 3 6월 말 + 첫 주 $30억+ 전망 삼중 모멘텀. 역대 최대 엔터테인먼트 출시가 6개월 앞으로 다가오며 마케팅 사이클 점화. TTWO 주도 통신/미디어 섹터 최강 모멘텀.
- **최고 시그널 (LMT +0.62)**: 주간 PAC-3·F-35·MH-60R ~$100억 + 우주군 $5.1억 + Deutsche Bank Buy 업그레이드. 유럽 재무장·중동 미사일방어 수요 동시 폭발. 방산 섹터 복합 호재 집중.
- **섹터 동기화 (방산 예산 확대)**: LMT +0.62 / RTX +0.57 / NOC +0.52 / KTOS +0.48 / AVAV +0.42 — 5개 방산주 동시 강세. 미사일방어(LMT·RTX)·스텔스(NOC)·드론(KTOS·AVAV) 전 영역에서 대형 계약 동시 발표. NATO 재무장 + 드론 우위 전략이 방산 섹터 구조적 슈퍼사이클 신호.
- **섹터 동기화 (소비재 방어주 로테이션)**: WMT +0.60 / COST +0.55 / MCD +0.57 / KO +0.52 — 4종목 동시 강세. 소비 경기 불확실성 속 대형 소비재 방어주 로테이션 가속. PEP +0.23·NKE -0.27의 약세 대비 극명한 양극화.
- **섹터 동기화 (통신 인프라 구조 개편)**: VZ Frontier 인수 완료 + T Lumen 인수 완료 + 3사 위성 JV — 통신 빅3 모두 인프라 확장·위성 커버리지 공동 진입. 광케이블 vs FWA(TMUS) 경쟁이 최고조로 도달, 구독자 쟁탈전 본격화.
- **역방향 (NKE vs 소비재 섹터)**: NKE -0.27 vs WMT +0.60·MCD +0.57·COST +0.55 — 나이키만 섹터 내 역행. 브랜드 리셋 고통이 2년째 지속 중. 6/30 Q4 실적이 전환점 여부의 마지막 판단 기회.
- **경고 시그널 (012450.KS -0.28)**: 대전 폭발 5명 사망·CEO 중대재해법 입건·9개 사업장 중단 — K-방산 대장주에 최대 악재. 폴란드·루마니아 수출 납기 차질 여부 30일 추적 필요. 경쟁사 LIG Nex1(079550.KS +0.53)이 반사 수혜.
- **섹터간 전파 (AI 인프라 → 소비재 + 방산 + 통신)**: CAT AI 데이터센터 2GW 컨소시엄 + VZ 기업 광케이블 +12% + GE Q1 수주 +87% — AI 인프라 수요가 소비재(CAT 발전기)·방산(드론 AI)·통신(광케이블 연결) 전 섹터로 파급.
- **연속성 (스트리밍 수익화)**: NFLX +0.62 (광고 60%) / DIS +0.57 (스트리밍 +88%) — 2주 연속 스트리밍 수익화 테마 강화. OTT 업계 광고 모델 수익성 전환 완성 신호.
- **주목 이벤트**: GTA VI 트레일러 3 6월 말 공개·사전예약 시작, HONA 스핀오프 6/29 완료, HON·MO 배당락일 6/15, NKE Q4 실적 6/30, PEP Q2 실적 7/9, UPS Q2 실적 (감원 효과 첫 확인), 012450.KS 수출 납기 30일 추적.

### 감지된 패턴 (2026-06-13 · 토요일 · 금융 + 부동산 (REITs))
"""

    # Insert signal section before the existing "## 오늘의 시그널 (2026-06-10" line
    existing_signal_marker = "## 오늘의 시그널 (2026-06-10"
    idx = content.find(existing_signal_marker)
    if idx != -1:
        content = content[:idx] + signal_section + "\n" + content[idx:]
    else:
        # Append before "## 사용 팁"
        tip_marker = "## 사용 팁"
        idx = content.find(tip_marker)
        if idx != -1:
            content = content[:idx] + signal_section + "\n" + content[idx:]

    dash_path.write_text(content, encoding="utf-8")
    print(f"  updated _dashboard.md")


# ── Main ──────────────────────────────────────────────────────────────────────

print("=== Updating ticker wiki files ===")
for ticker, d in DATA.items():
    update_ticker_file(ticker, d)

print("\n=== Creating new ticker files ===")
create_ticker_file("AVAV", "AeroVironment, Inc.", {**AVAV_DATA, "claims": AVAV_DATA["claims"], "competitors_context": AVAV_DATA["competitors_context"]})
create_ticker_file("KTOS", "Kratos Defense & Security Solutions, Inc.", {**KTOS_DATA, "claims": KTOS_DATA["claims"], "competitors_context": KTOS_DATA["competitors_context"]})

print("\n=== Updating dashboard ===")
update_dashboard()

print("\n✅ All wiki files updated successfully!")
