# Claude Deep Research Agent
See example outputs here: https://claude-code-deep-research.vercel.app/

## Table of Contents

1. [Why This Exists](#why-this-exists)
2. [Repo Structure](#repo-structure)
3. [Version 4.0](#version-40-june-2026)
4. [Quick Start](#quick-start)
5. [How It Works](#how-it-works)
6. [Customization](#customization)
7. [Credits & Acknowledgements](#credits--acknowledgements)
8. [License](#license)

---

UPDATE: Added `Claude2.md` — updated for deeper research and closer Graph-of-Thought patterns.

## Version 4.0 (June 2026)
V4 replaces thinking scaffolds with verification scaffolds: deterministic stop rules
and citation gates (scripts), cross-model verification, consequence-tier confidence
floors, run cards, and signed residue statements. See `Version4/README.md`.
V3 remains unchanged below for existing users.

**Recommended default for new research:** start with V4. Use V3 only when you need
the original public Graph-of-Thoughts workflow or are comparing V3 against V4.

## Why This Exists

Large Language Models (LLMs) excel at single queries but struggle with complex, multi-step research requiring iterative querying, source verification, and citations—what OpenAI and Google call "Deep Research." Anthropic’s Claude Code can achieve the same results, provided the right instructions. This repo supplies those instructions, streamlined into an easy-to-use workflow.

## Repo Structure

| File/Folder                                           | Purpose                                                                                                       |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **CLAUDE.md**                                         | Master instructions for Claude Code. Includes Graph-of-Thoughts integration and deep-research methodology.    |
| **Deep Research Question Generator System Prompt.md** | ChatGPT system prompt (o3/o3-pro) refining raw questions into structured prompts (OpenAI format recommended). |
| **deepresearchprocess.md**                            | Comprehensive 7-phase deep research playbook inspired by OpenAI & Google Gemini, foundational to `CLAUDE.md`. |
| **.template\_mcp.json**                               | Optional MCP server configuration for local filesystem and browser automation with Claude.                    |
| `examples/`                                           | Sample refined questions and completed Claude reports compared to other outputs.                              |
| `Version4/`                                           | Current verification-gated workflow: control file, installable agents, scripts, schemas, prompt refiner, skill wrapper, benchmark artifacts, and deployment reports. |
| `AGENTS.md` / `GEMINI.md`                             | Pointers for Codex/Gemini-style surfaces to read `Version4/skills/deep-research/SKILL.md` and follow the V4 control logic. |

## Quick Start

### Recommended: Version 4.0 verification-gated workflow

1. Read `Version4/README.md` for the V3 → V4 changes.
2. Use `Version4/CLAUDE.md` as the controller and `Version4/agents/*.md` for the six research roles.
3. Keep `Version4/scripts/` and `Version4/schemas/` with the run so `stop_rule.py`, `citation_audit.py`, run cards, ledgers, and residue statements are available.
4. Start with: `Deep research [your question]`.
5. Before finalizing, run the deterministic gates and record any unresolved claims in the residue statement.

### Legacy V3 workflow

Example output and comparisons from the examples folder: https://claude-code-deep-research.vercel.app/

### Step 1: Refine Your Question with ChatGPT (or your favorite LLM)

1. Open ChatGPT (model o3/o3-pro or other thinking models work best).
2. Set the **system prompt** to the contents of `Deep Research Question Generator System Prompt.md`.
3. Paste your raw research question into the **user prompt**.
4. Respond to any clarifying questions from ChatGPT.
5. Copy the generated **OpenAI-formatted** prompt.

### Step 2: Prepare Claude Code

1. Launch a new Claude Code session.
2. Set the model using `/model opus`.
3. Type:

   ```
   Please read the CLAUDE.md file and confirm when ready for my deep research question.
   ```
4. Wait for Claude’s confirmation.

### Step 3: Launch Deep Research

1. Paste your refined question.

2. Claude autonomously performs:

   * Research planning with Graph-of-Thoughts.
   * Spins up multiple subagents to do the work faster
   * Iterative search and data scraping.
   * Fact verification and cross-referencing.
   * Markdown report generation with citations and bibliography.

3. Review and refine as needed.

> **Tip ⚡:** Include directory instructions, such as:
>
> "Save all outputs in the `/RESEARCH/[topic]` folder."

### Bonus Step (Optional)

After obtaining the report, instruct Claude to convert it into a user-friendly website format for enhanced accessibility and readability.

## How It Works

### Workflow Overview

```
[ Question Refinement ] → [ Claude Code / agent surface ] → [ V4 verification-gated research pipeline ] → [ Cited Markdown Report + Evidence Ledger + Run Card + Residue ]
```

* **Version4:** Current workflow. It uses branch quotas, disjointness checks, deterministic stop rules, citation audits, cross-model verification, consequence-tier confidence floors, run cards, and signed residue statements.
* **DeepResearchProcess:** Implements a 7-phase pipeline—Scope → Plan → Retrieve → Triangulate → Draft → Critique → Package.
* **Graph-of-Thoughts:** Allows Claude to branch and merge multiple reasoning paths rather than relying on linear chains.
* **CLAUDE.md:** Integrates instructions, enabling Claude to autonomously select tools, verify information, and embed citations systematically.

### Build Notes

* **Research Methodology:** Derived from OpenAI and Gemini’s deep-research playbooks.
* **Graph-of-Thoughts Integration:** Adapted from [Graph-of-Thoughts](https://github.com/spcl/graph-of-thoughts) to support dynamic research pathways.
* **Prompt Generation:** ChatGPT-based structured prompt ensures clarity, reducing confusion during Claude’s research by over 50% in tests.
* **Automation Hooks:** The `.template_mcp.json` demonstrates local automation options via MCP servers, enabling advanced Claude operations.

## Customization

* **Output Styles:** Adjust formatting and citation preferences directly within the `CLAUDE.md` file.
* **Model Flexibility:** Alternative Gemini-specific prompts provided by the ChatGPT system prompt generator if preferred.
* **Tool Integration:** Expand automation via MCP by updating `.template_mcp.json` and referencing additional tools within `CLAUDE.md`.


## Credits & Acknowledgements

* **Graph-of-Thoughts Framework:** [SPCL, ETH Zürich](https://github.com/spcl/graph-of-thoughts) (MIT License).
* Methodologies inspired by publicly available OpenAI and Google Gemini documentation.
* Developed by Ankit at [My Business Care Team (MyBCAT)](https://mybcat.com).

## License

MIT License. See `LICENSE` file for full details.
