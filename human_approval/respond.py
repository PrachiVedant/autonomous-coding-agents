from human_approval.config import DECISION_CONFIG

def handle_human_response(decision_type, context):
    config = DECISION_CONFIG[decision_type]

    print(config["message"])
    print("Choices:", ", ".join(config["choices"]))

    choice = input("Decision: ").strip().lower()

    while choice not in config["choices"]:
        print("Invalid choice.")
        choice = input("Decision: ").strip().lower()

    return choice
