import os
from langchain_google_genai import ChatGoogleGenerativeAI


class GeminiProvider:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GEMINI_API_KEY"),
        )

    def generate(self, prompt: str):
        response = self.llm.invoke(prompt)
        return response.content