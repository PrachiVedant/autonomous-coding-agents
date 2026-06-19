from github.issues import get_issue
from github.pull_requests import create_branch_and_pr
from repository.reader import get_repo_structure, read_file
from repository.writer import write_file
from agent.planner import plan_issue
from agent.code_generator import generate_fix


def solve_issue(repo, issue_number):
    """Orchestrate the issue-fix workflow."""
    print(f"\n1. Fetching issue #{issue_number}...")
    issue = get_issue(repo, issue_number)
    print(f"   Title: {issue['title']}")

    print("\n2. Reading repo structure...")
    structure = get_repo_structure()

    print("\n3. Analyzing the issue and planning the fix...")
    plan = plan_issue(issue, structure)
    print(f"   Approach: {plan['approach']}")
    print(f"   Files to read: {plan['files_to_read']}")

    print("\n4. Reading relevant files...")
    file_content = {}
    for filepath in plan['files_to_read']:
        content = read_file(filepath)
        file_content[filepath] = content
        print(f"   Read: {filepath}")

    print("\n5. Generating the fix...")
    fix = generate_fix(issue, plan, file_content)

    print("\n6. Applying changes")
    for change in fix['changes']:
        write_file(change['path'], change['content'])
        print(f"Updated : {change['path']}")

    branch_name = f"fix/issue-{issue_number}"
    print(f"\n7. Creating branch '{branch_name}' and opening PR...")

    pr_url = create_branch_and_pr(
        repo, issue_number, branch_name,
        f"fix-issue{issue_number}:{issue['title']}",
        fix['pr_description']
    )
    print(f"\n   PR created: {pr_url}")
    print("\nDone.")
