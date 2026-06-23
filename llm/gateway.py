import os
from openai import OpenAI


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_ADMIN_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing OpenAI credentials. "
            "Set OPENAI_API_KEY or OPENAI_ADMIN_KEY in your environment."
        )

    return OpenAI(api_key=api_key)
