from agent.github_agent import solve_issue

if __name__ == "__main__":
    repo = input("GitHub repo (e.g. username/repo-name): ")
    issue_number = input("Issue number to fix: ")
    solve_issue(repo, int(issue_number))
