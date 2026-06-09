# HERMES DEPLOYMENT PACKAGE: Deep Research V4

Deploy owner: Hermes
Mode: AAC v2.0 creation-gate deployment. Read-only research capability; no client-facing actions in scope.
Idempotency rule: every step checks current state before acting. Re-running this package must never duplicate work.
PILOT mapping: this deploy is R0 to R1 (sandbox benchmark, then Ankit's own use). Go-Live Gate (R3 to R4) is out of scope; nothing here touches client workflows. The human gate for THIS deploy is the PR merge plus residue signature.

---

## 0. Lanes (verdict frame)

ALLOWED lane:
- Repo: branch, additive commit of Version4/, PR. No force push. No edits to Version3/ or existing files except the one root README snippet in Step 2.
- Surfaces: install skill/agent/config files per Step 4.
- OB_mybcat: captures per Step 5, idempotent.
- One benchmark run (Step 3): web search and fetch only. external_actions_taken must equal 0.

BLOCKED lane (hard):
- Any production send/write/draft toward clients, HubSpot, Gmail, calendars, or EHRs.
- Modifications to AAC, PILOT, THROUGHLINE, Alignment Protocol, or any other canonical framework.
- Model pin changes beyond what models.config.md ships with.
- Deleting or rewriting V3. V4 is additive; public consumers on V3 stay unaffected.

If any step requires leaving the allowed lane: STOP, write the blocker to the deploy report, do not improvise.

---

## 1. Preconditions (gate, all must pass)

- [ ] Package contents match the manifest below (17 files + this deploy folder)
- [ ] python3 available on host
- [ ] Git access to AnkitClassicVision/Claude-Code-Deep-Research
- [ ] OB_mybcat MCP reachable (run one test search)
- [ ] Both gate scripts pass self-test (commands in Step 2.4)

Any failure: stop, report, zero partial deployment.

Manifest: CLAUDE.md, README.md, models.config.md, agents/{scout,extractor,verifier,resolver,red-team,editor}.md, scripts/{stop_rule.py,citation_audit.py}, schemas/{evidence_ledger,convergence_log,run_card,residue_statement}.md, prompts/question-refiner-v2.md, skills/deep-research/SKILL.md, deploy/HERMES-DEPLOY.md.

---

## 2. Step R0: Repo (system of record first)

2.1 `git checkout -b feat/version4` from latest main.
2.2 Unzip Version4/ at repo root. Verify no existing file outside Version4/ was modified: `git status` must show only additions plus the README edit below.
2.3 Root README.md: add this section verbatim under the UPDATE line:

```
## Version 4.0 (June 2026)
V4 replaces thinking scaffolds with verification scaffolds: deterministic stop rules
and citation gates (scripts), cross-model verification, consequence-tier confidence
floors, run cards, and signed residue statements. See `Version4/README.md`.
V3 remains unchanged below for existing users.
```

2.4 Script self-test (must both behave as stated):
- `python3 Version4/scripts/stop_rule.py --log <synthetic log>` returns correct verdicts for: sufficient (exit 1, STOP_SUFFICIENT), low-yield explore (exit 0, SHIFT_VERIFY), oscillation (exit 2, ESCALATE_STUCK).
- `python3 Version4/scripts/citation_audit.py` FAILs on a ledger with a ghost reference and PASSes when resolved.

2.5 Commit message: `Add Version 4.0: gate-driven research (deterministic stop rules, citation gates, cross-model verification, AAC v2.0 alignment)`. Push, open PR. **Do not merge. Ankit merges. This is a human gate.**

---

## 3. Step R1: Benchmark (graduation condition)

Fixed benchmark question (do not substitute; reproducibility requires a constant):

> "What is the measured effect of patient self-scheduling on no-show rates in outpatient medical practices?"

Chosen because: decision-relevant, numerically contested, and polluted with vendor-inflated secondary sources, which stress-tests independence grouping and citation laundering exactly where V3 was weakest.

3.1 Run under V3 (as published, untouched) with N_fetch=30.
3.2 Run under V4, same budgets, Standard tier, citation audit with `--fetch` where network allows.
3.3 Produce comparison table in `deploy/BENCHMARK-[date].md`: cost per VERIFIED claim, citation-audit pass rate, decision-claim gate coverage, wall-clock, % budget on losing branches, FATAL/MATERIAL red-team counts.
3.4 Graduation criteria (all three): V4 citation audit PASS; every decision claim at 0.92 floor or explicitly in residue; no unaddressed FATAL red-team objection.
3.5 external_actions_taken=0 confirmed in both run cards.

---

## 4. Step R2: Surface installs (five parallel targets, no ranking)

| Surface | Install | Verify |
|---|---|---|
| Hermes | Register skills/deep-research per Hermes skill convention; add Surface Rule Registry entry: "deep-research current = V4, canonical pointer in OB_mybcat, fetch at runtime" | Dry-run Phase 0 on a toy question; confirm registry entry resolves |
| Claude Code | CLAUDE.md to project root (research projects), agents/*.md to .claude/agents/, skill to ~/.claude/skills/deep-research/ | `/agents` lists all six research-* agents; skill triggers on "deep research X" |
| Codex | Skill files into repo; AGENTS.md pointer: "For deep research tasks read Version4/skills/deep-research/SKILL.md and follow CLAUDE.md; run agents sequentially in isolated contexts" | Invoke on toy question; confirm it reads SKILL.md first |
| Gemini | Same files; GEMINI.md pointer with identical text | Same toy-question check |
| Claude.ai | Upload skill folder (SKILL.md + CLAUDE.md + schemas + scripts) via Skills; scripts run in its code environment | Trigger phrase test; confirm stop_rule.py executes in-session |

Documented exceptions (required by the surface-interchangeability rule, these are constraints, not rankings):
1. Native parallel subagents exist on Claude Code and Hermes only. Codex, Gemini, and Claude.ai run agents sequentially in isolated contexts per SKILL.md degraded mode.
2. Surfaces without code execution fall back to manual checklist gates, recorded as `gates_mode=manual` in the run card.

Any surface that cannot be verified today: log it as PENDING with reason in the deploy report. Do not silently skip.

---

## 5. Step R3: OB_mybcat captures (pointer-to-brain, idempotent)

5.1 WIP capture. SEARCH FIRST for topics `deep-research-v4, wip`. A capture dated 2026-06-09 from Claude.ai likely exists. If present: verify text matches intent below, do not duplicate. If absent, capture:
- type: idea; topics: deep-research-v4, wip, active, claude-code, benchmark, aac
- text: "Deep Research V4 built 2026-06-09: verification scaffolds replace V3 thinking scaffolds. Deterministic stop_rule.py + citation_audit.py gates, cross-model verifier, consequence-tier floors 0.60/0.80/0.92, run cards, signed residue. Graduation condition: one benchmark run vs V3 (fixed no-show question) with clean citation audit, all decision claims at floor or in residue, no unaddressed FATAL red-team objection. Repo: Claude-Code-Deep-Research/Version4."

5.2 Pointer capture (reference type): "Deep Research current version = V4. Surfaces fetch this pointer at runtime per Pointer-to-Brain Pattern v1. V3 remains published for external users; internal default is V4. Owner: Hermes (rule propagation), Ankit (framework)."

5.3 Post-benchmark: if graduation criteria met, promote WIP to Decision capture (V4 canonical for internal research) and note the run card location. If not met, append failure observation to the WIP, leave it WIP, surface to Ankit.

---

## 6. Acceptance checklist (deployment is done when ALL boxes tick)

- [ ] PR merged by Ankit (human gate 1)
- [ ] Benchmark comparison file committed, graduation verdict recorded
- [ ] 5/5 surfaces verified, or PENDING entries with reasons
- [ ] OB captures present, no duplicates
- [ ] Deploy run card written (template in 8)
- [ ] Deploy residue signed by Ankit (human gate 2)

## 7. Rollback

Revert the PR (single revert commit; V3 untouched throughout so external users never notice). Remove surface installs in reverse order. OB captures: mark superseded with reason; never delete.

## 8. Deploy run card (Hermes fills)

run_id, date, steps executed, preconditions outcome, PR url + merge status, benchmark verdict + metrics table link, surfaces (verified/pending per surface), OB capture ids, refusals or lane-stop events, total cost est, external_actions_taken (must be 0).

## 9. Deploy residue (pre-filled, Ankit signs)

| Risk | Probability /1000 deploys | Magnitude | Escalation trigger |
|---|---|---|---|
| Benchmark question idiosyncrasy: V4 wins on this question, not generally | 150 | Wrong confidence in V4; rerun cost | Second benchmark question disagrees with first |
| Surface drift: five installs diverge over time | 300 | Inconsistent research quality by surface | Any surface run card missing fields others have |
| Sequential-mode surfaces lose branch independence quality | 200 | Weaker exploration on Codex/Gemini/Claude.ai | Overlap >30% recurring on sequential surfaces |
| Correlated blind spot: drafter and verifier share training gaps | 50 | Verified-but-wrong decision claim | Post-hoc contradiction found by human reader |
| Public repo consumers misapply V4 without AAC context | open | Reputation only; no MyBCAT exposure | Issues filed on repo |

Accepter: Ankit ____________  Date: ________  Status: ACCEPTED / BLOCKED
