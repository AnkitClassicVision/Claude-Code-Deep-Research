# Deep Research Implementation with Graph of Thoughts

## Overview
This is a complete, self-contained implementation of Graph of Thoughts (GoT) for deep research. No external files or setup required - everything runs using Task agents that simulate GoT operations.

## Understanding Graph of Thoughts

Graph of Thoughts is a reasoning framework where:
- **Thoughts = Nodes**: Each research finding or synthesis is a node
- **Edges = Dependencies**: Connect parent thoughts to children
- **Transformations**: Operations that create (Generate), merge (Aggregate), or improve (Refine) thoughts
- **Scoring**: Every thought is evaluated 0-10 for quality
- **Pruning**: Low-scoring branches are abandoned
- **Frontier**: Active nodes available for expansion

The system explores multiple research paths in parallel, scores them, and finds optimal solutions through graph traversal.

## The 7-Phase Deep Research Process
prep: make sure you put all of your produced documents inside of the folder /RESERACH/[create project name] where create project name is a name you decide based on the inquiry.  Also note that when you create files break down into smaller doucments to avoid context limitations.  Make sure you also compelte all tasks you define from the start of the project and track completion as you go.
### Phase 1: Question Scoping
- Clarify the research question with the user
- Define output format and success criteria
- Identify constraints and desired tone
- Create unambiguous query with clear parameters

### Phase 2: Retrieval Planning
- Break main question into subtopics
- Generate specific search queries
- Select appropriate data sources
- Create research plan for user approval
- Use GoT to model the research as a graph of operations

### Phase 3: Iterative Querying
- Execute searches systematically
- Navigate and extract relevant information
- Formulate new queries based on findings
- Use multiple search modalities (web search, file analysis, etc.)
- Apply GoT operations for complex reasoning

### Phase 4: Source Triangulation
- Compare findings across multiple sources
- Validate claims with cross-references
- Handle inconsistencies
- Assess source credibility
- Use GoT scoring functions to evaluate information quality

### Phase 5: Knowledge Synthesis
- Structure content logically
- Write comprehensive sections
- Include inline citations for every claim
- Add data visualizations when relevant
- Use GoT to optimize information organization

### Phase 6: Quality Assurance
- Check for hallucinations and errors
- Verify all citations match content
- Ensure completeness and clarity
- Apply Chain-of-Verification techniques
- Use GoT ground truth operations for validation

### Phase 7: Output & Packaging
- Format for optimal readability
- Include executive summary
- Create proper bibliography
- Export in requested format

## How Graph of Thoughts Works for Research

### Core Concepts

1. **Graph Structure**: 
   - Each research finding is a node with a unique ID
   - Nodes have scores (0-10) indicating quality
   - Edges connect parent thoughts to child thoughts
   - The frontier contains active nodes for expansion

2. **Transformation Operations**:
   - **Generate(k)**: Create k new thoughts from a parent
   - **Aggregate(k)**: Merge k thoughts into one stronger thought
   - **Refine(1)**: Improve a thought without adding new content
   - **Score**: Evaluate thought quality
   - **KeepBestN(n)**: Prune to keep only top n nodes per level

3. **Research Quality Metrics**:
   - Citation density and accuracy
   - Source credibility
   - Claim verification
   - Comprehensiveness
   - Logical coherence

## Implementation Tools

### Core Tools:
1. **WebSearch**: Built-in web search capability for finding relevant sources
2. **WebFetch**: For extracting and analyzing content from specific URLs
3. **Read/Write**: For managing research documents locally
4. **Task**: For spawning autonomous agents for complex multi-step operations
5. **TodoWrite/TodoRead**: For tracking research progress

### MCP Server Tools:
1. **mcp__filesystem__**: File system operations (read, write, search files)
2. **mcp__puppeteer__**: Browser automation for dynamic web content
   - Navigate to pages requiring JavaScript
   - Take screenshots of web content
   - Extract data from interactive websites
   - Fill forms and interact with web elements

### Web Research Strategy:
- **Primary**: Use WebSearch tool for general web searches
- **Secondary**: Use WebFetch for extracting content from specific URLs
- **Advanced**: Use mcp__puppeteer__ for sites requiring interaction or JavaScript rendering
- **Note**: When MCP web fetch tools become available, prefer them over WebFetch as per documentation

### Data Analysis:
- Python code execution for data processing
- Visualization tools for creating charts/graphs
- Statistical analysis for quantitative research

## Graph of Thoughts Research Strategy

The system implements GoT using Task agents that act as transformation operations. When you request deep research, a controller agent maintains the graph state and deploys specialized agents to explore, refine, and aggregate research paths.

### Implementation Instructions

#### Step 1: Create Research Plan
Break down the main research question into specific subtopics:
- Subtopic 1: Current state and trends
- Subtopic 2: Key challenges and limitations
- Subtopic 3: Future developments and predictions
- Subtopic 4: Case studies and real-world applications
- Subtopic 5: Expert opinions and industry perspectives

#### Step 2: Launch Parallel Agents
Use multiple Task tool invocations in a single response to launch agents simultaneously. Each agent should receive:
- Clear description of their research focus
- Specific instructions on what to find
- Expected output format

#### Step 3: Coordinate Results
After agents complete their tasks:
- Compile findings from all agents
- Identify overlaps and contradictions
- Synthesize into coherent narrative
- Maintain source attribution from each agent

### Example Multi-Agent Deployment

When researching a topic like "AI in Healthcare", deploy agents as follows:

**Agent 1**: "Research current AI applications in healthcare"
**Agent 2**: "Find challenges and ethical concerns in medical AI"
**Agent 3**: "Investigate future AI healthcare innovations"
**Agent 4**: "Gather case studies of successful AI healthcare implementations"
**Agent 5**: "Cross-reference and verify key statistics about AI healthcare impact"

### Best Practices for Multi-Agent Research

1. **Clear Task Boundaries**: Each agent should have a distinct focus to minimize redundancy
2. **Comprehensive Prompts**: Include all necessary context in agent prompts
3. **Parallel Execution**: Launch all agents in one response for maximum efficiency
4. **Result Integration**: Plan how to merge findings before launching agents
5. **Quality Control**: Always include at least one verification agent

### GoT-Enabled Agent Prompt Templates

**Deep Research GoT Agent Template**:
```
Execute Graph of Thoughts research for: [specific aspect] of [main topic]

1. Set up the GoT environment:
   ```python
   import sys
   sys.path.append('/home/umyong/recruit')
   sys.path.append('/home/umyong/recruit/graph-of-thoughts')
   
   from RESEARCH.deep_research_got import create_research_got, run_research
   from graph_of_thoughts import controller, language_models, operations
   ```

2. Create and execute a research graph:
   ```python
   # Create research-specific GoT
   topic = "[specific aspect]"
   gop = create_research_got(topic)
   
   # Add custom operations if needed
   # For web search integration:
   web_search_op = WebSearchOperation()
   gop.append_operation(web_search_op)
   
   # Run the graph
   result = run_research(topic, subtopic="[main topic context]")
   ```

3. The graph will:
   - Generate 5 research queries (Generate operation)
   - Execute searches and collect sources
   - Score each source for quality (Score operation)
   - Keep best 3 sources (KeepBestN operation)
   - Generate summaries with citations (Generate operation)
   - Validate all claims have sources (ValidateAndImprove operation)
   - Aggregate into final report (Aggregate operation)

4. Save results to /RESEARCH/[project_name]/[aspect].md

Return the final scored and validated research summary.
```

**Cross-Validation GoT Agent Template**:
```
Execute Graph of Thoughts validation for research findings:

1. Import GoT and create validation graph:
   ```python
   from graph_of_thoughts import operations
   
   # Create validation-focused graph
   val_gop = operations.GraphOfOperations()
   
   # Extract claims from all research
   val_gop.append_operation(operations.Generate(1, 1))  # Extract claims
   
   # Cross-reference each claim
   cross_ref = CrossReferenceOperation()
   val_gop.append_operation(cross_ref)
   
   # Score claim validity
   val_gop.append_operation(operations.Score(scoring_function=claim_validity_score))
   
   # Keep only validated claims
   val_gop.append_operation(operations.KeepValid())
   ```

2. Process these findings:
   [List of findings to validate]

3. Return validation report with:
   - Claim validity scores
   - Contradictions found
   - Source reliability ratings
```

**Synthesis GoT Agent Template**:
```
Execute Graph of Thoughts synthesis for final research report:

1. Create aggregation graph:
   ```python
   # Synthesis graph
   syn_gop = operations.GraphOfOperations()
   
   # Collect all research findings
   syn_gop.append_operation(operations.Generate(1, 1))
   
   # Score quality of each section
   syn_gop.append_operation(operations.Score(scoring_function=research_quality_score))
   
   # Aggregate into coherent narrative
   syn_gop.append_operation(operations.Aggregate(num_responses=1))
   
   # Improve clarity and organization
   syn_gop.append_operation(operations.Improve())
   
   # Final validation
   syn_gop.append_operation(operations.ValidateAndImprove(validate_function=verify_citations))
   ```

2. Input findings from all agents:
   [Research findings to synthesize]

3. Output comprehensive report with:
   - Executive summary
   - Integrated findings
   - Full citation list
   - Confidence scores
```

### Tool Usage Instructions for Agents

**WebSearch Usage**:
```
Use WebSearch with specific queries:
- Include key terms in quotes for exact matches
- Use domain filtering for authoritative sources
- Try multiple query variations
```

**WebFetch Usage**:
```
After WebSearch identifies URLs:
1. Use WebFetch with targeted prompts
2. Ask for specific information extraction
3. Request summaries of long content
```

**Puppeteer MCP Usage**:
```
For JavaScript-heavy sites:
1. mcp__puppeteer__puppeteer_navigate to URL
2. mcp__puppeteer__puppeteer_screenshot for visual content
3. mcp__puppeteer__puppeteer_evaluate to extract dynamic data
```

## Research Quality Checklist

- [ ] Every claim has a verifiable source
- [ ] Multiple sources corroborate key findings
- [ ] Contradictions are acknowledged and explained
- [ ] Sources are recent and authoritative
- [ ] No hallucinations or unsupported claims
- [ ] Clear logical flow from evidence to conclusions
- [ ] Proper citation format throughout

## Advanced Research Methodologies

### Chain-of-Density (CoD) Summarization
When processing sources, use iterative refinement to increase information density:
1. First pass: Extract key points (low density)
2. Second pass: Add supporting details and context
3. Third pass: Compress while preserving all critical information
4. Final pass: Maximum density with all essential facts and citations

### Chain-of-Verification (CoVe)
To prevent hallucinations:
1. Generate initial research findings
2. Create verification questions for each claim
3. Search for evidence to answer verification questions
4. Revise findings based on verification results
5. Repeat until all claims are verified

### ReAct Pattern (Reason + Act)
Agents should follow this loop:
1. **Reason**: Analyze what information is needed
2. **Act**: Execute search or retrieval action
3. **Observe**: Process the results
4. **Reason**: Determine if more information needed
5. **Repeat**: Continue until sufficient evidence gathered

### Multi-Agent Orchestration
For complex topics, deploy specialized agents:
- **Planner Agent**: Decomposes research into subtopics
- **Search Agents**: Execute queries and retrieve sources
- **Synthesis Agents**: Combine findings from multiple sources
- **Critic Agents**: Verify claims and check for errors
- **Editor Agent**: Polishes final output

### Human-in-the-Loop Checkpoints
Critical intervention points:
1. **After Planning**: Approve research strategy
2. **During Verification**: Expert review of technical claims
3. **Before Finalization**: Stakeholder sign-off
4. **Post-Delivery**: Feedback incorporation

## Citation Requirements & Source Traceability

### Mandatory Citation Standards

**Every factual claim must include:**
1. **Author/Organization** - Who made this claim
2. **Date** - When the information was published
3. **Source Title** - Name of paper, article, or report
4. **URL/DOI** - Direct link to verify the source
5. **Page Numbers** - For lengthy documents (when applicable)

### Citation Formats

**Academic Papers:**
```
(Author et al., Year, p. XX) with full citation in references
Example: (Smith et al., 2023, p. 145) 
Full: Smith, J., Johnson, K., & Lee, M. (2023). "Title of Paper." Journal Name, 45(3), 140-156. https://doi.org/10.xxxx/xxxxx
```

**Web Sources:**
```
(Organization, Year, Section Title)
Example: (NIH, 2024, "Treatment Guidelines")
Full: National Institutes of Health. (2024). "Treatment Guidelines for Metabolic Syndrome." Retrieved [date] from https://www.nih.gov/specific-page
```

**Direct Quotes:**
```
"Exact quote from source" (Author, Year, p. XX)
```

### Source Verification Protocol

1. **Primary Sources Only** - Link to original research, not secondary reporting
2. **Archive Links** - For time-sensitive content, include archive.org links
3. **Multiple Confirmations** - Critical claims need 2+ independent sources
4. **Conflicting Data** - Note when sources disagree and explain discrepancies
5. **Source Quality Ratings**:
   - **A**: Peer-reviewed RCTs, systematic reviews, meta-analyses
   - **B**: Cohort studies, case-control studies, clinical guidelines
   - **C**: Expert opinion, case reports, mechanistic studies
   - **D**: Preliminary research, preprints, conference abstracts
   - **E**: Anecdotal, theoretical, or speculative

### Traceability Requirements

**For Medical/Health Information:**
- PubMed ID (PMID) when available
- Clinical trial registration numbers
- FDA/regulatory body references
- Version/update dates for guidelines

**For Genetic Information:**
- dbSNP rs numbers
- Gene database links (OMIM, GeneCards)
- Population frequency sources (gnomAD, 1000 Genomes)
- Effect size sources with confidence intervals

**For Statistical Claims:**
- Sample sizes
- P-values and confidence intervals
- Statistical methods used
- Data availability statements

### Source Documentation Structure

Each research output must include:

1. **Inline Citations** - Throughout the text
2. **References Section** - Full bibliography at end
3. **Source Quality Table** - Rating each source A-E
4. **Verification Checklist** - Confirming each claim is sourced
5. **Data Availability** - Where raw data can be accessed

### Example Implementation

**Poor Citation:**
"Studies show that metformin reduces diabetes risk."

**Proper Citation:**
"The Diabetes Prevention Program demonstrated that metformin reduces diabetes incidence by 31% over 2.8 years in high-risk individuals (Knowler et al., 2002, NEJM, PMID: 11832527, https://doi.org/10.1056/NEJMoa012512)"

### Red Flags for Unreliable Sources

- No author attribution
- Missing publication dates
- Broken or suspicious URLs
- Claims without data
- Conflicts of interest not disclosed
- Predatory journals
- Retracted papers (check RetractionWatch)

### Agent Instructions for Citations

When deploying research agents, include:
```
"For every factual claim, provide:
1. Direct quote or specific data point
2. Author/organization name
3. Publication year
4. Full title
5. Direct URL/DOI
6. Confidence rating (High/Medium/Low)
Never make claims without sources. If uncertain, state 'Source needed' rather than guessing."
```

## Mitigation Strategies

### Hallucination Prevention:
- Always ground statements in source material
- Use Chain-of-Verification for critical claims
- Cross-reference multiple sources
- Explicitly state uncertainty when appropriate

### Coverage Optimization:
- Use diverse search queries
- Check multiple perspectives
- Include recent sources (check dates)
- Acknowledge limitations and gaps

### Citation Management:
- Track source URLs and access dates
- Quote relevant passages verbatim when needed
- Maintain source-to-statement mapping
- Use consistent citation format

## Research Tool Recommendations

### For Implementation (if building custom systems):
- **LangChain**: Orchestrate LLM + tools workflows
- **LlamaIndex**: Index and query document collections
- **Tavily Search API**: AI-optimized search results
- **Guardrails AI**: Enforce output requirements
- **FAISS/Pinecone**: Vector databases for semantic search

### Model Selection Strategy:
- **High-volume tasks**: Use faster models (GPT-4o-mini, Gemini Flash)
  - Query generation
  - Initial summarization
  - Basic searches
- **Critical tasks**: Use advanced models (GPT-4o, Gemini Pro)
  - Planning phase
  - Final synthesis
  - Verification loops
  - Complex reasoning

### Cost Optimization:
- Typical research: 120-220 LLM calls, 30-60 search calls
- Use tiered model approach to reduce costs
- Cache intermediate results
- Batch similar operations

## User Interaction Protocol

### Initial Question Gathering Phase

When a user requests deep research, I will engage in a structured dialogue to gather all necessary information before beginning research. This ensures the final output meets their exact needs.

### Required Information Checklist

Before starting research, I need to clarify:

1. **Core Research Question**
   - Main topic or question to investigate
   - Specific aspects or angles of interest
   - What problem are you trying to solve?

2. **Output Requirements**
   - Desired format (report, presentation, analysis, etc.)
   - Length expectations (executive summary vs comprehensive report)
   - File structure preferences (single document vs folder with multiple files)
   - Visual requirements (charts, graphs, diagrams, images)

3. **Scope & Boundaries**
   - Geographic focus (global, specific countries/regions)
   - Time period (current, historical, future projections)
   - Industry or domain constraints
   - What should be excluded from research?

4. **Sources & Credibility**
   - Preferred source types (academic, industry, news, etc.)
   - Any sources to prioritize or avoid
   - Required credibility level (peer-reviewed only, industry reports ok, etc.)

5. **Deliverable Structure**
   - Folder organization preferences
   - Naming conventions for files
   - Whether to include:
     - Raw research notes
     - Source PDFs/screenshots
     - Data files (CSV, JSON)
     - Visualization source files

6. **Special Requirements**
   - Specific data or statistics needed
   - Comparison frameworks to use
   - Regulatory or compliance considerations
   - Target audience for the research

### Output Creation Protocol

Based on gathered requirements, I will create all research outputs in the **RESEARCH** folder:

```
RESEARCH/
└── [topic_name]/
    ├── README.md (Overview and navigation guide)
    ├── executive_summary.md (1-2 page summary)
    ├── full_report.md (Comprehensive findings)
    ├── data/
    │   ├── raw_data.csv
    │   ├── processed_data.json
    │   └── statistics_summary.md
    ├── visuals/
    │   ├── charts/
    │   ├── graphs/
    │   └── infographics/
    ├── sources/
    │   ├── bibliography.md
    │   ├── source_summaries.md
    │   └── screenshots/
    ├── research_notes/
    │   ├── agent_1_findings.md
    │   ├── agent_2_findings.md
    │   └── synthesis_notes.md
    └── appendices/
        ├── methodology.md
        ├── limitations.md
        └── future_research.md
```

**Important**: All research outputs will be saved in `/home/umyong/deep_research/RESEARCH/[topic_name]/` where [topic_name] is a descriptive folder name based on the research topic.

### Question Templates I Will Ask

1. **Topic Clarification**
   - "What specific aspects of [topic] are most important for your needs?"
   - "Are you looking for current state analysis, historical trends, or future predictions?"

2. **Output Specification**
   - "Would you prefer a single comprehensive report or multiple focused documents?"
   - "Do you need visualizations? If so, what types would be most helpful?"

3. **Scope Definition**
   - "Are there any geographic regions or time periods I should focus on?"
   - "What level of technical detail is appropriate for your audience?"

4. **Source Preferences**
   - "Do you have any preferred sources or databases I should prioritize?"
   - "Are there any sources or viewpoints I should avoid?"

5. **Delivery Format**
   - "How would you like the files organized?"
   - "Do you need the raw research data or just the final analysis?"

### Example Interaction Flow

```
User: "I need research on AI in healthcare"

Assistant: "I'll help you research AI in healthcare. Let me ask some questions to ensure I deliver exactly what you need:

1. **Specific Focus**: What aspects of AI in healthcare interest you most?
   - Clinical diagnosis and treatment
   - Drug discovery and development
   - Hospital operations and management
   - Patient care and monitoring
   - Medical imaging and radiology
   - All of the above

2. **Output Format**: What type of deliverable would be most useful?
   - Comprehensive report (20-30 pages)
   - Executive summary (3-5 pages)
   - Presentation slides
   - Data analysis with visualizations

3. **Scope**: Any specific constraints?
   - Geographic focus (US, Europe, Global?)
   - Time period (current state, last 5 years, future projections?)
   - Healthcare sectors (hospitals, pharma, insurance, tech companies?)

4. **Audience**: Who will be reading this research?
   - Technical team
   - Business executives
   - Healthcare professionals
   - General audience"

User: "Focus on clinical diagnosis, comprehensive report, global scope but emphasize US and Europe, last 3 years plus future trends. Audience is healthcare executives considering AI adoption."

Assistant: "Perfect\! A few more clarifications:

5. **Data Requirements**: Would you like me to include:
   - Market size and growth projections?
   - Case studies of successful implementations?
   - ROI and cost-benefit analyses?
   - Regulatory landscape overview?

6. **Deliverable Structure**: Should I create:
   - Single comprehensive document?
   - Folder structure with main report + supporting documents?
   - Include raw data files and source screenshots?

7. **Visual Elements**: What would help communicate the findings?
   - Market trend graphs
   - Technology adoption timelines
   - Comparison tables
   - Process flow diagrams"

User: "Yes to all data requirements. Folder structure please with main report, executive summary, and supporting docs. Include market trends graphs and comparison tables. Raw data would be helpful for our internal analysis."

Assistant: "Excellent\! I have all the information needed. Here's my research plan:

**Research Plan: AI in Clinical Diagnosis**

**Output Structure:**
```
AI_Clinical_Diagnosis_Research/
├── README.md
├── 01_Executive_Summary.md (3-5 pages)
├── 02_Full_Report.md (25-30 pages)
├── 03_Data/
│   ├── market_analysis.csv
│   ├── adoption_rates.json
│   └── roi_calculations.xlsx
├── 04_Visuals/
│   ├── market_trends_2021-2024.png
│   ├── adoption_timeline.png
│   └── vendor_comparison_table.png
├── 05_Case_Studies/
│   ├── mayo_clinic_ai.md
│   ├── cleveland_clinic.md
│   └── european_examples.md
├── 06_Sources/
│   ├── bibliography.md
│   └── key_reports/
└── 07_Appendices/
    ├── regulatory_overview.md
    └── technical_glossary.md
```

**Multi-Agent Deployment:**
- Agent 1: Current market analysis and adoption rates
- Agent 2: Technology assessment and clinical outcomes
- Agent 3: Regulatory landscape and compliance
- Agent 4: Case studies and ROI analysis
- Agent 5: Future trends and emerging technologies
- Agent 6: Cross-verification and fact-checking

Shall I proceed with this research plan?"
```

## Complete Example: How GoT Research Works

### When you say: "Deep research CRISPR gene editing safety"

Here's the complete execution flow:

#### Iteration 1: Initialize and Explore
1. **Controller Agent** creates root node: "Research CRISPR gene editing safety"
2. **Generate(3)** deploys 3 parallel agents exploring:
   - Current evidence and success rates
   - Safety concerns and limitations
   - Future implications and regulations
3. **Results**: 3 thoughts with scores (6.8, 8.2, 7.5)
4. **Graph state** saved with frontier = [n3(8.2), n2(7.5), n4(6.8)]

#### Iteration 2: Deepen Best Paths
1. **Controller** examines frontier, decides:
   - n3 (8.2): High score → Generate(3) for deeper exploration
   - n2 (7.5): Medium → Generate(2) 
   - n4 (6.8): Low → Refine(1) to improve
2. **6 agents** deployed in parallel
3. **Best result**: "High-fidelity SpCas9 variants reduce off-targets by 95%" (Score: 9.1)

#### Iteration 3: Aggregate Strong Branches  
1. **Controller** sees multiple high scores
2. **Aggregate(3)** merges best thoughts into comprehensive synthesis
3. **Score**: 9.3 - exceeds threshold

#### Iteration 4: Final Polish
1. **Refine(1)** enhances clarity and completeness
2. **Final thought** scores 9.5
3. **Output**: Best path through graph becomes research report

### What Makes This True GoT

1. **Graph maintained** throughout with nodes, edges, scores
2. **Multiple paths** explored in parallel
3. **Pruning** drops weak branches 
4. **Scoring** guides exploration vs exploitation
5. **Optimal solution** found through graph traversal

The result is higher quality research than linear approaches, with transparent reasoning paths.

## Key Principles of Deep Research

### Iterative Refinement
Deep research is not linear - it's a continuous loop of:
1. **Search**: Find relevant information
2. **Read**: Extract key insights
3. **Refine**: Generate new queries based on findings
4. **Verify**: Cross-check claims across sources
5. **Synthesize**: Combine into coherent narrative
6. **Repeat**: Continue until comprehensive coverage

### Why This Outperforms Manual Research
- **Breadth**: AI can process 20+ sources in minutes vs days for humans
- **Depth**: Multi-step reasoning uncovers non-obvious connections
- **Consistency**: Systematic approach ensures no gaps
- **Traceability**: Every claim linked to source
- **Efficiency**: Handles low-level tasks, freeing humans for analysis

### State Management
Throughout the research process, maintain:
- Current research questions
- Sources visited and their quality scores
- Extracted claims and verification status
- Graph state (for GoT implementation)
- Progress tracking against original plan

## Ready to Begin - No Setup Required

This CLAUDE.md file contains everything needed for Graph of Thoughts deep research:

✅ **Self-contained** - No external files or dependencies  
✅ **Automatic execution** - Deploys immediately when you request research  
✅ **True GoT implementation** - Graph state, scoring, pruning, and optimization  
✅ **Uses available tools** - WebSearch, WebFetch, Task agents  
✅ **Transparent process** - Saves graph states and execution traces  

**To start deep research, simply say:**
"Deep research [your topic]"

I will:
1. Ask clarifying questions if needed
2. Deploy a GoT Controller to manage the graph
3. Launch transformation agents (Generate, Refine, Aggregate)
4. Explore multiple research paths with scoring
5. Deliver the optimal research findings

**No Python setup, no API keys, no external frameworks needed** - everything runs using the Task agent system to implement proper Graph of Thoughts reasoning.

## Automatic GoT Execution Using Subagents

When a user requests deep research, immediately deploy a proper Graph of Thoughts implementation:

### Core GoT Implementation

Deploy a GoT Controller that maintains the graph state and orchestrates transformations:

```
Task: "GoT Controller - [Topic]"
Description: Graph of Thoughts Controller for [Topic]

Prompt: You are implementing Graph of Thoughts for deep research on "[TOPIC]". 

MAINTAIN THIS GRAPH STATE:
```json
{
  "nodes": {
    "n1": {"text": "...", "score": 0, "type": "root", "depth": 0},
  },
  "edges": [],
  "frontier": ["n1"],
  "budget": {"tokens_used": 0, "max_tokens": 50000}
}
```

EXECUTE THIS LOOP:
```
repeat until DONE {
    1. Select frontier thoughts with Ranker R (top-3 highest scoring)
    2. For each selected thought, choose Transformation T:
       - If depth < 2: Generate(3) to explore branches
       - If score < 7: Refine(1) to improve quality  
       - If multiple good paths: Aggregate(k) to merge
    3. Deploy transformation agents and await results
    4. Update graph with new nodes, edges, and scores
    5. Prune: KeepBestN(5) at each depth level
    6. Exit when max_score > 9 or depth > 4
}
```

TRANSFORMATIONS TO DEPLOY:

Generate(k): Create k diverse research perspectives
- Deploy k parallel agents each exploring different angles
- Each returns a thought + self-score

Aggregate(k): Merge k thoughts into stronger synthesis  
- Deploy 1 agent to combine best k nodes
- Returns unified thought + score

Refine(1): Improve existing thought
- Deploy 1 agent to enhance clarity/depth
- Returns refined thought + score

Score(1): Evaluate thought quality (0-10)
- Accuracy of claims
- Citation quality
- Completeness
- Coherence

OUTPUT: Save graph state to /RESEARCH/[topic]/graph_state.json after each iteration
```

### Transformation Agent Templates

**Generate Agent Template**:
```
Task: "GoT Generate - Node [ID] Branch [k]"
Prompt: You are Generate transformation creating branch [k] from parent thought:
"[PARENT_THOUGHT]"

Your specific exploration angle: [ANGLE]
- Angle 1: Current state and evidence
- Angle 2: Challenges and limitations  
- Angle 3: Future implications

Execute:
1. WebSearch for "[TOPIC] [ANGLE]" - find 5 sources
2. Score each source quality (1-10)
3. WebFetch top 3 sources
4. Synthesize findings into coherent thought (200-400 words)
5. Self-score your thought (0-10) based on:
   - Claim accuracy
   - Citation density
   - Novel insights
   - Coherence

Return:
{
  "thought": "your synthesized findings with inline citations",
  "score": float,
  "sources": ["url1", "url2", "url3"],
  "operation": "Generate",
  "parent": "[PARENT_ID]"
}
```

**Aggregate Agent Template**:
```
Task: "GoT Aggregate - Nodes [IDs]"
Prompt: You are Aggregate transformation combining these [k] thoughts:

[THOUGHT_1]
Score: [SCORE_1]

[THOUGHT_2] 
Score: [SCORE_2]

[THOUGHT_k]
Score: [SCORE_k]

Combine into ONE stronger unified thought that:
- Preserves all important claims
- Resolves contradictions
- Maintains all citations
- Achieves higher quality than any input

Self-score the result (0-10).

Return:
{
  "thought": "aggregated synthesis",
  "score": float,
  "operation": "Aggregate",
  "parents": [parent_ids]
}
```

**Refine Agent Template**:
```
Task: "GoT Refine - Node [ID]"
Prompt: You are Refine transformation improving this thought:
"[CURRENT_THOUGHT]"
Current score: [SCORE]

Improve by:
1. Fact-check claims using WebSearch
2. Add missing context/nuance
3. Strengthen weak arguments
4. Fix citation issues
5. Enhance clarity

Do NOT add new major points - only refine existing content.

Self-score improvement (0-10).

Return refined thought with updated score.
```

### Graph Traversal Strategy

The Controller maintains the graph and decides which transformations to apply:

1. **Early Depth (0-2)**: Aggressive Generate(3) to explore search space
2. **Mid Depth (2-3)**: Mix of Generate for promising paths + Refine for weak nodes
3. **Late Depth (3-4)**: Aggregate best branches + final Refine
4. **Pruning**: Keep only top 5 nodes per depth level
5. **Termination**: When best node scores 9+ or depth exceeds 4

### Implementation Protocol

When deep research is requested:

1. **Initialize Graph**: Create root node with topic
2. **Deploy Controller**: Manages graph state and transformation decisions
3. **Iterative Execution**: 
   - Controller selects frontier nodes
   - Deploys appropriate transformation agents
   - Updates graph with results
   - Prunes low-scoring branches
4. **Final Output**: Best-scoring path becomes research result

The graph structure ensures:
- **Multiple perspectives** explored in parallel
- **Quality optimization** through scoring/pruning
- **Depth control** to manage token budget
- **Transparency** via saved graph states

This implements true Graph of Thoughts with proper graph maintenance, transformations, and scoring!

I'm ready to conduct Graph of Thoughts-powered deep research on any topic you provide!
