# AI News Across Africa — Intelligence Crew

A Python-powered multi-agent AI system that autonomously researches, filters, and delivers a weekly briefing on AI developments across Africa — startups, funding rounds, policy updates, tools, and events — straight to your inbox.

## Overview

Built with CrewAI and Python, this crew runs a fully automated intelligence pipeline. Four specialized agents work sequentially: one searches the web, one filters for African AI relevance, one structures the findings into a clean report, and one delivers it as a formatted HTML email via SendGrid.

## Agent Workflow

**4 agents. 4 tasks. 1 briefing.**

1. **Researcher** — Searches the web for the latest AI news, startups, funding rounds, and policy updates across Africa using SerperDev
2. **Africa AI Filter** — Reviews the research and keeps only AI-relevant developments from African countries — Nigeria, Kenya, South Africa, Egypt, and beyond
3. **Reporting Analyst** — Structures the filtered results into a categorized weekly briefing covering startups, funding, policy, tools, and events
4. **Email Sender** — Formats the final report as clean HTML and delivers it to the recipient's inbox via SendGrid

## Report Format

Each weekly briefing includes:
- **Headline Summary** — 3-sentence overview of the most important developments
- **Startups & Products** — What launched and who built it
- **Funding & Investment** — Rounds, amounts, and investor details
- **Policy & Regulation** — Government and regulatory updates
- **Tools & Research** — New tools and papers worth knowing
- **Events & Opportunities** — Upcoming dates and links
- **Key Takeaway** — One bold insight from the week

## Technical Stack

- **Python** for the core pipeline and agent logic
- **CrewAI** for multi-agent orchestration
- **SerperDev** for real-time web search
- **SendGrid** for HTML email delivery
- **Sequential process** — each agent builds on the previous output

## Setup

1. Clone the repo and install dependencies:
   ```
   pip install uv
   crewai install
   ```

2. Add your API keys to a `.env` file:
   ```
   OPENAI_API_KEY=your_key
   SERPER_API_KEY=your_key
   SENDGRID_API_KEY=your_key
   ```

3. Run the crew:
   ```
   crewai run
   ```

The pipeline generates a `report.md` file locally and sends the HTML briefing to the configured recipient email.

## Project Structure

```
src/ai_news_across_africa/
├── config/
│   ├── agents.yaml      # Agent roles, goals, and backstories
│   └── tasks.yaml       # Task descriptions and expected outputs
├── tools/
│   └── sendgrid_tool.py # Custom SendGrid email tool
└── crew.py              # Crew assembly and orchestration logic
```

**Builder:** Milena Tanui, AI Agent Builder & Automation Architect — Nairobi, Kenya

---
