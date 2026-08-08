# ROI Calculator — Technical Specification

## Purpose

An interactive, embeddable calculator that demonstrates the cost savings of multi-model AI routing vs single-provider approaches. Captures qualified leads.

---

## Form Inputs

| Field | Type | Description |
|:--|:--|:--|
| `monthly_api_calls` | Number | Total API calls per month (e.g., 100,000) |
| `current_provider` | Select | OpenAI, Anthropic, Google, Mixed, Other |
| `current_monthly_spend` | Currency | Current monthly AI API spend ($) |
| `simple_query_pct` | Slider | % of queries that are simple (0-100) |
| `medium_query_pct` | Slider | % of queries that are medium complexity (0-100) |
| `complex_query_pct` | Slider | Auto-calculated: 100 - simple - medium |
| `name` | Text | Full name |
| `email` | Email | Work email |
| `company` | Text | Company name |

---

## Routing Logic

### Model Cost Table (per 1M tokens)

| Model | Provider | Cost/1M input | Cost/1M output | Best For |
|:--|:--|:--|:--|:--|
| Llama 3.3 70B | NVIDIA NIM | $0.20 | $0.20 | Simple queries, triage |
| Claude Sonnet 4.6 | Anthropic | $3.00 | $15.00 | Standard responses |
| Claude Opus 4.7 | Anthropic | $15.00 | $75.00 | Complex reasoning |
| GPT-5.2 | OpenAI | $3.75 | $15.00 | Synthesis, reporting |
| Gemini 2.0 Flash | Google | $0.10 | $0.40 | Long-context analysis |
| GLM-5-2 | Zhipu | $1.00 | $1.00 | Chinese language |
| MiniMax M3 | MiniMax | $0.50 | $2.00 | Chinese business |

### Routing Rules

```
simple_queries (60% default)  → Llama 3.3 70B    (95% cheaper than GPT-5)
medium_queries (30% default)  → Claude Sonnet 4.6 (balanced cost/quality)
complex_queries (10% default) → Claude Opus 4.7   (premium reasoning)
chinese_queries (if applicable)→ GLM-5-2           (native, 75% cheaper than GPT-5)
```

### Calculation

```
current_cost = monthly_api_calls × avg_tokens_per_call × current_model_cost_per_token
routed_cost = sum of (query_type_pct × monthly_api_calls × avg_tokens × target_model_cost)
annual_savings = (current_cost - routed_cost) × 12
savings_pct = (current_cost - routed_cost) / current_cost × 100
```

---

## Example Output (Pre-calculated for display)

### Current State
- 100,000 API calls/month
- All using GPT-5: $8,500/month
- Annual cost: $102,000

### With RJ Multi-Model Routing
- 60% simple tasks → Llama 3.3: $800/month
- 30% standard tasks → Claude Sonnet: $1,200/month
- 10% complex tasks → Claude Opus: $1,200/month
- **Total: $3,200/month**
- **Annual cost: $38,400**

### Results Display
| Metric | Value |
|:--|:--|
| Current Monthly Spend | $8,500 |
| Optimized Monthly Spend | $3,200 |
| Monthly Savings | $5,300 |
| Annual Savings | $63,600 |
| Savings Percentage | **62%** |
| Payback Period | Immediate |

---

## Lead Capture Flow

1. User enters their numbers → sees real-time savings projection
2. "See Your Personalized Savings" CTA reveals the email capture form
3. On submit:
   - Display personalized results page with downloadable PDF
   - Send email with results
   - Add lead to CRM with calculator inputs as metadata
   - Trigger email nurture sequence Day 1

---

## Technical Implementation

### Frontend
- React component with Tailwind CSS
- Real-time calculation as sliders move
- Animated number counters for results
- RJ brand colors: --rj-blue #2563eb, --rj-navy #0f172a
- Fonts: Space Grotesk headings, Inter body

### Backend
- POST endpoint: `POST /api/roi-calculator`
- Validate inputs, compute savings, store lead
- Generate PDF via headless Chromium
- Send email via Resend/SendGrid

### CRM Integration
- Create contact with calculator inputs as custom fields
- Tag: "ROI Calculator Lead"
- Assign to nurture sequence

---

*Built for RJ Business Solutions · Empowering Generational Wealth*
