import os


def write_file(filepath, content):
    """Write content to a file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content)
    return f"Written to {filepath}"
