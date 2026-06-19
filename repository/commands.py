import subprocess
import os

REPO_PATH = os.getcwd()


def run_command(command):
    """Run a shell command and return output."""
    result = subprocess.run(
        command, shell=True, capture_output=True, text=True, cwd=REPO_PATH
    )
    return f"stdout: {result.stdout}\nstderr: {result.stderr}\nreturncode: {result.returncode}"
