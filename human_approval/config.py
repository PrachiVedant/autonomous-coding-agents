DECISION_CONFIG = {
    "commit": {
        "choices": ["approve", "reject"],
        "message": "Approve commit?"
    },

    "push": {
        "choices": ["approve", "reject"],
        "message": "Approve push to remote?"
    },

    "create_pr": {
        "choices": ["approve", "reject", "edit"],
        "message": "Approve PR creation?"
    },

    "large_change": {
        "choices": ["approve", "reject", "request_changes"],
        "message": "Large number of files modified."
    },

    "sensitive_files": {
        "choices": ["approve", "reject"],
        "message": "Sensitive files detected."
    },
}