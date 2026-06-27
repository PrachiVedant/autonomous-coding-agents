# Autonomous Coding Agent

An AI-powered autonomous coding agent that automatically analyzes GitHub issues, understands a repository, generates code fixes, applies changes, creates pull requests, and validates its own output using LLM-as-a-Judge and safety guardrails.

---

## Features

* Automatically fetches GitHub issues
* Clones repositories locally
* Reads repository structure and relevant files
* Uses an LLM to plan the required code changes
* Generates code fixes automatically
* Applies changes to the repository
* Creates Git branches
* Commits and pushes changes
* Opens GitHub Pull Requests automatically
* Uses pre-agent safety guardrails to block dangerous requests
* Uses post-agent LLM-as-a-Judge to verify correctness and security
* Supports automated evaluation using synthetic benchmarks

---

## Architecture

```
GitHub Issue
      │
      ▼
Repository Clone
      │
      ▼
Repository Reader
      │
      ▼
Planning Agent
      │
      ▼
Code Generator
      │
      ▼
Apply Changes
      │
      ▼
Git Operations
      │
      ▼
LLM-as-a-Judge
      │
      ▼
Pull Request
```

---

## Project Structure

```
agent/
│── github_agent.py
│── planner.py
│── code_generator.py

config/
│── env.py

evals/
│── datasets.py
│── evaluator.py
│── correctness.py
│── relevance.py

github/
│── issues.py
│── repository.py
│── git_operations.py

guardrails/
│── before_agent.py
│── after_agent.py

llm/
│── gateway.py
│── openai.py
│── groq.py
│── gemini.py

repository/
│── reader.py
│── writer.py

main.py
requirements.txt
README.md
```

---

## Technologies Used

* Python
* OpenAI GPT
* LangChain
* LangGraph
* GitHub CLI
* Git
* Groq API
* Google Gemini API

---

## Workflow

1. Fetch a GitHub issue.
2. Clone the target repository.
3. Read the repository structure.
4. Plan the required code changes using an LLM.
5. Read only the relevant source files.
6. Generate code modifications.
7. Apply the generated changes.
8. Commit and push the changes.
9. Automatically create a Pull Request.
10. Validate the generated output using an LLM Judge.

---

## Before-Agent Guardrails

The project blocks unsafe requests before the agent executes.

Protected against:

* Dangerous shell commands (`rm -rf`, `sudo`, etc.)
* Secret extraction
* Sensitive file access (`.env`, SSH keys, credentials)
* External data exfiltration
* Unauthorized or malicious requests

Example:

```
User Request:
Delete the entire repository

Result:
Request blocked by guardrails.
```

---

## After-Agent LLM Judge

After code generation, an independent LLM reviews the output.

The judge verifies:

* The solution satisfies the user's request
* No dangerous or malicious code is introduced
* No secrets are exposed
* No unrelated functionality is modified

Only responses that pass all checks are accepted.

---

## Evaluation Framework

The project includes an automated evaluation pipeline.

Metrics:

* Correctness
* Relevance
* Average Latency

Example output:

```
Correctness Score: 100%
Relevance Score: 100%
Average Latency: 4.93s
```

Synthetic benchmark datasets are included to evaluate multiple issue-fixing scenarios.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd autonomous-coding-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file and configure the following:

```
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
GEMINI_API_KEY=your_key
GITHUB_TOKEN=your_token
```

---

## Running the Agent

```bash
python main.py
```

Example:

```
GitHub repo:
owner/repository

Issue number:
1
```

The agent will:

* Clone the repository
* Analyze the issue
* Generate the fix
* Commit the changes
* Push a new branch
* Create a Pull Request

---

## Running Evaluations

```bash
python -m evals.evaluator
```

This evaluates the agent on multiple benchmark issues and reports:

* Correctness
* Relevance
* Latency

---

## Example Pull Request Workflow

```
Issue
    ↓
Planner
    ↓
Read Files
    ↓
Generate Fix
    ↓
Apply Changes
    ↓
Commit
    ↓
Push
    ↓
Create PR
    ↓
LLM Judge Validation
```

---

## Future Improvements

* Retrieval-Augmented Generation (RAG) over repositories
* Multi-file dependency analysis
* Automatic test execution
* Code review agent
* Multi-agent collaboration
* Docker sandbox execution
* Human approval for sensitive changes
* Support for additional LLM providers

---

## Skills Demonstrated

* Autonomous AI Agents
* Large Language Models (LLMs)
* LangChain
* LangGraph Middleware
* LLM-as-a-Judge
* Prompt Engineering
* GitHub Automation
* Software Engineering
* AI Safety Guardrails
* Repository Analysis
* Automated Code Generation
* Evaluation Framework Design

---

## Author

**Prachi Vedant**

AI & Data Science Student | Machine Learning & LLM Enthusiast

Interested in building autonomous AI systems, coding agents, Retrieval-Augmented Generation (RAG), and production-ready LLM applications.
