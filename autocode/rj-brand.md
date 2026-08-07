Yes — the next skill should be a **Brand & Productization Factory** that automatically turns every finished build into an **RJ Business Solutions** product with consistent naming, visual identity, UI language, documentation, onboarding, release assets, and support materials.

I’d make it a separate hierarchical skill so it can sit across **all three factories** and apply branding from planning through launch.

# RJ BUSINESS SOLUTIONS — BRAND FACTORY

## Universal Product Branding, Naming, UI Identity, Documentation & Launch Skill

---

# PURPOSE

This skill ensures every product, application, internal tool, SaaS platform, AI system, dashboard, automation, website, mobile experience, documentation set, training asset, and customer-facing deliverable produced by the factory ecosystem is consistently branded as:

# RJ Business Solutions

The goal is not to paste a logo onto finished software.

Branding must be integrated into:

PRODUCT STRATEGY
→ NAMING
→ INFORMATION ARCHITECTURE
→ USER EXPERIENCE
→ VISUAL SYSTEM
→ UI COPY
→ DOCUMENTATION
→ TRAINING
→ SUPPORT
→ RELEASE
→ CUSTOMER EXPERIENCE

---

# PACKAGE STRUCTURE

```text
rj-business-solutions-brand-factory/
├── SKILL.md
├── brand/
│   ├── brand-core.md
│   ├── voice-tone.md
│   ├── naming-system.md
│   ├── visual-system.md
│   ├── ui-system.md
│   ├── accessibility.md
│   ├── product-signature.md
│   └── brand-governance.md
├── modules/
│   ├── 00-brand-router.md
│   ├── 01-product-naming.md
│   ├── 02-brand-architecture.md
│   ├── 03-ui-branding.md
│   ├── 04-copy-branding.md
│   ├── 05-web-branding.md
│   ├── 06-mobile-branding.md
│   ├── 07-email-branding.md
│   ├── 08-documentation-branding.md
│   ├── 09-training-branding.md
│   ├── 10-support-branding.md
│   ├── 11-release-branding.md
│   ├── 12-marketing-assets.md
│   ├── 13-white-label-policy.md
│   ├── 14-brand-qa.md
│   └── 15-handoff.md
└── templates/
    ├── brand-manifest.md
    ├── product-identity.md
    ├── ui-copy.md
    ├── release-kit.md
    └── brand-audit.md
```

---

# SKILL.md

```markdown
---
name: rj-business-solutions-brand-factory
description: Universal branding and productization system for every RJ Business Solutions build. Applies consistent company identity, product naming, interface branding, UX copy, visual tokens, documentation, onboarding, training, support, launch materials, and brand QA across software produced by research, development, verification, and release factories.
---

# RJ Business Solutions Brand Factory

You are the brand architecture, product identity, UX writing, design-governance, documentation-branding, and launch-productization layer for RJ Business Solutions.

Every applicable build must emerge as a coherent RJ Business Solutions product.

You do not merely add branding after development.

You integrate identity throughout the product lifecycle.

---

# MASTER BRAND

Company:

RJ Business Solutions

Canonical written form:

RJ Business Solutions

Preferred short form:

RJ

Never independently invent alternate corporate spellings unless explicitly approved.

Examples to avoid:

RJBS
R.J. Business Solutions
RJ Biz Solutions
RJ Solutions

unless a specific approved brand manifest says otherwise.

---

# BRAND OBJECTIVE

Every RJ product should communicate:

PROFESSIONAL
CLEAR
CAPABLE
MODERN
TRUSTWORTHY
EFFICIENT
PRACTICAL
BUSINESS-FOCUSED

The experience should feel engineered to help a customer accomplish real work.

Avoid:

unnecessary hype
vague AI language
childish copy
overly playful interfaces
technical jargon presented to non-technical users
fake urgency
dark patterns

---

# PRODUCT BRANDING MODEL

Use:

RJ Business Solutions
+
Product Name
+
Functional Descriptor

Example structure:

RJ Business Solutions
RJ Flow
Business Workflow Automation

or:

RJ Business Solutions
RJ Insight
Business Intelligence Platform

Exact names must pass the Naming Module before use.

---

# PRODUCT SIGNATURE

Every applicable customer-facing build should include a tasteful RJ Business Solutions identity.

Possible locations:

application login
application shell
footer
about page
help center
documentation
emails
reports
exports
training
release notes

Default footer/signature:

"Powered by RJ Business Solutions"

or where RJ owns the entire product:

"© <year> RJ Business Solutions"

Do not overload every screen with repetitive branding.

Brand should reinforce trust without interfering with workflow.

---

# BRAND ROUTING

At project start:

1. determine product type,
2. establish product identity,
3. determine brand visibility,
4. create brand manifest,
5. pass tokens/copy requirements into development.

At implementation:

apply brand system.

At verification:

perform brand QA.

At release:

generate branded release and training materials.

---

# MANDATORY BRAND MANIFEST

For substantial products create:

docs/brand/brand-manifest.md

Include:

# Company
RJ Business Solutions

# Product Name

# Product Descriptor

# Positioning

# Target Audience

# Brand Relationship

# Product Voice

# Logo Treatment

# Color Tokens

# Typography Tokens

# Icon Style

# UI Radius

# Spacing Character

# Header Treatment

# Footer Treatment

# Loading Language

# Error Language

# Success Language

# Email Signature

# Documentation Header

# Training Identity

# Support Identity

# Legal/Footer Requirements

# White-Label Rules

# Accessibility Requirements
```

---

# BRAND ARCHITECTURE

Use one of these models.

## MODEL A — MASTERBRAND

Use when RJ Business Solutions itself is the product identity.

Example:

RJ Business Solutions Client Portal

Suitable for:

internal business systems
customer portals
service delivery platforms

## MODEL B — ENDORSED PRODUCT

Preferred default for reusable software.

Structure:

<Product Name>
by RJ Business Solutions

or:

<Product Name>
An RJ Business Solutions Product

## MODEL C — RJ PRODUCT FAMILY

Use for products intended to form an interconnected portfolio.

Pattern:

RJ <Name>

Examples:

RJ Flow
RJ Desk
RJ Insight
RJ Connect
RJ Automate

Names are illustrative only.

Check conflicts before final adoption.

## MODEL D — WHITE LABEL

Use when software is intentionally customer-branded.

RJ branding may remain only where contractually appropriate:

administration
legal metadata
about information
support attribution

Never force visible RJ branding where white-label requirements prohibit it.

---

# PRODUCT NAMING RULE

Do not casually invent names.

For new products:

1. understand functionality,
2. identify customer benefit,
3. generate naming territories,
4. search for obvious conflicts when web access exists,
5. check domain/product ecosystem collisions when appropriate,
6. score candidates,
7. recommend a winner.

Score:

MEMORABILITY
CLARITY
PROFESSIONALISM
EXTENSIBILITY
PRONUNCIATION
BRAND FIT
DISTINCTIVENESS
CONFLICT RISK

Avoid names that falsely imply:

certification
government affiliation
security guarantees
medical claims
financial guarantees
market dominance

---

# VISUAL SYSTEM

Brand implementation should rely on semantic design tokens.

Never scatter arbitrary colors throughout application code.

Recommended token model:

--rj-brand-primary
--rj-brand-primary-hover
--rj-brand-secondary
--rj-brand-accent

--rj-bg
--rj-bg-subtle
--rj-surface
--rj-surface-raised

--rj-text
--rj-text-muted
--rj-text-inverse

--rj-border
--rj-border-strong

--rj-success
--rj-warning
--rj-danger
--rj-info

--rj-focus

Colors must be sourced from the approved brand manifest.

If no approved color palette exists, create a proposed accessible palette and label it:

PROVISIONAL — REQUIRES BRAND APPROVAL

Do not imply provisional brand decisions are legally established trademarks or official corporate standards.

---

# TYPOGRAPHY SYSTEM

Use typography tokens:

--font-brand
--font-ui
--font-mono

--text-xs
--text-sm
--text-base
--text-lg
--text-xl
--text-2xl
--text-display

Do not introduce unnecessary font dependencies.

Prioritize:

readability
availability
performance
accessibility
professional character

---

# UI BRANDING

Apply branding consistently to:

authentication
navigation
dashboard
forms
dialogs
empty states
loading states
errors
success confirmations
notifications
settings
help
account
reports

Do not brand by decorating every component.

Create recognizable product identity using:

color
spacing
type hierarchy
navigation treatment
iconography
microcopy
interaction consistency

---

# BRAND VOICE

RJ Business Solutions copy should generally be:

direct
helpful
competent
concise
actionable
calm

Prefer:

"Your report is ready."

over:

"Awesome! We've worked our magic and your incredible report is ready!!!"

Prefer:

"We couldn't connect to QuickBooks. Check the connection and try again."

over:

"Oops! Something went wrong."

Errors should explain:

WHAT HAPPENED
WHAT THE USER CAN DO
WHAT HAPPENS NEXT

---

# BUTTON LANGUAGE

Prefer clear verbs:

Save
Continue
Create
Send
Review
Export
Connect
Approve
Retry

Avoid ambiguous:

OK
Yes
Submit

when a more meaningful action exists.

---

# AI FEATURES

Do not brand every capability as "AI."

Describe user value first.

Better:

"Summarize this report"

than:

"AI-Powered Intelligent Report Summary"

Use AI terminology when it materially helps users understand functionality.

---

# LOADING COPY

Prefer factual messaging.

Examples:

Loading your dashboard…
Generating report…
Connecting to service…
Processing file…

Do not claim success before completion.

---

# ERROR COPY

Pattern:

<What failed>. <Useful next action>.

Example:

"We couldn't save the invoice. Check your connection and try again."

Never expose:

stack traces
internal database errors
secret names
tokens
sensitive server details

to ordinary users.

---

# SUCCESS COPY

Confirm the accomplished outcome.

Example:

"Invoice sent."

Not:

"Operation completed successfully."

---

# EMPTY STATES

Every important empty state should answer:

WHAT IS THIS?
WHY IS IT EMPTY?
WHAT SHOULD I DO?

Example:

"No projects yet.

Create your first project to organize your client work."

[Create project]

---

# DOCUMENT BRANDING

Every significant customer-facing document should use a consistent identity.

Include where appropriate:

RJ Business Solutions
product name
document title
version
date
support reference

Potential footer:

"RJ Business Solutions — <Product Name>"

For technical documentation:

state exact product/version when relevant.

---

# EXPORTS & REPORTS

When the software produces customer reports, PDFs, spreadsheets, or exports, evaluate whether branding belongs in the artifact.

Possible elements:

RJ Business Solutions
product name
report title
generated date
customer organization
confidentiality label

Do not add branding where customers require clean exports or white labeling.

---

# EMAIL BRANDING

Product-generated email should clearly identify:

sender/product
purpose
requested action
support path

Default signature where appropriate:

RJ Business Solutions <Product Name>

Avoid visually excessive email templates.

Transactional clarity comes first.

---

# TRAINING BRANDING

All training materials should use:

consistent title cards
product name
release/version where useful
RJ Business Solutions attribution
consistent terminology
consistent UI labels
support destination

Do not train on outdated UI.

Training Factory must regenerate or flag content when material workflows change.

---

# SCREEN RECORDINGS

Before recording:

ensure correct product branding is visible,
remove developer/debug artifacts,
use approved test accounts,
remove sensitive information,
use realistic authorized content.

Recordings should demonstrate the actual verified release candidate.

---

# IN-APP TUTORIALS

Tutorial language must match UI language exactly.

If button says:

Create Project

tutorial must not say:

Start New Project

unless that is intentionally different terminology.

Brand consistency includes vocabulary.

---

# SUPPORT BRANDING

Support materials should clearly distinguish:

USER ACTION
ADMIN ACTION
RJ SUPPORT ACTION

Use consistent support identity.

Example footer:

Need additional help?
Contact RJ Business Solutions Support through your approved support channel.

Do not invent phone numbers, email addresses, URLs, hours, SLAs, or support guarantees.

Use only configured/verified contact information.

---

# RELEASE BRANDING

Every production release should have a release package.

Example:

release/
brand/
training/
support/
docs/

Release notes should contain:

Product
Version
Release date
What's new
Improvements
Resolved issues
Known issues
Upgrade notes
Support notes

Use customer language rather than raw commit summaries.

---

# MARKETING HANDOFF

For products intended for external sale, create a marketing brief.

Include:

PRODUCT NAME
DESCRIPTOR
ONE-LINE POSITIONING
TARGET CUSTOMER
PROBLEM
BENEFIT
KEY CAPABILITIES
DIFFERENTIATORS
PROOF
SCREENSHOTS REQUIRED
DEMO STORY
CTA
FAQ
DISCLAIMERS

Never manufacture testimonials, customer numbers, ROI, awards, usage statistics, or performance claims.

Claims require evidence.

---

# PRODUCT PAGE STRUCTURE

Default:

Hero
→ Outcome
→ Problems solved
→ Key capabilities
→ How it works
→ Evidence / verified advantages
→ Screens
→ Integrations
→ Security/trust where appropriate
→ FAQ
→ CTA

Avoid generic AI-marketing filler.

---

# BRAND QA

Brand QA is separate from functional QA.

Inspect:

PRODUCT NAME
COMPANY NAME
LOGOS
COLORS
TYPOGRAPHY
ICONS
SPACING
COPY
TERMINOLOGY
FOOTERS
EMAILS
REPORTS
DOCS
TRAINING
SUPPORT
RESPONSIVENESS
ACCESSIBILITY
WHITE LABELING

Search the repository for:

old product names
placeholder company names
Lorem Ipsum
example.com
Acme
TODO branding
default framework logos
template metadata
favicon leftovers
boilerplate titles

Remove accidental template branding.

---

# BRAND SECURITY

Never embed confidential brand assets, customer information, API credentials, or unreleased strategy into public client assets.

Separate:

PUBLIC BRAND DATA

from:

INTERNAL BUSINESS DATA.

---

# BRAND COMPLETION JUDGE

Before release evaluate:

## Identity

Does the product clearly belong to the intended RJ brand architecture?

## Consistency

Are naming and terminology consistent?

## UI

Does visual presentation follow the manifest?

## Copy

Is language professional and actionable?

## Accessibility

Are visual choices accessible?

## Documentation

Does documentation match the product?

## Training

Does training show current UI?

## Support

Are support instructions valid?

## Exports

Are generated assets correctly branded?

## Metadata

Titles, icons, manifests, PWA metadata, social metadata and package descriptors correct?

## White Label

Are client-brand requirements respected?

Verdict:

BRAND APPROVED
BRAND APPROVED WITH EXCEPTIONS
BRAND REJECTED
BLOCKED

A software release cannot receive final RJ product approval until required brand QA passes.

````

---

# brand/brand-core.md

```markdown
# RJ Business Solutions Brand Core

Canonical company name:

RJ Business Solutions

Brand idea:

Practical business technology that turns complex work into clear, reliable systems.

Brand characteristics:

Professional
Capable
Clear
Efficient
Trustworthy
Modern
Practical

The brand should communicate:

"We understand the work and built this to make it easier."

Avoid communicating:

"We added technology because technology is impressive."
````

---

# brand/voice-tone.md

```markdown
# Voice & Tone

RJ Business Solutions speaks like an experienced business technology partner.

VOICE:

CLEAR
DIRECT
USEFUL
CALM
CONFIDENT
RESPECTFUL

Avoid:

buzzword density
excessive exclamation
fake friendliness
vague errors
unnecessary technical language
unverifiable claims

Match language to user expertise.

Customer-facing:
outcome-oriented.

Administrator:
precise.

Developer documentation:
technical and explicit.

Incident/error:
calm and actionable.
```

---

# brand/naming-system.md

```markdown
# Naming System

Preferred portfolio approach:

RJ <Distinctive Name>

when building a family of proprietary RJ products.

Alternative:

<Distinctive Product Name>
by RJ Business Solutions

Names should be:

short
pronounceable
memorable
professional
extensible

Avoid overly descriptive names that become limiting.

Before recommending a final externally marketed name, perform reasonable conflict research where tools permit.

Naming output:

CANDIDATE
RATIONALE
PRODUCT FIT
EXTENSIBILITY
CONFLICT NOTES
SCORE
```

---

# modules/14-brand-qa.md

```markdown
# Brand QA

Run after functional verification.

Automated checks where possible:

search codebase for placeholder brands,
inspect metadata,
inspect favicon/icons,
inspect app manifest,
inspect title tags,
inspect email templates,
inspect generated reports,
inspect legal/footer strings.

Visual checks:

desktop
tablet
mobile
dark mode when applicable
high zoom
focus states
errors
empty states
loading
auth
primary workflows

Evidence:

screenshot
recording
DOM/metadata inspection
generated artifact

Every finding receives:

LOCATION
EXPECTED
ACTUAL
SEVERITY
EVIDENCE
FIX
RETEST
```

---

# modules/15-handoff.md

```markdown
# Brand Factory Handoff

The Brand Factory interfaces with all other factories.

## Research Factory receives

brand positioning constraints,
target audience,
existing portfolio,
approved terminology.

## Software Factory receives

brand manifest,
design tokens,
product identity,
UI copy rules,
asset references,
metadata requirements.

## Verification Factory receives

brand acceptance criteria,
visual QA checklist,
content consistency requirements.

## Training Factory receives

current product vocabulary,
brand identity,
approved visuals,
support references.

## Release Judge receives

brand QA verdict.

Brand requirements are versioned.

When branding changes materially:

update manifest
→ update product
→ rerun relevant brand QA
→ update documentation
→ update training assets.
```

---

# BRAND MANIFEST TEMPLATE

```markdown
# RJ Business Solutions Brand Manifest

## Product

Name:

Descriptor:

Version:

## Ownership

RJ Business Solutions

## Brand Architecture

<Masterbrand | RJ Product Family | Endorsed | White Label>

## Positioning

## Audience

## Product Promise

## Voice

## Terminology

| Concept | Approved wording | Avoid |
|---|---|---|
| | | |

## Identity

Logo:
<asset/reference>

Primary:
<token/value>

Secondary:

Accent:

Background:

Surface:

Text:

Success:

Warning:

Danger:

Focus:

## Typography

Brand:

UI:

Mono:

## UI Character

Radius:

Shadow:

Spacing:

Iconography:

## Application Identity

Browser title:

Application name:

Short name:

Favicon:

Manifest name:

Login treatment:

Navigation treatment:

Footer:

About page:

## Communications

Email sender display:

Email signature:

Report footer:

Documentation title:

Training title:

Support identity:

## Accessibility

Contrast requirements:

Focus requirements:

Motion requirements:

## White Label Rules

## Prohibited Treatments

## Approval State

<PROVISIONAL | APPROVED>
```

---

# COMPLETE FACTORY ECOSYSTEM

```text
                    RJ BUSINESS SOLUTIONS
                           │
                           ▼
                ┌─────────────────────┐
                │ BRAND FACTORY       │
                │ identity + rules    │
                └──────────┬──────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   RESEARCH FACTORY   SOFTWARE FACTORY   VERIFICATION
          │                │                │
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                  RELEASE CANDIDATE
                           │
                           ▼
                  BRAND + RELEASE QA
                           │
                           ▼
              TRAINING / SUPPORT FACTORY
                           │
                           ▼
                       PRODUCTION
                           │
                           ▼
                    RJ CUSTOMER
```

---

# UNIVERSAL RJ BUILD RULE

Every new project begins with:

1. product objective,
2. RJ brand architecture,
3. product identity,
4. brand manifest,
5. research,
6. architecture,
7. development,
8. verification,
9. brand QA,
10. training/support,
11. release.

Branding is therefore not:

BUILD
→ ADD LOGO.

It is:

RJ IDENTITY
→ PRODUCT DESIGN
→ BUILD
→ EXPERIENCE
→ PROOF
→ CUSTOMER DELIVERY.

---

# FINAL RULE

Every applicable product should make a user immediately understand:

WHO MADE THIS?
RJ Business Solutions.

WHAT IS THIS?
The named product/capability.

WHAT DOES IT HELP ME DO?
The business outcome.

WHAT SHOULD I DO NEXT?
A clear action.

HOW DO I GET HELP?
A verified support path.

The result should feel like a coherent RJ Business Solutions product—not a generic application with a company name pasted on top.

One thing I intentionally left **provisional** is the exact logo, colors, fonts, slogan, and legal trademark treatment. Those should become a single authoritative RJ brand manifest once you establish them; after that, every factory can enforce them automatically rather than allowing agents to invent slightly different versions on each build.
