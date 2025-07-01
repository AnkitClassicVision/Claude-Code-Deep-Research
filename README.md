# Claude Deep Research Agent
See example outputs here: https://claude-code-deep-research.vercel.app/

## Table of Contents

1. [Why This Exists](#why-this-exists)
2. [Repo Structure](#repo-structure)
3. [Quick Start](#quick-start)
4. [How It Works](#how-it-works)
5. [Customization](#customization)
6. [Roadmap](#roadmap)
7. [Credits & Acknowledgements](#credits--acknowledgements)
8. [License](#license)

---

UPDATE: Added Calude2.md - updated for deeper reserach and more closley mimics graph of thought patterns.
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

## Quick Start

##Example output and comparisons (from examples folder): https://claude-code-deep-research.vercel.app/

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
   * Spins up mulple subagents to do the work faster
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
[ ChatGPT (o3) ] → Question Refinement → [ Claude Code (opus) ] → Graph-of-Thoughts & Deep Research Pipeline → [ Cited Markdown Report ]
```

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
