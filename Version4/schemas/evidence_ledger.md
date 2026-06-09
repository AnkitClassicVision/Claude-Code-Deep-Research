# Schema: 04_evidence_ledger.csv

The load-bearing artifact. Nothing reaches the report except through a row here.

| Column | Type | Rule |
|---|---|---|
| claim_id | E### | Unique, sequential, never reused |
| claim_text | text | One claim. Split compounds |
| tier | context / finding / decision | From contract subquestion mapping; extractor assigns LOW, verifier promotes |
| subquestion | SQ# | Links to research contract |
| quote | text | Verbatim, under 40 words, supports the claim alone |
| url | url | Required for any factual row |
| source_quality | A-E or I | I = internal-canonical (own-operation questions only) |
| independence_group | G## (semicolon-sep if multiple) | Sources tracing to one origin share a group. Corroboration counts GROUPS |
| confidence | 0.00-1.00 | Calibrated estimate the claim as written is true |
| status | unverified / verified / rejected / needs_source | Only the verifier sets verified |
| branch | B# | Which branch produced it |
| date_captured | YYYY-MM-DD | |
| notes | text | Optional |

Floors: context 0.60 / finding 0.80 / decision 0.92.
Corroboration: context 1 source; finding 2 groups OR 1 primary (A); decision independence rule + live re-fetch + verifier sign-off + zero open contradictions.
