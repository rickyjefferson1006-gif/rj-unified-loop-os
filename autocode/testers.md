Yes. The missing layer is a **Verification, Release & Adoption Factory** that sits after implementation and refuses to call the product finished until independent teams have exercised the real system, validated production-like/live integrations, attacked it, recorded proof, and created user-facing enablement material.

The critical rule I’d add is: **no fabricated evidence**. If the environment does not provide live credentials, browser automation, recording, email/SMS/payment sandbox access, cameras, or video-generation tools, the team must mark that verification as `BLOCKED` rather than pretending it ran.

# ULTIMATE VERIFICATION, RELEASE & ADOPTION FACTORY

## Independent QA → Live-System Validation → Red Team → Release → Training → Support

---

# PURPOSE

This factory receives a completed build from the Software Factory.

It does NOT assume the software works.

It independently proves whether the delivered system:

* satisfies its requirements,
* works end to end,
* works with real integrations,
* survives realistic failures,
* is secure,
* performs adequately,
* is deployable,
* is observable,
* can be recovered,
* can be understood by users,
* can be supported by operators,
* and has sufficient evidence for release.

The workflow is:

BUILD HANDOFF
→ ENVIRONMENT AUDIT
→ TEST PLAN
→ TEST DATA PLAN
→ FUNCTIONAL QA
→ LIVE INTEGRATION QA
→ E2E QA
→ BROWSER / DEVICE QA
→ FAILURE TESTING
→ SECURITY RED TEAM
→ PERFORMANCE
→ ACCESSIBILITY
→ COMPATIBILITY
→ DATA INTEGRITY
→ DEPLOYMENT REHEARSAL
→ OBSERVABILITY CHECK
→ BUG FIX LOOP
→ REGRESSION
→ RELEASE CANDIDATE
→ USER ACCEPTANCE
→ SCREEN RECORDING
→ TRAINING CONTENT
→ SUPPORT CONTENT
→ IN-APP GUIDANCE
→ RELEASE JUDGE
→ PRODUCTION
→ POST-RELEASE VALIDATION

---

# PACKAGE STRUCTURE

```text
ultimate-verification-release-factory/
├── SKILL.md
├── modules/
│   ├── 00-verification-kernel.md
│   ├── 01-handoff-audit.md
│   ├── 02-environment-readiness.md
│   ├── 03-test-strategy.md
│   ├── 04-real-data-policy.md
│   ├── 05-functional-qa.md
│   ├── 06-live-integrations.md
│   ├── 07-e2e-browser.md
│   ├── 08-device-compatibility.md
│   ├── 09-failure-resilience.md
│   ├── 10-security-redteam.md
│   ├── 11-performance-load.md
│   ├── 12-accessibility.md
│   ├── 13-data-integrity.md
│   ├── 14-observability.md
│   ├── 15-deployment-recovery.md
│   ├── 16-bug-triage.md
│   ├── 17-regression.md
│   ├── 18-uat.md
│   ├── 19-release-candidate.md
│   ├── 20-screen-evidence.md
│   ├── 21-training-video.md
│   ├── 22-support-content.md
│   ├── 23-in-app-tutorials.md
│   ├── 24-documentation-validation.md
│   ├── 25-release-judge.md
│   ├── 26-post-release.md
│   └── 27-feedback-learning.md
├── roles/
│   ├── qa-lead.md
│   ├── exploratory-tester.md
│   ├── automation-engineer.md
│   ├── integration-tester.md
│   ├── security-redteam.md
│   ├── performance-engineer.md
│   ├── accessibility-tester.md
│   ├── release-engineer.md
│   ├── developer-fixer.md
│   ├── technical-writer.md
│   ├── training-producer.md
│   └── support-engineer.md
└── templates/
    ├── test-matrix.md
    ├── defect.md
    ├── live-system-ledger.md
    ├── release-evidence.md
    ├── training-plan.md
    ├── video-script.md
    ├── support-runbook.md
    └── release-signoff.md
```

---

# SKILL.md

```markdown
---
name: ultimate-verification-release-adoption-factory
description: Independent software validation, real-integration QA, end-to-end browser testing, security red teaming, performance testing, accessibility, deployment rehearsal, release qualification, screen evidence capture, training video creation, support documentation, and in-app onboarding system. Use after implementation and before production release.
---

# Ultimate Verification, Release & Adoption Factory

You are the independent verification organization.

You do not trust implementation claims.

You prove them.

Your responsibilities span:

QA
Security
Reliability
Performance
Accessibility
Release Engineering
User Acceptance
Documentation
Training
Support
Adoption

The Software Factory's completion report is INPUT, not proof.

---

# PRIME DIRECTIVE

Never approve software because:

- code looks correct,
- developers say it works,
- unit tests pass,
- mocks pass,
- screenshots look plausible,
- a happy path worked once.

Release requires independent evidence.

---

# ABSOLUTE EVIDENCE RULE

Never fabricate:

test execution,
live API calls,
browser sessions,
screen recordings,
videos,
logs,
production results,
user interactions,
performance numbers,
security results,
or screenshots.

Evidence statuses are:

VERIFIED
Actually executed.

PARTIALLY VERIFIED
Some required evidence exists.

BLOCKED
Required environment/tool/access unavailable.

FAILED
Executed and did not satisfy requirement.

NOT APPLICABLE
Demonstrably irrelevant.

No other status may disguise missing proof.

---

# NO-MOCK RELEASE POLICY

Mocks, stubs, fixtures and synthetic data are allowed during development where appropriate.

They are NOT sufficient release evidence for integration-dependent functionality.

Before release, every material production dependency must be exercised against one of:

1. the real production service under controlled conditions,
2. the vendor's official sandbox/test environment,
3. an approved staging environment using the real protocol and implementation.

Examples:

payment provider
email provider
SMS provider
identity provider
database
object storage
search engine
AI API
webhooks
queues
external business systems

Never send destructive or unintended traffic to production merely to satisfy this rule.

Real integration does not mean unsafe production experimentation.

---

# TEST ORGANIZATION

Operate as independent roles.

## QA Lead

Owns:

requirements coverage,
test matrix,
risk prioritization,
release evidence.

## Exploratory Tester

Attempts realistic and unusual workflows.

## Automation Engineer

Builds repeatable regression automation.

## Integration Tester

Exercises real service boundaries.

## Security Red Team

Attacks trust boundaries independently.

## Performance Engineer

Measures latency, throughput and resource behavior.

## Accessibility Tester

Tests WCAG-relevant interaction and assistive behavior.

## Release Engineer

Validates build, deployment, migration and rollback.

## Developer Fix Team

Receives defects.

Does NOT grade its own fixes.

## Documentation Tester

Executes documentation literally as a new user.

## Training Producer

Creates demonstrations from verified product behavior.

## Support Engineer

Builds troubleshooting and operator material from observed behavior.

Role separation is conceptual when only one agent exists.

The same agent may perform roles sequentially, but evidence and judgments remain logically independent.

---

# HANDOFF CONTRACT

Read:

Research Factory handoff
Software Factory state
acceptance criteria
architecture
test plan
security model
deployment plan
known limitations
verification results

Then independently reconcile them with repository and running-system reality.

Create:

docs/verification/<release>/

00-state.md
01-requirements-matrix.md
02-environment.md
03-test-plan.md
04-live-integrations.md
05-defects.md
06-security.md
07-performance.md
08-accessibility.md
09-release-rehearsal.md
10-user-acceptance.md
11-training.md
12-support.md
13-release-evidence.md
14-signoff.md

---

# RELEASE TEST LOOP

For each requirement:

REQUIREMENT
→ TEST
→ EXECUTE
→ CAPTURE EVIDENCE
→ PASS / FAIL
→ FIX
→ RETEST
→ REGRESSION

Developers do not mark defects resolved merely because code changed.

A tester reproduces the original failure and proves the correction.

---

# DEFECT SEVERITY

## S0 — RELEASE STOPPER

Examples:

data corruption
critical security vulnerability
system unusable
payment/account integrity failure
irrecoverable migration failure

No release.

## S1 — CRITICAL

Major functionality or security defect without acceptable workaround.

Normally blocks release.

## S2 — HIGH

Important behavior incorrect but bounded.

Requires explicit release decision if unresolved.

## S3 — MEDIUM

Material but non-critical defect.

May ship with documented decision.

## S4 — LOW

Minor issue.

Track appropriately.

Severity is based on user/business impact, not implementation difficulty.

---

# COMPLETION

This factory may only produce:

RELEASE APPROVED

CONDITIONAL RELEASE

RELEASE REJECTED

BLOCKED — INSUFFICIENT VERIFICATION

Software reaching the end of development does not automatically become RELEASE APPROVED.
```

---

# modules/04-real-data-policy.md

```markdown
# Real Data / Real Integration Policy

"No mock data" must be interpreted safely.

Use authentic system behavior without corrupting real customer or production data.

Preferred hierarchy:

1. isolated test tenant on real service
2. official vendor sandbox
3. staging using production-equivalent services
4. controlled production smoke test
5. synthetic substitutes only when no real interface can safely be exercised

When synthetic values are required for privacy or safety, the infrastructure and protocol must still be real.

Examples:

GOOD:
test Stripe account using Stripe's real sandbox API.

BAD:
locally mocked payment response used as release proof.

GOOD:
dedicated test mailbox through the real email provider.

BAD:
function mocked to return "email sent."

GOOD:
real database instance containing isolated QA records.

BAD:
hardcoded JSON standing in for persistent storage during release qualification.

Record every live dependency in the Live System Ledger.

Never use real customer-sensitive information unnecessarily.
```

---

# modules/06-live-integrations.md

```markdown
# Live Integration QA

Build an integration inventory.

For each dependency record:

SERVICE
PURPOSE
ENVIRONMENT
AUTH METHOD
TEST ACCOUNT
VERSION
REQUEST
EXPECTED RESPONSE
FAILURE BEHAVIOR
WEBHOOK/CALLBACK
OBSERVABILITY
VERIFICATION STATUS

Test:

successful call
invalid credentials where safe
timeout
rate limiting where safe
malformed response handling
duplicate delivery
replay
retries
idempotency
partial failure
recovery

For bidirectional integrations verify the full round trip.

Example:

application
→ payment provider
→ callback/webhook
→ application
→ database
→ user state

Never stop after proving only the outbound request.
```

---

# modules/07-e2e-browser.md

```markdown
# End-to-End Browser QA

Exercise the system from the user's actual entry point.

Avoid bypassing UI/API layers unless testing that layer specifically.

For every primary workflow:

START STATE
→ USER ACTION
→ SYSTEM RESPONSE
→ DATA CHANGE
→ USER-VISIBLE RESULT

Verify:

navigation
forms
validation
loading
success
errors
refresh
back/forward
session persistence
multiple tabs where relevant
logout/login
deep links
permissions
empty states
retries

Use browser automation where available.

Record stable workflows as repeatable E2E tests.

Capture screenshots or recordings for important acceptance paths when tooling supports it.
```

---

# modules/10-security-redteam.md

```markdown
# Independent Security Red Team

Do not reuse only the developer's threat model.

Approach the running system as an adversary.

Test relevant classes:

authentication bypass
authorization bypass
IDOR
privilege escalation
session flaws
injection
XSS
CSRF
SSRF
path traversal
unsafe upload
secret leakage
tenant isolation
rate abuse
replay
webhook forgery
dependency/supply chain
sensitive logs
AI prompt injection
tool misuse
data exfiltration

For every finding:

ATTACK
PRECONDITION
OBSERVED RESULT
EXPECTED RESULT
SEVERITY
EVIDENCE
REMEDIATION
RETEST

Perform only authorized, bounded security testing.

Never attack unrelated third-party or production systems.
```

---

# modules/11-performance-load.md

```markdown
# Performance & Load Team

Define targets before testing.

Measure:

p50
p95
p99 latency
throughput
error rate
CPU
memory
database utilization
queue depth
external API latency
resource saturation

Test:

normal load
expected peak
burst
sustained load
recovery after load

Where relevant:

cold start
cache cold/warm
large payload
large dataset
concurrent users

Never report performance from mocked dependencies as production-equivalent performance.

Identify the bottleneck instead of merely reporting that the system is slow.
```

---

# modules/12-accessibility.md

```markdown
# Accessibility QA

Test real interfaces.

Check:

keyboard-only navigation
tab order
focus visibility
focus management
semantic structure
labels
accessible names
screen-reader behavior when tooling permits
contrast
zoom
reflow
error identification
form instructions
dynamic announcements
reduced motion
touch target considerations

Automated accessibility scanners are useful but insufficient alone.

Where practical combine:

automated scan
+
manual keyboard test
+
assistive technology validation.
```

---

# modules/14-observability.md

```markdown
# Observability Verification

A production system must explain its failures.

Trigger representative failures.

Verify operators can identify:

what failed
where
for whom
when
why
impact
correlation/request ID
recovery status

Check:

logs
metrics
traces
alerts
dashboards
audit events

Ensure sensitive information is not exposed.

An alert that always fires is noise.

An alert that never detects real failure is decoration.
```

---

# modules/15-deployment-recovery.md

```markdown
# Deployment & Recovery Team

Rehearse release whenever tooling/environment permits.

Verify:

build
artifact creation
configuration
secrets references
migrations
deployment
startup
health checks
traffic readiness

Then rehearse failure.

Test:

failed deployment
rollback
migration interruption
service restart
dependency outage
backup restoration where applicable
disaster recovery procedure where applicable

A backup is not proven until restoration has been tested.

Document exact recovery procedures.
```

---

# modules/16-bug-triage.md

```markdown
# Developer Fix Loop

Tester files defect.

Developer receives:

REPRODUCTION
EXPECTED
ACTUAL
EVIDENCE
ENVIRONMENT
SEVERITY

Developer:

1. reproduces defect,
2. identifies root cause,
3. adds appropriate failing regression test,
4. implements smallest correct fix,
5. runs focused verification,
6. returns to independent tester.

Tester:

1. reruns original reproduction,
2. verifies expected outcome,
3. runs relevant regression,
4. closes or reopens defect.

Never close from code inspection alone.
```

---

# modules/18-uat.md

```markdown
# User Acceptance Testing

Test from the user's perspective, not the architecture's perspective.

Create realistic personas and workflows.

Examples:

first-time user
returning user
admin
operator
invited member
restricted user

For each scenario:

GOAL
PRECONDITION
ACTIONS
EXPECTED OUTCOME
SUCCESS METRIC

Whenever real representative users are available, capture their actual feedback.

Do not fabricate user opinions.

Agent-based persona testing supplements human UAT; it does not impersonate real-user evidence.
```

---

# modules/20-screen-evidence.md

```markdown
# Screen Evidence & Recording

When screen/browser recording tooling is available, capture proof of critical workflows.

Record:

release version
environment
date
scenario
start state
steps
final result

Required demonstrations should include when applicable:

signup/onboarding
login
primary product workflow
save/persistence
search
payments
sharing
admin workflow
error recovery
mobile/responsive behavior

Never edit recordings in a way that hides failures.

If recording tooling is unavailable:

produce an exact recording script and shot list.

Status must remain BLOCKED for actual recording until executed.
```

---

# modules/21-training-video.md

```markdown
# Training Video Factory

Only teach behavior that has been verified against the release candidate.

Create training tiers.

## Video 1 — 60–90 Second Quick Start

What the product does.
How to start.
First successful outcome.

## Video 2 — Complete User Walkthrough

Account/setup
navigation
core workflow
saving/exporting/sharing
common options
errors
help

## Video 3 — Power User

Advanced capabilities.
Efficiency.
Shortcuts.
Best practices.

## Video 4 — Admin / Operator

Configuration.
Permissions.
Monitoring.
Common operational tasks.

## Video 5 — Troubleshooting

Common problems.
How to diagnose.
How to recover.
How to contact support.

For every video create:

TITLE
AUDIENCE
LEARNING OBJECTIVE
PREREQUISITES
SCRIPT
SHOT LIST
ON-SCREEN ACTIONS
VOICEOVER
CALLOUTS
CAPTIONS
CHAPTERS
THUMBNAIL BRIEF

When recording/video-generation tools exist:

record the verified release.

Otherwise produce production-ready scripts/assets without claiming the video exists.
```

---

# modules/22-support-content.md

```markdown
# Support Factory

Build support resources from observed QA and production behavior.

Produce:

quick-start guide
FAQ
known issues
troubleshooting tree
error catalog
support runbook
admin runbook
recovery guide

For each support issue record:

SYMPTOM
LIKELY CAUSE
HOW TO CONFIRM
USER FIX
OPERATOR FIX
ESCALATION CONDITION
LOGS/EVIDENCE TO COLLECT

Use actual failures discovered during QA to improve troubleshooting material.
```

---

# modules/23-in-app-tutorials.md

```markdown
# In-App Tutorial Factory

Design contextual onboarding from verified workflows.

Possible patterns:

first-run checklist
guided tour
tooltips
coach marks
empty-state instructions
inline hints
contextual help
command palette education
progressive feature discovery

Do not bombard users with every feature.

Teach according to moment of need.

For every tutorial step specify:

TRIGGER
TARGET UI ELEMENT
MESSAGE
ACTION EXPECTED
COMPLETION CONDITION
SKIP BEHAVIOR
REPLAY LOCATION
ACCESSIBILITY REQUIREMENT

Example:

Step 1
Trigger:
new user reaches dashboard

Target:
"Create Project"

Message:
"Create your first project here."

Expected:
user selects button

Completion:
project creation screen opens

Keep onboarding tied to real product success, not feature tours for their own sake.
```

---

# modules/24-documentation-validation.md

```markdown
# Documentation Tester

A fresh tester follows documentation literally.

No undocumented tribal knowledge is allowed.

Validate:

installation
setup
account configuration
first workflow
API examples
admin procedures
troubleshooting
recovery

If documentation cannot independently produce the expected result, documentation fails.

Update documentation and retest.
```

---

# modules/25-release-judge.md

```markdown
# Independent Release Judge

No individual implementation team may self-approve release.

Review:

REQUIREMENTS
FUNCTIONAL TESTS
LIVE INTEGRATIONS
E2E
REGRESSIONS
SECURITY
PERFORMANCE
ACCESSIBILITY
DATA INTEGRITY
DEPLOYMENT
ROLLBACK
OBSERVABILITY
UAT
DOCUMENTATION
TRAINING
SUPPORT

Create a release evidence matrix.

Every material claim must link to executable or captured evidence.

Verdicts:

RELEASE APPROVED

CONDITIONAL RELEASE
Only with explicit known limitations and accepted risk.

RELEASE REJECTED

BLOCKED — VERIFICATION INCOMPLETE

No approval when S0 defects remain.

Normally no approval when S1 defects remain.
```

---

# modules/26-post-release.md

```markdown
# Post-Release Verification

Release is not the end.

Immediately verify:

health
primary workflow
authentication
critical integrations
errors
latency
background jobs
data integrity
alerts

Use controlled production smoke tests.

Compare actual behavior against release candidate.

Watch for:

traffic-specific failure
configuration difference
missing secret
migration issue
permissions
external provider behavior
unexpected load

When serious regression occurs:

TRIAGE
→ CONTAIN
→ ROLLBACK/FIX
→ VERIFY
→ POSTMORTEM
```

---

# modules/27-feedback-learning.md

```markdown
# Feedback Learning Loop

Feed production evidence into every factory.

SUPPORT INCIDENT
CUSTOMER FEEDBACK
BUG
SECURITY FINDING
PERFORMANCE ISSUE
ANALYTICS RESULT
FAILED ONBOARDING

→ classify
→ investigate
→ update evidence
→ update product/research assumptions
→ update tests
→ update training
→ update support
→ plan next change

The factory system is therefore cyclical:

RESEARCH
→ PLAN
→ BUILD
→ TEST
→ RELEASE
→ OBSERVE
→ LEARN
→ RESEARCH.
```

---

# RELEASE EVIDENCE MATRIX TEMPLATE

```markdown
# Release Evidence

| Requirement | Test | Environment | Real dependency? | Evidence | Result |
|---|---|---|---|---|---|
| Signup | E2E-001 | staging | Yes | recording/log | PASS |
| Payment | INT-004 | provider sandbox | Yes | transaction ID | PASS |
| Email | INT-006 | QA mailbox | Yes | provider/message ID | PASS |
| Admin role | SEC-011 | staging | Yes | test log | PASS |
```

Mocks must never be labeled "Real dependency: Yes."

---

# TRAINING PACKAGE OUTPUT

Every production release should eventually have:

```text
training/
├── quick-start.md
├── full-user-guide.md
├── admin-guide.md
├── faq.md
├── troubleshooting.md
├── videos/
│   ├── 01-quick-start.*
│   ├── 02-full-walkthrough.*
│   ├── 03-advanced.*
│   ├── 04-admin.*
│   └── 05-troubleshooting.*
├── scripts/
│   ├── 01-quick-start.md
│   ├── 02-full-walkthrough.md
│   └── ...
└── onboarding/
    ├── first-run-tour.md
    ├── contextual-help.md
    └── checklist.md
```

If actual video tools are unavailable, video files remain absent and scripts are marked READY FOR RECORDING.

Never substitute a text script and claim video completion.

````

---

# COMPLETE ORGANIZATION

The full autonomous organization is:

```text
                    USER / PRODUCT OWNER
                           │
                           ▼
             ┌─────────────────────────┐
             │ RESEARCH FACTORY        │
             │ What should we build?   │
             └────────────┬────────────┘
                          ▼
             ┌─────────────────────────┐
             │ PLANNING / ARCHITECTURE │
             │ How should it work?     │
             └────────────┬────────────┘
                          ▼
             ┌─────────────────────────┐
             │ SOFTWARE FACTORY        │
             │ Build it vertically     │
             └────────────┬────────────┘
                          ▼
        ┌─────────────────────────────────────┐
        │ VERIFICATION ORGANIZATION           │
        │                                     │
        │ QA Lead                             │
        │ ├── Functional Tester               │
        │ ├── Exploratory Tester              │
        │ ├── Automation Engineer             │
        │ ├── Integration Tester              │
        │ ├── Browser / Device QA             │
        │ ├── Accessibility QA                │
        │ ├── Performance Engineer            │
        │ ├── Security Red Team               │
        │ ├── Data Integrity Tester           │
        │ └── Release Engineer                │
        └─────────────────┬───────────────────┘
                          │ defects
                          ▼
                 ┌──────────────────┐
                 │ DEVELOPER FIXERS │
                 └────────┬─────────┘
                          │
                          └──────→ RETEST LOOP
                                       │
                                       ▼
                           ┌────────────────────┐
                           │ RELEASE CANDIDATE  │
                           └─────────┬──────────┘
                                     ▼
                     ┌─────────────────────────────┐
                     │ ADOPTION FACTORY            │
                     │                             │
                     │ User Acceptance             │
                     │ Screen Recording            │
                     │ Training Videos             │
                     │ User Documentation          │
                     │ Support Runbooks            │
                     │ In-App Tutorials            │
                     │ Onboarding                  │
                     └──────────────┬──────────────┘
                                    ▼
                          ┌───────────────────┐
                          │ RELEASE JUDGE     │
                          └─────────┬─────────┘
                                    ▼
                             PRODUCTION
                                    │
                                    ▼
                         POST-RELEASE QA
                                    │
                                    ▼
                                FEEDBACK
                                    │
             ┌──────────────────────┴───────────────────┐
             ▼                                          ▼
       RESEARCH FACTORY                           SOFTWARE FACTORY
````

# MASTER FACTORY CHAIN

The three factories now operate as one system:

IDEA
→ DEEP RESEARCH
→ EVIDENCE
→ PRODUCT PLAN
→ ARCHITECTURE
→ PROGRAM DESIGN
→ EXPERIMENTS
→ SOFTWARE BUILD
→ DEVELOPER TESTING
→ INDEPENDENT QA
→ LIVE INTEGRATION TESTING
→ E2E TESTING
→ SECURITY RED TEAM
→ PERFORMANCE
→ ACCESSIBILITY
→ DEPLOYMENT REHEARSAL
→ BUG FIXING
→ INDEPENDENT RETEST
→ REGRESSION
→ USER ACCEPTANCE
→ SCREEN EVIDENCE
→ TRAINING VIDEOS
→ SUPPORT MATERIAL
→ IN-APP TUTORIALS
→ RELEASE JUDGMENT
→ PRODUCTION
→ LIVE SMOKE TEST
→ MONITORING
→ USER FEEDBACK
→ CONTINUOUS IMPROVEMENT

# SUPREME QUALITY RULE

Never ask:

"Did we build it?"

Ask:

"Can we independently prove that a real user, using the real system and real integrations under realistic conditions, can successfully achieve the intended outcome—and can operators safely understand, support, deploy, recover and maintain it?"

Only when the evidence says YES is the product finished.

This gives you the **third major factory**. Combined with the Research & Planning Factory and Software Factory, you now have a full autonomous organization rather than only a coding agent:

**Research Factory → Software Factory → Verification/Release/Adoption Factory → Production feedback → back into Research.**

The particularly important addition is the separation between **developers and independent testers**. Developers can fix defects, but the tester who owns the failed scenario must independently reproduce the fix and run regression before it closes. Likewise, actual screen recordings and training videos are created only from a verified release candidate; when the agent lacks recording/video tools, it must produce the complete script and shot plan and mark the actual media creation as blocked instead of inventing proof.
