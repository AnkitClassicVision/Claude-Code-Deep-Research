# Surface verification — 2026-06-09

## Summary

Surface rule: `deep-research current = V4, canonical pointer in OB_mybcat, fetch at runtime`.

## Hermes

Status: VERIFIED.

Evidence:
- Hermes skill `deep-research` created in profile `full-access-worker-a` under `skills/research/deep-research/SKILL.md`.
- `skill_view(name="deep-research")` resolves.
- Support files copied into the skill folder: `CLAUDE.md`, `README.md`, `models.config.md`, `agents/`, `scripts/`, `schemas/`, `prompts/`.
- Registry fallback file resolves at `references/surface-rule-registry.md` with the required pointer text.
- Script dry-run using installed skill path returned `STOP_SUFFICIENT` with exit code 1 on the benchmark convergence log.
- Toy Phase 0 dry-run: question `Deep research whether a paperclip is metal` -> hard-refuse: none; internal-first: skipped/no internal source needed; complexity: Type A single lookup, so no full pipeline/web spend.

## Claude Code

Status: INSTALLED, RUNTIME VERIFICATION PENDING.

Evidence:
- Installed `Version4/agents/*.md` into `/home/ankit114/.claude/agents/`.
- Installed full skill folder into `/home/ankit114/.claude/skills/deep-research/`.
- Installed six agent frontmatter names verified from files: `research-scout`, `research-extractor`, `research-verifier`, `research-resolver`, `research-red-team`, `research-editor`.
- `stop_rule.py` executed from the installed Claude skill path and returned `STOP_SUFFICIENT` with exit code 1.

Pending reason:
- `/agents` runtime listing could not be verified headlessly. `claude -p "/agents"` returned `/agents isn't available in this environment`; an interactive PTY attempt hit first-run theme/onboarding UI before accepting slash commands.

## Codex

Status: INSTALLED, RUNTIME VERIFICATION PENDING.

Evidence:
- Added repo-level `AGENTS.md` pointer: `For deep research tasks read Version4/skills/deep-research/SKILL.md and follow Version4/CLAUDE.md; run agents sequentially in isolated contexts when native parallel subagents are unavailable.`
- V4 skill files are present in-repo under `Version4/skills/deep-research/` and supporting files under `Version4/`.

Pending reason:
- `codex exec` runtime verification failed before model execution with OpenAI API `401 Unauthorized` / missing auth header. No files were modified by the verification attempt.

## Gemini

Status: INSTALLED, RUNTIME VERIFICATION PENDING.

Evidence:
- Added repo-level `GEMINI.md` pointer with the same V4 read-first/sequential-mode instruction.
- V4 skill files are present in-repo under `Version4/skills/deep-research/` and supporting files under `Version4/`.

Pending reason:
- `gemini --prompt` runtime verification failed before model execution because no Gemini auth method was configured in this Hermes profile (`GEMINI_API_KEY`, Vertex, or GCA not available).

## Claude.ai

Status: PENDING.

Pending reason:
- Claude.ai Skills upload requires interactive browser/UI access and account/session authorization not available in this headless Hermes run. Required upload package is present in `Version4/` and the installed Claude Code skill folder.

## Documented surface exceptions

- Native parallel subagents are available on Claude Code and Hermes only.
- Codex, Gemini, and Claude.ai should run agents sequentially in isolated contexts per `SKILL.md` degraded mode.
- Surfaces without code execution must use manual checklist gates and record `gates_mode=manual` in the run card.
