# AGENTS.md — RJ Unified Loop OS v2.0

## Project Identity

This is the **RJ Unified Loop OS** — Rick Jefferson's fail-closed research-to-production loop engine combining 45 operational loops, 12 autocode generators, and a consolidated credential layer.

**Operator:** Rick Jefferson / RJ Business Solutions
**Stack:** Python 3.12+ / Cloudflare-first / Mistral Vibe agents
**Principle:** Fail-closed. Never proceed without evidence, verification, and required approvals.

## What Agents Must Know

### 1. Loop execution flow

Every loop follows the same pattern:
1. **Init** → Create an immutable run with input hashes
2. **Run** → Execute stages sequentially via vibe agents
3. **Approve** → Human approvals for high-risk gates
4. **Verify** → Independent validation of all stage artifacts
5. **Complete** or **Blocked** → Only complete when all gates pass

### 2. Agent assignments

Loop stages are routed to agents by profile:

| Profile | Agent | Domains |
|:--|:--|:--|
| `research` | `rb-researcher` | Papers, repos, evidence |
| `software` | `rb-builder` | Code, architecture, tests |
| `experience` | `xp-builder` | Websites, apps, CRM, SEO |
| `compliance` | `lo-compliance` | Credit, legal, privacy |
| `finance` | `lo-compliance` | Funding, business credit |
| `growth` | `lo-growth` | Marketing, sales, content |
| `operations` | `lo-operator` | Delivery, support, billing |
| `ai` | `lo-ai` | Model routing, agents, RAG |

Verification stages always route to `lo-verifier`.

### 3. Safety constraints (NEVER VIOLATE)

- Never transmit disputes, legal notices, or regulatory complaints
- Never apply for credit, funding, grants, or contracts
- Never publish legal policies or activate marketing campaigns
- Never deploy to production or move money
- Never delete records, expand credentials, or contact third parties
- All of the above require explicit human approval with evidence

### 4. Evidence hierarchy

1. Official specs, vendor docs, laws, regulations, standards, source repositories
2. Original papers (arXiv, conference proceedings, author repos)
3. Maintainer-authored release notes, security advisories, issues, PRs
4. Independent technical analyses (only when primary sources unavailable)

Search results, AI summaries, and copied blogs are discovery signals — not proof.

### 5. Working with autocode templates

Autocode templates in `autocode/` are prompt-templates for code generation. When using them:
- Read the template fully before generating
- Adapt to the specific project context
- Never generate secrets or hardcoded credentials
- Always verify generated code against the ResearchBuild quality gates

### 6. Key files

| File | Purpose |
|:--|:--|
| `engine/loop_os.py` | Main loop orchestrator |
| `engine/loop-catalog.json` | All 45 loop definitions |
| `engine/research_build.py` | Research → Build pipeline |
| `engine/experience_build.py` | Website/App/CRM build pipeline |
| `config/loop-policy.json` | Loop execution policies |
| `config/policy.json` | ResearchBuild policies |
| `config/experience-policy.json` | ExperienceBuild policies |
| `agents/*.toml` | Vibe agent definitions |
| `prompts/*.md` | Agent prompt files |
