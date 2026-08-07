# RJ Unified Loop OS v2.0

**Fail-closed research-to-production loop engine for Rick Jefferson / RJ Business Solutions.**

Combines three integrated systems under one roof:

| Component | Purpose | Source |
|:--|:--|:--|
| **Engine** (45 loops) | Research → PRD → Architecture → Build → Deploy → Monitor | ResearchBuild-Loop v2.0 |
| **Autocode** (12 templates) | Blog, CRM, funnel, website, social-media, TypeScript generators | Autocode Rick |
| **Config** | API keys, policies, agent definitions, prompts | tokens-keys26 consolidation |

## Quick Start

```bash
# Verify installation
./scripts/install.sh

# See all 45 loops
./scripts/run.sh --list

# Run any loop
./scripts/run.sh --loop full-software-build
./scripts/run.sh --loop credit-dispute-case --inputs case.json

# Dashboard
./scripts/loop-dashboard.sh
```

## Architecture

```
rj-unified-loop-os/
├── engine/                  # Loop engine (Python 3.12+)
│   ├── loop_os.py           # Multi-domain loop orchestrator
│   ├── research_build.py    # Stage 1: Research → Build
│   ├── experience_build.py  # Stage 2: Website/App/CRM/SEO
│   ├── collect_sources.py   # Paper/repo discovery
│   ├── loop-catalog.json    # 45 production loops
│   ├── schemas/             # 8 JSON schema validators
│   └── templates/           # Build specs, evidence guides
├── autocode/                # Code generation templates (12)
├── config/                  # Policies, env template, vibe config
├── agents/                  # 19 Vibe agent definitions (.toml)
├── prompts/                 # 18 agent prompt files (.md)
├── scripts/                 # run.sh, install.sh, dashboard
└── tests/                   # Python test suite
```

## Loop Families (45 total)

| Domain | Loops |
|:--|:--|
| Research & Intelligence | `research-intelligence`, `market-opportunity` |
| Software Engineering | `product-prd`, `architecture-threat-model`, `full-software-build`, `test-repair` |
| DevOps & Ops | `release-deployment`, `service-monitoring`, `incident-response`, `dependency-maintenance`, `backup-disaster-recovery` |
| AI & ML | `ai-model-routing`, `agent-evaluation`, `rag-knowledge`, `memory-governance`, `prompt-optimization` |
| Credit & Finance | `credit-report-audit`, `credit-dispute-case`, `complaint-escalation`, `compliance-audit`, `privacy-compliance`, `business-credit-progression`, `funding-readiness`, `grant-contract-readiness`, `credit-score-analytics` |
| Growth & Marketing | `seo-content-authority`, `content-distribution`, `conversion-funnel`, `lead-nurture`, `sales-pipeline`, `reputation-management`, `affiliate-partner`, `offer-pricing` |
| Operations | `client-onboarding`, `client-delivery`, `crm-data-quality`, `forms-consent`, `billing-reconciliation`, `client-support`, `vendor-risk` |
| Governance | `document-policy-governance`, `cost-optimization`, `analytics-experiment` |
| Education | `financial-education-course` |
| Experience | `website-experience-build` |

## Autocode Templates

Generate code, content, or design specs from proven templates:

```bash
./scripts/run-autocode.sh blog        # Blog post generator
./scripts/run-autocode.sh crm         # CRM builder
./scripts/run-autocode.sh funnel      # Funnel/landing page
./scripts/run-autocode.sh social-media # Social content
./scripts/run-autocode.sh website-design # Website design
./scripts/run-autocode.sh codenexus   # Code nexus
./scripts/run-autocode.sh planning    # Project planning
./scripts/run-autocode.sh rj-brand    # Brand guidelines
./scripts/run-autocode.sh founder-docs # Founder docs
./scripts/run-autocode.sh typescript12 # TypeScript
./scripts/run-autocode.sh coding-autonomous-skills
./scripts/run-autocode.sh testers     # Test generators
```

## Configuration

1. Copy the env template: `cp config/.env.example .env`
2. Fill in your API keys in `.env`
3. Review policies in `config/loop-policy.json`, `config/policy.json`

## Safety Rules

The loop engine is **fail-closed**. It will BLOCK and refuse to proceed when:

- Evidence is missing or cannot be verified
- Required human approvals are absent
- Gates fail (tests, security scans, quality checks)
- Placeholder markers exist in production paths
- Immutable input hashes don't match

**Never runs autonomously:** production deployment, credit dispute delivery, regulatory complaints, funding/credit applications, legal policy publication, marketing campaigns, money movement, or destructive data operations.

## Requirements

- Python 3.12+
- Git
- Mistral Vibe CLI (for agent-driven loop execution)
- Internet access for research loops

## Status

RJ Unified Loop OS v2.0 — August 2026. Assembled from ResearchBuild-Loop v2.0, Autocode Rick, and Master Credentials Configuration.
