import subprocess


def get_repo_structure():
    """Get the current repo file structure."""
    result = subprocess.run(
        ["find", ".", "-type", "f", "-not", "-path", "./.git/*",
         "-not", "-path", "./node_modules/*", "-not", "-path", "./venv/*"],
        capture_output=True, text=True
    )
    return result.stdout


def read_file(filepath):
    """Read a file's contents."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"File not found: {filepath}"
