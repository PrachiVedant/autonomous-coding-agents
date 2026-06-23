import subprocess
from langchain_core.tools import tool


@tool
def git_operations(
    action: str,
    branch_name: str = "",
    commit_message: str = "",
    repo: str = "",
    pr_title: str = "",
    pr_body: str = "",
    num_files_changed: int = 0,
    sensitive_files: list[str] | None = None,
) -> str:
    """
    Perform Git/GitHub operations.

    Parameters
    ----------
    action : str
        One of:
        - commit
        - push
        - create_pr

    branch_name : str
        Branch name to push.

    commit_message : str
        Commit message.

    repo : str
        GitHub repository in the format 'owner/repo'.

    pr_title : str
        Pull request title.

    pr_body : str
        Pull request description.

    num_files_changed : int
        Number of modified files. Used by Human-in-the-Loop.

    sensitive_files : list[str]
        Sensitive files being modified. Used by Human-in-the-Loop.
    """

    sensitive_files = sensitive_files or []

    try:
        if action == "commit":
            subprocess.run(
                ["git", "add", "-A"],
                check=True,
            )

            subprocess.run(
                ["git", "commit", "-m", commit_message],
                check=True,
            )

            return f"Committed changes: {commit_message}"

        elif action == "push":
            subprocess.run(
                ["git", "push", "origin", branch_name],
                check=True,
            )

            return f"Pushed branch '{branch_name}'"

        elif action == "create_pr":
            result = subprocess.run(
                [
                    "gh",
                    "pr",
                    "create",
                    "--repo",
                    repo,
                    "--title",
                    pr_title,
                    "--body",
                    pr_body,
                    "--head",
                    branch_name,
                ],
                capture_output=True,
                text=True,
                check=True,
            )

            return f"PR created successfully.\n{result.stdout}"

        else:
            return (
                "Invalid action. "
                "Supported actions: commit, push, create_pr."
            )

    except subprocess.CalledProcessError as e:
        return f"Git operation failed: {e}"

