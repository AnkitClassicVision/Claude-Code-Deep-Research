# BENCHMARK-2026-06-09: Deep Research V3 vs V4

Fixed question: **What is the measured effect of patient self-scheduling on no-show rates in outpatient medical practices?**

## Surface note

This benchmark was executed from Hermes using web fetches and deterministic V4 scripts. Native Claude Code/Claude.ai surface verification is tracked separately in the deploy report. No client-facing systems, CRM, email, calendar, EHR, or production workflow was touched.

external_actions_taken=0 for both run cards.

## Metrics

| Metric | V3 replay | V4 Standard |
|---|---:|---:|
| Fetch budget | 30 | 30 |
| Verified claims | 2 post-hoc | 8 |
| Cost per VERIFIED claim | n/a: cost telemetry unavailable | n/a: cost telemetry unavailable |
| Citation-audit pass rate | 0% post-hoc (FAIL) | 100% (PASS with --fetch) |
| Decision-claim gate coverage | n/a: no V3 floor gate | 100% (1/1 at >=0.92) |
| Wall-clock | not reliably instrumented | not reliably instrumented |
| % budget on losing/confounder branches | not instrumented | 33% |
| Red-team FATAL / MATERIAL | 0 / 1 | 0 / 0 |
| external_actions_taken | 0 | 0 |

## V4 graduation criteria

- Citation audit PASS: **yes**.
- Every decision claim at 0.92 floor or explicitly in residue: **yes** (1/1 at floor).
- No unaddressed FATAL red-team objection: **yes** (0 FATAL).

Verdict: **GRADUATES for internal R1 use, pending PR merge and Ankit residue signature**.

## Research result from V4

The measured effect should be stated as an **observational association, not a universal causal effect**. The cleanest direct private-practice source in this run reported **2.1% missed online appointments vs 7.6% traditional/offline appointments** in Clinic A, with similar significant findings across four other practices. However, the implementation bundled online booking with automated reminders, and broader web-appointment evidence is heterogeneous enough that a pooled causal no-show reduction is not defensible.

Recommended wording: **online self-scheduling is often associated with lower observed no-show rates, but the standalone causal effect is unresolved; quote local pilots separately from reminders, lead time, and patient-selection effects.**

## Artifacts

- V3 report: `Version4/deploy/benchmark-2026-06-09/v3/report/report.md`
- V3 post-hoc citation audit: `Version4/deploy/benchmark-2026-06-09/v3/qa/citation_audit.md`
- V3 run card: `Version4/deploy/benchmark-2026-06-09/v3/run_card.md`
- V4 report: `Version4/deploy/benchmark-2026-06-09/v4/report/report.md`
- V4 evidence ledger: `Version4/deploy/benchmark-2026-06-09/v4/04_evidence_ledger.csv`
- V4 citation audit: `Version4/deploy/benchmark-2026-06-09/v4/qa/citation_audit.md`
- V4 stop rule output: `Version4/deploy/benchmark-2026-06-09/v4/qa/stop_rule.out`
- V4 run card: `Version4/deploy/benchmark-2026-06-09/v4/run_card.md`

## Red-team residue

- MATERIAL in V3: secondary-review claims were treated as if primary without fetching every cited primary; post-hoc audit also caught a ghost reference (`E099`).
- V4 residue: no randomized trial isolating self-scheduling alone was verified; do not claim causality.
- Surface limitation: cost telemetry and exact wall-clock instrumentation were unavailable in this Telegram/Hermes run and are marked unavailable instead of estimated.
