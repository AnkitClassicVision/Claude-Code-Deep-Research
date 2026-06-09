# Deep Research Implementation - Version 4.0

## The one-line change

V3 scaffolded the model's THINKING (Graph-of-Thoughts controller, node scores,
transformation states) because 2025 models needed it. 2026 frontier models plan
natively; what they still cannot be trusted with is grading their own work. V4
deletes the thinking choreography and hardens VERIFICATION into deterministic,
script-enforced gates.

Governance: the pipeline maps to AAC v2.0 (BOUNDED / GROUNDED / GATED / OBSERVED /
GOVERNED). Certify the pipeline once at design time; each run emits a run card.

## What changed V3 -> V4

| V3 | V4 | Why |
|---|---|---|
| ChatGPT o3 question refiner (separate tool) | Phase 1 in-session interview (`prompts/question-refiner-v2.md` optional standalone) | o3 retired; the hop lost context |
| GoT graph_state.json as control structure | Branch quotas + disjointness gate (max 30% source overlap) + `branch_manifest.md`; `graph_trace.md` is a log only | Independence enforced by architecture (parallel subagents), not simulated in one context |
| Inline agent prompt templates in one 1,100-line file | Real subagents in `agents/` (Claude Code `.claude/agents/` format), thin ~330-line CLAUDE.md | Installable, versionable, model-pinned per role |
| Fixed agent counts per tier | Model routing per role (`models.config.md`); tiers set branch minimums | Haiku swarm for grunt work, frontier for judgment, DIFFERENT model for verification |
| Termination: "any 2 of 4 conditions", model-judged | `scripts/stop_rule.py`: deterministic verdicts (CONTINUE_EXPLORE / SHIFT_VERIFY / STOP_SUFFICIENT / STOP_SATURATED / STOP_BUDGET / ESCALATE_STUCK) from `convergence_log.csv` | The model never grades its own sufficiency |
| HIGH/MED/LOW confidence labels | Consequence tiers with enforced floors: context 0.60 / finding 0.80 / decision 0.92 | Labels became gates |
| Citation audit as optional tooling | `scripts/citation_audit.py` as a blocking gate (exit code), optional live quote re-fetch | Hallucinated citations are the failure mode that matters |
| QA = model self-review | Cross-model verifier + red team + script gates + signed residue statement | Uncorrelated checks |
| (none) | Internal-first check in Phase 0 | Do not re-research what your knowledge base already decided |
| (none) | `run_card.md` per run | Telemetry you can compare across runs and model generations |

Kept from V3 (it was right): evidence ledger as the load-bearing artifact,
contradiction triage, independence grouping (anti citation-laundering), red team,
budgets, prompt-injection firewall, domain overlays (now hard-refuse-FIRST;
reuse `../Version3/DOMAIN_OVERLAYS/`).

## Quick start (Claude Code)

1. Copy `CLAUDE.md` to your project root
2. Copy `agents/*.md` into `.claude/agents/`
3. Confirm `python3` is available; keep `scripts/` and `schemas/` in the project
4. Set the main model (Fable/Opus class) via `/model`
5. Say: `Deep research [your topic]`

Phase 1 will interview you for the contract. Do not skip consequence-tier tagging;
sufficiency is defined there or nowhere.

## Folder structure

```
Version4/
├── README.md
├── CLAUDE.md                  # Control logic only (~330 lines)
├── models.config.md           # Single update point for model pins
├── agents/                    # scout, extractor, verifier, resolver, red-team, editor
├── scripts/                   # stop_rule.py, citation_audit.py (the D-runtime gates)
├── schemas/                   # evidence_ledger, convergence_log, run_card, residue_statement
├── prompts/                   # question-refiner-v2 (optional standalone)
└── skills/deep-research/      # SKILL.md wrapper for cross-surface install
```

## Benchmark protocol (champion-challenger)

Settle V3 vs V4 (and every future change) with runs, not opinions:

1. Pick one fixed benchmark question (Type C/D, known to have conflicting sources)
2. Run it under V3 and under V4 with equal fetch budgets
3. Compare: cost per VERIFIED claim, citation-audit pass rate, decision-claim gate
   coverage, wall-clock time, % budget on losing branches (exploration spend)
4. Rerun the same question after ANY change to thresholds.json, agent files, or
   model pins; diff the run cards

## Version history

- V1.0 initial; V2.0 GoT + agent templates; V3.0 hypothesis formation, ledger,
  red team, overlays (Dec 2025)
- **V4.0 (June 2026): verification scaffolds replace thinking scaffolds;
  deterministic gates; cross-model verification; convergence state machine;
  run cards + residue statements; AAC v2.0 alignment**
