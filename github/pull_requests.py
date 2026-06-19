import subprocess
from repository.commands import run_command


def create_branch_and_pr(repo, issue_number, branch_name, title, body):
    """Create a branch, commit changes, and open a PR"""
    commands = [
        f"git checkout -b {branch_name}",
        "git add -A",
        f'git commit -m "fix: {title}"',
        f"git push origin {branch_name}",
    ]

    for cmd in commands:
        result = run_command(cmd)
        print(f"  {cmd}: {result}")

    pr_result = subprocess.run(
        ["gh", "pr", "create", "--repo", repo,
         "--title", title, "--body", body,
         "--head", branch_name],
        capture_output=True, text=True
    )
    return pr_result.stdout
