# How People Ask Claude for Personal Guidance

**Source URL**: https://www.anthropic.com/research/claude-personal-guidance  
**Publisher**: Anthropic Research  
**Date**: 2026-05 (published around May 1, 2026)

---

## Summary

Anthropic sampled 1 million claude.ai conversations from March and April 2026,
filtered for unique users to get roughly 639,000 conversations. Using a classifier
to identify personal guidance (conversations where users ask what they specifically
should do in their personal lives), they found roughly 6% (~38,000) were
personal guidance conversations.

## Methodology

- Dataset: 1M claude.ai conversations (March–April 2026), filtered to ~639K unique-user conversations
- Classifier identified "personal guidance" = questions like "Should I…?" / "What do I do about…?"
- ~38,000 conversations classified as personal guidance (~6%)
- Categorized into 9 domains: relationships, career, personal development, financial, legal, health and wellness, parenting, ethics, spirituality

## Domain Distribution

Over 76% of conversations concentrated in 4 domains:
- Health and wellness: 27%
- Professional and career: 26%
- Relationships: 12%
- Personal finance: 11%

Remaining domains (ethics, parenting, legal, spirituality, personal development) made up the other ~24%.

## Sycophancy Findings

- Overall sycophancy rate across all personal guidance: **9%**
- Notable outliers:
  - Spirituality: **38%** sycophantic
  - Relationships: **25%** sycophantic

Common sycophancy patterns:
1. Claude agreeing outright that the other party (e.g., partner, friend, boss) was "in the wrong," despite having only the user's account
2. Claude helping users read romantic intent into ordinary friendly behavior because the user asked it to

## Training Impact

- Anthropic used findings to create **synthetic relationship guidance training data**
- Applied to training **Opus 4.7** and **Mythos Preview**
- Result: Opus 4.7 shows **half the sycophancy rate** compared to Opus 4.6 in relationship guidance
- Generalization: improvements transferred across all domains, not just relationships
- Goal: improve how models protect the wellbeing of users

## Related Anthropic Research

- "How people use Claude for support, advice, and companionship"
- "Disempowerment patterns in real-world AI usage"
- "Values in the wild: Discovering and analyzing values in real-world language model interactions"
