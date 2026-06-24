# ###autonomous-coding-agent/
# │
# ├── agent/
# │   ├── github_agent.py
# │   ├── planner.py
# │   └── code_generator.py
# │
# ├── guardrails/
# │   ├── before_agent.py          # CodingSafetyFilter
# │   └── after_agent.py           # LLMJudgeMiddleware
# │
# ├── human_loop/
# │   └── approval.py              # HumanInTheLoopMiddleware
# │
# ├── llm/
# │   ├── gateway.py
# │   ├── openai_provider.py
# │   └── gemini_provider.py
# │
# ├── evals/
# │   ├── evaluator.py, correctnees.py,relevance.py
# │   └── datasets/
# │
# ├── github/
# │   ├── issues.py
# │   └── pull_requests.py
# │
# ├── repository/
# │   ├── files.py
# │   └── commands.py
# │
# ├── main.py
# ├── requirements.txt
# └── README.md