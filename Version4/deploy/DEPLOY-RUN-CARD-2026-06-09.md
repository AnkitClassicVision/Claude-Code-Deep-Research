# Deploy run card — Deep Research V4 — 2026-06-09

## Identity

- run_id: `deep-research-v4-hermes-deploy-2026-06-09`
- deploy owner: Hermes
- mode: AAC v2.0 creation-gate deployment
- PILOT mapping: R0 to R1 only; R3/R4 go-live out of scope
- repo: `AnkitClassicVision/Claude-Code-Deep-Research`
- branch: `feat/version4`
- PR: https://github.com/AnkitClassicVision/Claude-Code-Deep-Research/pull/2
- merge status: OPEN / pending Ankit human gate
- external_actions_taken: 0

## Steps executed

1. Preflighted package manifest from uploaded zip.
2. Verified host prerequisites: `python3`, `git`, `gh`, GitHub access, and OB_mybcat search.
3. Created branch `feat/version4` from latest `origin/main`.
4. Extracted `Version4/` additively at repo root.
5. Added the required root `README.md` Version 4.0 snippet under the existing UPDATE line.
6. Ran deterministic gate-script self-tests.
7. Committed and pushed initial V4 package commit.
8. Opened PR #2 without merging.
9. Ran V3/V4 benchmark on the fixed patient self-scheduling/no-show question.
10. Added benchmark artifacts and run cards under `Version4/deploy/`.
11. Installed/attempted the five requested surfaces and documented verified/pending states.
12. Searched OB_mybcat first, then created the missing V4 pointer and post-benchmark decision captures.

## Preconditions outcome

- Package contents: PASS. Zip contained 18 files = 17 package files plus `deploy/HERMES-DEPLOY.md`.
- `python3`: PASS (`python3 --version` succeeded).
- GitHub access: PASS (`gh auth status`; repo view succeeded).
- OB_mybcat MCP reachable: PASS (test search returned existing Deep Research V4 WIP capture).
- Gate scripts self-test: PASS.
  - `stop_rule.py`: sufficient -> exit 1 `STOP_SUFFICIENT`; low-yield explore -> exit 0 `SHIFT_VERIFY`; oscillation -> exit 2 `ESCALATE_STUCK`.
  - `citation_audit.py`: ghost reference -> FAIL exit 1; resolved reference -> PASS exit 0.

## Repo / PR

- PR URL: https://github.com/AnkitClassicVision/Claude-Code-Deep-Research/pull/2
- Merge status: not merged by Hermes; Ankit human gate pending.
- Main branch untouched by Hermes.
- `Version3/` untouched.
- Root README changed only for required V4 snippet.
- Additional surface pointer files added: `AGENTS.md`, `GEMINI.md`.
- Package fix made before final push: `Version4/skills/deep-research/SKILL.md` frontmatter changed from a single-line YAML description to a block scalar so Hermes skill registration can parse it.

## Benchmark verdict

- Benchmark file: `Version4/deploy/BENCHMARK-2026-06-09.md`
- V4 run card: `Version4/deploy/benchmark-2026-06-09/v4/run_card.md`
- V4 citation audit: PASS with `--fetch`.
- Decision-claim coverage: 1/1 at or above 0.92 floor.
- Red-team FATAL: 0.
- Graduation verdict: V4 graduates for internal R1 use, pending PR merge and residue signature.
- Research conclusion: self-scheduling should be described as an observational association, not a universal causal no-show reduction; cleanest direct source found was 2.1% online missed appointments vs 7.6% traditional/offline in one clinic, with causality residue for reminders, lead time, and patient selection.

## Surfaces

See `Version4/deploy/SURFACE-VERIFY-2026-06-09.md`.

- Hermes: VERIFIED.
- Claude Code: INSTALLED; runtime slash-command verification PENDING because `/agents` was not available in headless print mode and interactive PTY hit first-run UI.
- Codex: INSTALLED; runtime verification PENDING due `codex exec` OpenAI API 401/missing auth header.
- Gemini: INSTALLED; runtime verification PENDING due missing Gemini auth method in this Hermes profile.
- Claude.ai: PENDING; requires interactive Skills UI upload/account authorization.

## OB_mybcat captures

Search-first/idempotency results:

- Existing WIP found: Deep Research V4 WIP capture dated 2026-06-09 was present and not duplicated.
- Pointer capture created: `Deep Research current version = V4. Surfaces fetch this pointer at runtime...`
- Decision capture created: `DECISION 2026-06-09: Deep Research V4 graduates from WIP to canonical internal research default...`

The MCP tool returned capture confirmations but not raw IDs. Verification search returned both new captures.

## Refusals / lane stops / pending gates

- No blocked-lane actions were taken.
- No client-facing sends/writes/drafts, HubSpot, Gmail, calendar, or EHR actions were taken.
- No AAC/PILOT/THROUGHLINE/Alignment Protocol canonical framework modifications were made.
- No model-pin changes beyond the shipped `models.config.md` were made.
- PR merge remains pending Ankit.
- Deploy residue signature remains pending Ankit.
- Claude.ai upload and Codex/Gemini runtime verifications remain pending for auth/UI reasons.

## Total cost estimate

- Exact cost telemetry was unavailable in this Telegram/Hermes surface and is intentionally not fabricated.
- Benchmark artifact records this as unavailable; token/cost observability should be added to the next benchmark harness if cost per verified claim is required as a hard metric.

## Acceptance checklist status

- [ ] PR merged by Ankit — pending.
- [x] Benchmark comparison file committed/staged for PR branch, graduation verdict recorded.
- [ ] 5/5 surfaces verified — not complete; pending entries documented with reasons.
- [x] OB captures present, no duplicate WIP.
- [x] Deploy run card written.
- [ ] Deploy residue signed by Ankit — pending.
