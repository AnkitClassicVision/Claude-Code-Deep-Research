# Schema: residue_statement.md (one per research run, signed)

What this pipeline CANNOT gate against for this run. A report without a signed
residue statement is not done. Signing means the accepter owns these risks.

For each residue item:

| Field | Rule |
|---|---|
| risk | Named failure the gates cannot catch |
| probability | Estimated occurrences per 1,000 comparable runs |
| magnitude | What it costs if it happens (decision led astray, $ band, rework) |
| detection | How it would eventually surface, if at all |
| escalation_trigger | Observable event that forces a re-run or human review |

## Standing residue classes (start here, add run-specific items)
1. Coordinated-wrong sources: independence groups verified, but the whole field can repeat one bad origin
2. Paywalled or offline primaries: cited via secondaries, quote not live-verifiable
3. Recency gap: world changed after capture date
4. Correlated model error: drafter and verifier differ, but share training-data blind spots
5. Scope exclusions: contract out-of-scope list means real factors were never searched
6. Unmet floors accepted at STOP_SATURATED: list the specific claims

## Signature
- Accepter (named human): ____________
- Date: ____________
- Status: ACCEPTED / BLOCKED (blocked = report not releasable for decisions)
