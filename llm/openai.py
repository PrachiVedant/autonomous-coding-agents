import os
from langchain_openai import ChatOpenAI


class OpenAIProvider:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-5",
            google_api_key=os.getenv("OPENAI_API_KEY"),
        )

    def generate(self, prompt: str):
        response = self.llm.invoke(prompt)
        return response.content