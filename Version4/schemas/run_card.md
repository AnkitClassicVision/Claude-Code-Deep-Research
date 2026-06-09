# Schema: run_card.md (one per research run)

OBSERVED in practice: the per-run telemetry record. Read this, not vibes, to judge a run.

## Identity
- run_id, date, question (one line), tier, domain overlay (if any)

## Models
- controller/synthesis, scouts, extractor, verifier (MUST differ from synthesis), red team
- Any model or prompt change since last run? (triggers benchmark comparison)

## Budgets vs actuals
- N_search, N_fetch, deep-read docs, checkpoints run, est. tokens, est. cost

## Convergence path
- Verdict sequence (e.g. CONTINUE x3, SHIFT_VERIFY, STOP_SUFFICIENT)
- Final verdict and why (one line)

## Branch stats
- Branches launched / merged for overlap / pruned
- Max pairwise source overlap (gate: under 30%)
- % of fetch budget spent on branches that did not survive (exploration spend; healthy is not 0)

## Gate outcomes
- Citation audit: PASS/FAIL, failures count, live fetch on/off
- Numeric audit: PASS/FAIL
- Trace check: PASS/FAIL
- Red team: FATAL / MATERIAL / MINOR counts

## Ledger stats
- Claims by tier; % verified; rejected count; [Unverified] parked count

## Refusals
- Hard-refuse events (logged separately) and graceful refusals, with reason classes

## Residue
- Signed: yes/no, accepter name
