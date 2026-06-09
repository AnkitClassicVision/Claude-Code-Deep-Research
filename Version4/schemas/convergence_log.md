# Schema: convergence_log.csv

One row per checkpoint. Consumed by scripts/stop_rule.py. The controller reports; the script decides.

| Column | Type | Meaning |
|---|---|---|
| checkpoint_id | int | Sequential |
| timestamp | ISO 8601 | |
| fetches_total | int | Cumulative |
| fetches_window | int | Since last checkpoint |
| new_claims_window | int | Net-new ledger rows this window |
| new_claim_rate | 0-1 | new_claims_window / fetches_window |
| new_source_rate | 0-1 | Share of window sources not already in catalog |
| decision_claims_total | int | All decision-tier rows |
| decision_claims_at_floor | int | Decision rows meeting full floor requirements |
| gate_coverage_pct | 0-1 | at_floor / total (0 if total is 0) |
| open_decision_contradictions | int | UNRESOLVED conflicts touching decision claims |
| answer_flips_window | int | Decision claims added, removed, or reversed in answer_snapshot.md since last checkpoint |
| verdict | text | What stop_rule.py returned |
| notes | text | Optional |

Companion file thresholds.json (version-controlled; changing it = champion-challenger rerun):
{ "yield_floor": 0.10, "novelty_floor": 0.20, "window_checkpoints": 2, "flip_alert": 2, "gate_coverage_target": 1.0 }
