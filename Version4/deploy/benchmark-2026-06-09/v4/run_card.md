# V4 benchmark run card

- run_id: deep-research-v4-benchmark-2026-06-09
- date: 2026-06-09
- question: What is the measured effect of patient self-scheduling on no-show rates in outpatient medical practices?
- tier: Standard
- budgets: N_fetch=30, N_search=30
- actual fetches logged: 12 source fetches + live citation re-fetches
- external_actions_taken: 0
- verified_claims: 8
- decision_claims_total: 1
- decision_claims_at_floor: 1
- citation_audit: PASS with --fetch, exit 0
- stop_rule: exit 1; see qa/stop_rule.out
- red_team: FATAL=0, MATERIAL=0, MINOR=2
- losing_branch_budget: 33% (confounder branch used to bound, not answer primary effect)
- cost_estimate: not exposed by this Telegram/Hermes surface; token/cost field recorded as unavailable rather than fabricated
- gates_mode: script
- residue_signed: no; Ankit human gate pending
