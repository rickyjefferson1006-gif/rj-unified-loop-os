# RJ Business Solutions — Brand Kit v10.0

---

## 01 · Brand Essence

**Tagline:** *Empowering Generational Wealth*

RJ Business Solutions delivers premium credit-repair technology, AI-powered marketing automations, and conversion-engineered growth systems. Every surface, every pixel, every word is designed to convey technical mastery, earned trust, and relentless execution — without hype or fluff.

The brand sits at the intersection of Silicon Valley precision and Wall Street confidence. The visual language is clean, dark, gradient-layered, and always anchored by the RJ Blue glow — a signal of competence in a noisy market.

---

## 02 · Company Information

| Field | Value |
|---|---|
| **Company** | RJ Business Solutions |
| **Founder** | Rick Jefferson |
| **Address** | 1342 NM 333, Tijeras, New Mexico 87059 |
| **Website** | [rjbusinesssolutions.org](https://rjbusinesssolutions.org) |
| **Support Email** | [support@rjbusinesssolutions.org](mailto:support@rjbusinesssolutions.org) |
| **LinkedIn** | [linkedin.com/in/rick-jefferson-314998235](https://www.linkedin.com/in/rick-jefferson-314998235) |
| **TikTok** | [@rick_jeff_solution](https://www.tiktok.com/@rick_jeff_solution) |
| **Twitter / X** | [@ricksolutions1](https://twitter.com/ricksolutions1) |
| **GitHub** | [github.com/rjbizsolution23-wq](https://github.com/rjbizsolution23-wq) |

---

## 03 · Logo System

**Primary Logo:**

![RJ Business Solutions Logo](https://storage.googleapis.com/msgsndr/qQnxRHDtyx0uydPd5sRl/media/67eb83c5e519ed689430646b.jpeg)

- **URL:** `https://storage.googleapis.com/msgsndr/qQnxRHDtyx0uydPd5sRl/media/67eb83c5e519ed689430646b.jpeg`
- **Alt text:** `RJ Business Solutions logo`
- **Usage:** Self-host at `/public/logo.jpg` in production; convert to `.svg` if a vector source becomes available.
- **Clear space:** Minimum 24px padding around the logo mark in all applications.

---

## 04 · Color System

### Primary Palette

| Token | Hex | CSS Variable | Usage |
|---|---|---|---|
| RJ Blue | `#2563eb` | `--rj-blue` | Primary CTA buttons, links, focus rings, active states |
| RJ Sky | `#0ea5e9` | `--rj-sky` | Accents, gradient stops, subtle highlights |
| RJ Deep | `#1e3a8a` | `--rj-deep` | Section dividers, dark headers, gradient midpoints |
| RJ Navy | `#0f172a` | `--rj-navy` | Body text, hero backgrounds, footer backgrounds |

### Neutrals

| Token | Hex | CSS Variable | Usage |
|---|---|---|---|
| White | `#ffffff` | `--rj-white` | Card backgrounds, text on dark surfaces |
| Soft | `#f8fafc` | `--rj-soft` | Page background |
| Light | `#eff6ff` | `--rj-light` | Section wash backgrounds, hover states |
| Border | `#bfdbfe` | `--rj-border` | Ghost button borders |
| Muted | `#dbeafe` | `--rj-muted` | Chips, badges, inactive elements |
| Line | `#e2e8f0` | `--rj-line` | Borders, dividers, input borders |

### Semantic

| Token | Hex | CSS Variable | Usage |
|---|---|---|---|
| Success | `#10b981` | `--rj-success` | Positive trends, booked status |
| Warning | `#f59e0b` | `--rj-warning` | Hot leads, caution states |
| Danger | `#ef4444` | `--rj-danger` | Negative trends, notification dots, errors |

### Text Colors

| Token | Hex | CSS Variable | Usage |
|---|---|---|---|
| Text | `#0f172a` | `--rj-text` | Primary body and heading text |
| Muted Text | `#475569` | `--rj-muted-text` | Secondary text, placeholders, captions |

### Gradients

| Token | Value | Usage |
|---|---|---|
| `--grad-primary` | `linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%)` | CTA buttons, section accents |
| `--grad-dark` | `linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #2563eb 100%)` | Dark hero surfaces, featured cards |
| `--grad-light` | `linear-gradient(180deg, #ffffff 0%, #eff6ff 100%)` | Subtle section transitions |

---

## 05 · Typography System

### Font Stack

| Role | Font Family | Source |
|---|---|---|
| Headings / Display | Space Grotesk | Google Fonts |
| Body / UI | Inter | Google Fonts |
| Mono / Labels | Space Grotesk | Google Fonts |

**Import URL:** `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap`

In Next.js, use `next/font/google` for self-hosting and zero CLS.

### Type Scale

| Role | Size | Weight | Line Height | Letter Spacing | Font |
|---|---|---|---|---|---|
| H1 | 72px | 600 | 1 | -0.02em | Space Grotesk |
| H2 | 48px | 600 | 1.1 | -0.02em | Space Grotesk |
| H3 | 28px | 600 | 1.2 | -0.01em | Space Grotesk |
| H4 | 20px | 600 | 1.3 | — | Space Grotesk |
| Body | 16px | 400 | 1.6 | — | Inter |
| Small | 14px | 400 | 1.5 | — | Inter |
| Mono | 12px | 600 | 1.4 | 0.14em (uppercase) | Space Grotesk |

---

## 06 · Spacing Scale

Used consistently across all surfaces:

`4 · 6 · 8 · 10 · 12 · 14 · 16 · 20 · 24 · 28 · 32 · 40 · 48 · 56 · 64 · 80 · 100 · 120` px

Tailwind mapping: `1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 10, 12, 14, 16, 20, 24, 28`

---

## 07 · Border Radius

| Radius | Value | Use Case |
|---|---|---|
| Tight | 4px | Labels, badges |
| Small | 6–8px | Buttons, small chips |
| Input | 10–12px | Inputs, small cards |
| Card | 14–16px | Standard cards |
| Large | 20–24px | Hero cards, feature blocks |
| Pill | 999px | Pill badges, tokens |

---

## 08 · Shadows

| Token | Value | Usage |
|---|---|---|
| `--shadow-card` | `0 20px 40px rgba(15,23,42,0.08)` | Default card elevation |
| `--shadow-card-hover` | `0 20px 40px rgba(15,23,42,0.15)` | Card hover, KPI cards |
| `--shadow-featured` | `0 30px 60px rgba(15,23,42,0.15)` | Featured/hero cards |
| `--shadow-deep` | `0 30px 60px rgba(15,23,42,0.25)` | Deep hero shadow |
| `--shadow-cta` | `0 4px 14px rgba(37,99,235,0.35)` | CTA button at rest |
| `--shadow-cta-hover` | `0 8px 20px rgba(37,99,235,0.4)` | CTA button hover |

---

## 09 · Radial Glow Motif

Used on nearly every dark surface for depth. Apply via the `.glow-radial` class or the pseudo-element below:

```css
.glow-radial {
  position: relative;
  overflow: hidden;
}

.glow-radial::after {
  content: "";
  position: absolute;
  right: -150px;
  top: -150px;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(14,165,233,0.4) 0%, transparent 60%);
  filter: blur(60px);
  pointer-events: none;
}
```

---

## 10 · Voice & Tone

### Brand Voice

- **Direct.** No hedging. Say what you do, do what you say.
- **Premium.** Price-appropriate language. This is not a discount brand.
- **Technical.** Credit repair, AI, automations — speak with precision.
- **Trustworthy.** Earned confidence, not exaggerated claims.
- **Founder-led.** Rick's voice: personal, experienced, no corporate-speak.
- **Conversion-focused.** Every sentence earns its place on the page.
- **Execution-ready.** Action verbs, clear CTAs, no passive voice.
- **AI-native.** Comfortable with technology-forward language.
- **No-fluff.** Cut adjectives. Kill buzzwords. Be useful.

### Writing Rules

1. Start with the value, not the feature.
2. One idea per paragraph.
3. CTAs are commands: "Book Your Call", "Get Started", "See Your Report".
4. Numbers > adjectives: "200+ clients" not "many clients".
5. Social proof is specific: name the metric, cite the result.

---

## 11 · Component Patterns

### Buttons

All CTAs use the `.btn` base class with a variant. Five variants:

| Class | Style | Usage |
|---|---|---|
| `.btn-primary` | Solid `--rj-blue` with glow shadow | Primary CTAs |
| `.btn-gradient` | Blue → Sky gradient | Hero CTAs, conversion points |
| `.btn-dark` | Solid `--rj-navy` | Secondary actions on light backgrounds |
| `.btn-ghost` | Transparent with blue border | Tertiary, low-commitment actions |
| `.btn-light` | Light blue background | Inline actions, chip-style CTAs |

All buttons: hover → `translateY(-1px)` + shadow lift (150ms ease). Focus-visible: 4px `rgba(37,99,235,0.12)` outline.

### Cards

Default cards use `.card` — white background, 1px `--rj-line` border, `--shadow-card`. Hover lifts 2px and shifts border to `--rj-blue`.

Featured cards use `.card-featured` — `--grad-dark` background, white text, `--shadow-featured`. No border.

### Inputs

`.input` class — 1.5px `--rj-line` border, 10px radius. Focus → border shifts to `--rj-blue` + 4px blue halo.

### Status Pills

Four semantic variants: Hot (amber), Qualified (blue), Booked (green), Nurture (slate).

### Sticky Nav

`position: sticky` · `backdrop-filter: blur(20px)` · `background: rgba(255,255,255,0.85)` · `border-bottom: 1px solid var(--rj-line)`.

---

## 12 · Responsive Breakpoints

| Breakpoint | Width | Behavior |
|---|---|---|
| `sm` | 640px | Grids → single column |
| `md` | 768px | Nav collapses to hamburger, sidebar → drawer |
| `lg` | 1024px | Full desktop layout |
| `xl` | 1280px | Max content width |
| `2xl` | 1440px | Design reference width for Landing Page + Dashboard |

---

## 13 · Asset Overview

The RJ Complete Brand Library (v10.0) contains **84 branded files** across **16 sections** plus developer handoff:

- **01 · Photos of Rick** — 6 real portraits
- **02–04** — Print, Email, Social (not included in this download)
- **05 · Sales Decks & Docs** — 8 sales enablement surfaces
- **06 · Legal & Contracts** — 5 legal documents
- **07 · Product & Web** — 7 interactive digital surfaces
- **08 · Ads & Paid Media** — 3 paid media templates
- **09 · Video & Podcast** — 4 media assets
- **10 · Physical & Merch** — 11 physical + merchandise surfaces
- **11 · Credit Technology** — 1 credit report template
- **12 · Client Ops** — 4 client operations templates
- **13 · Investor & Corporate** — 6 investor + corporate documents
- **14 · Interactive Forms** — 8 multi-step forms + 1 shared CSS design system
- **15 · Founder Documents** — 6 founder legal + finance documents
- **16 · Developer & Backend** — Developer handoff spec + Cloudflare backend spec

Full inventory in `brand-assets.json`.

---

## 14 · Meta / Schema Pack

```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "RJ Business Solutions",
  "description": "Empowering Generational Wealth — premium credit-repair technology and AI-powered growth systems.",
  "url": "https://rjbusinesssolutions.org",
  "email": "support@rjbusinesssolutions.org",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "1342 NM 333",
    "addressLocality": "Tijeras",
    "addressRegion": "NM",
    "postalCode": "87059"
  },
  "founder": {
    "@type": "Person",
    "name": "Rick Jefferson"
  },
  "sameAs": [
    "https://www.linkedin.com/in/rick-jefferson-314998235",
    "https://www.tiktok.com/@rick_jeff_solution",
    "https://twitter.com/ricksolutions1",
    "https://github.com/rjbizsolution23-wq"
  ]
}
```

---

**Brand Kit Version:** 10.0 · **Prepared:** August 2026 · **Owner:** Rick Jefferson · RJ Business Solutions
