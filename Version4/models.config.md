# Models Config (single update point)

GOVERNED rule: model assignments live HERE and in agent frontmatter, nowhere else.
When a new model generation ships: update this file, update the `model:` field in
`agents/*.md` if aliases shifted, rerun the benchmark question, compare run cards.
Do not adopt a new model without the benchmark comparison.

## Current pins (June 2026)

| Role | Recommended | Frontmatter value | Notes |
|---|---|---|---|
| Controller / synthesis / red team | Claude Fable 5 (fallback: Opus 4.8, `claude-opus-4-8`) | main thread: set via `/model`; red-team agent: `inherit` | Judgment work gets the frontier model |
| Verifier | Sonnet 4.6 (`claude-sonnet-4-6`) | `sonnet` | MUST differ from the synthesis model. Optional: route through an external model (Gemini/Codex CLI) for fully uncorrelated verification |
| Scouts / extractor | Haiku 4.5 (`claude-haiku-4-5-20251001`) | `haiku` | Parallel, cheap, explicit prompts |

Frontmatter `model:` accepts an alias (`haiku` / `sonnet` / `opus`), a full model ID, or `inherit`. See Claude Code docs (sub-agents page) for current fields and any environment-level overrides before changing behavior in production.

## Prompt-style rule per tier

- Frontier (controller, red team): goals and gates. No step choreography; it fights the model.
- Mid (verifier, editor): goals, gates, plus explicit output contracts.
- Small (scouts, extractor): explicit step contracts, exact output formats, hard budgets. Small models earn their cost only when the contract leaves nothing to interpret.

## Cross-model verification rationale

Two instances of the same model share blind spots; their agreement is weak evidence.
A different model re-fetching the primary source is the cheapest uncorrelated check
available. If only one model family is available, the verifier must rely on live
re-fetch of primary sources, never on re-reading agent notes.
