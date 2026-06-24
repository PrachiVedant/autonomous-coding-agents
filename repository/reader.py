import os
from pathlib import Path


def get_repo_structure():
    """Get the current repo file structure."""
    root = Path.cwd()
    paths = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.match(".git/*"):
            continue
        if path.match("node_modules/*"):
            continue
        if path.match("venv/*") or path.match(".venv/*"):
            continue
        paths.append(str(path.relative_to(root)))

    return "\n".join(sorted(paths))


def read_file(filepath):
    """Read a file's contents."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"File not found: {filepath}"
