# Deep Research Implementation Plan

## Overview
This document outlines the implementation plan for conducting deep research using the methodologies from deepresearchprocess.md and the Graph of Thoughts (GoT) framework.

## Understanding Deep Research

Deep research is an AI-driven approach that autonomously conducts multi-step research by:
- Iteratively searching, reading, and analyzing information
- Performing multi-step reasoning
- Compiling findings with explicit citations
- Using Graph of Thoughts for complex problem-solving

## The 7-Phase Deep Research Process

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

## Graph of Thoughts Integration

The GoT framework enhances deep research by:
1. **Modeling Research as Graph Operations**: Each research step becomes a node in the graph
2. **Parallel Processing**: Multiple research paths can be explored simultaneously
3. **Scoring & Optimization**: Information quality can be scored and optimized
4. **Backtracking**: Poor research paths can be abandoned for better alternatives

### GoT Operations for Deep Research:
- **Generate**: Create search queries and hypotheses
- **Score**: Evaluate information quality and relevance
- **GroundTruth**: Verify facts against authoritative sources
- **Aggregate**: Combine findings from multiple sources
- **Improve**: Refine research questions based on findings

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

## Multi-Agent Research Strategy

### Overview
To maximize research efficiency and coverage, spawn multiple Task agents to work on different aspects of the research simultaneously. This parallel approach mirrors how a research team would divide work among specialists.

### Agent Deployment Strategy

#### Phase 2 (Retrieval Planning) - Agent Distribution:
1. **Topic Decomposition Agent**: Break main question into 3-5 subtopics
2. **Launch Parallel Research Agents**: 
   - One agent per subtopic/research angle
   - Each agent gets specific research objectives
   - Agents work independently but share findings

#### Phase 3 (Iterative Querying) - Parallel Execution:

**Agent Type 1: Web Research Agents** (3-5 agents)
- Focus: Current information, trends, news
- Objective: Gather recent developments and real-world data
- Output: Structured summaries with source URLs

**Agent Type 2: Academic/Technical Agent** (1-2 agents)
- Focus: Research papers, technical specifications
- Objective: Find theoretical foundations and methodologies
- Output: Technical analysis with proper citations

**Agent Type 3: Cross-Reference Agent** (1 agent)
- Focus: Fact-checking and verification
- Objective: Validate claims across sources
- Output: Confidence ratings for key findings

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

### Agent Prompt Templates

**General Research Agent Template**:
"Research [specific aspect] of [main topic]. Use the following tools:
1. Start with WebSearch to find relevant sources
2. Use WebFetch to extract content from promising URLs
3. If sites require JavaScript, use mcp__puppeteer__puppeteer_navigate and screenshot
Focus on finding:
- Recent information (prioritize last 2 years)
- Authoritative sources
- Specific data/statistics
- Multiple perspectives
Provide a structured summary with all source URLs."

**Technical Research Agent Template**:
"Find technical/academic information about [topic aspect]. 
Tools to use:
1. WebSearch for academic papers and technical resources
2. WebFetch for PDF extraction and content analysis
3. mcp__filesystem__ tools to save important findings
Look for:
- Peer-reviewed papers
- Technical specifications
- Methodologies and frameworks
- Scientific evidence
Include proper academic citations."

**Verification Agent Template**:
"Verify the following claims about [topic]:
[List key claims to verify]
Use multiple search queries with WebSearch to find:
- Supporting evidence
- Contradicting information
- Original sources
Rate confidence: High/Medium/Low for each claim.
Explain any contradictions found."

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

## Ready to Begin

I have reviewed and understood:
1. The deep research process with 7-phase playbook
2. Multi-agent deployment strategies
3. Tool usage protocols (WebSearch, WebFetch, MCP servers)
4. User interaction and clarification process
5. Output creation and folder structure guidelines

**To start your deep research:**
Simply tell me your research topic, and I will:
1. Ask clarifying questions to understand your exact needs
2. Create a detailed research plan for your approval
3. Deploy multiple specialized agents to gather information
4. Synthesize findings into your requested format
5. Deliver a comprehensive, well-organized research output

I'm ready to conduct deep research on any topic you provide\!
