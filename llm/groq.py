import os
from langchain_groq import ChatGroq


class GroqProvider:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            google_api_key=os.getenv("GROQ_API_KEY"),
        )

    def generate(self, prompt: str):
        response = self.llm.invoke(prompt)
        return response.content