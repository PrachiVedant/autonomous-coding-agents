import os
from langchain_google_genai import ChatGoogleGenerativeAI


class GeminiProvider:
    def __init__(self):
        self.default_model = "gemini-2.5-flash"
        self.api_key = os.getenv("GEMINI_API_KEY")

    def generate(
        self,
        prompt: str,
        model: str | None = None,
        max_tokens: int | None = None,
    ):
        llm = ChatGoogleGenerativeAI(
            model=model or self.default_model,
            api_key=self.api_key,
        )

        kwargs = {}
        if max_tokens is not None:
            kwargs["max_tokens"] = max_tokens

        response = llm.invoke(prompt, **kwargs)
        return response.content