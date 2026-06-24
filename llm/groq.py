import os
from langchain_groq import ChatGroq


class GroqProvider:
    def __init__(self):
        self.default_model = "llama-3.3-70b-versatile"
        self.api_key = os.getenv("GROQ_API_KEY")

    def generate(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int | None = None,
    ):
        llm = ChatGroq(
            model=model or self.default_model,
            api_key=self.api_key,
        )

        kwargs = {}
        if max_tokens is not None:
            kwargs["max_tokens"] = max_tokens

        response = llm.invoke(prompt, **kwargs)
        return response.content