from llm.openai import OpenAIProvider
from llm.groq import GroqProvider
from llm.gemini import GeminiProvider

class LLMGateway:
    DEFAULT_MODELS={
        "OpenAIProvider": "gpt-5", 
        "GroqProvider": "llama-3.3-70b-versatile", 
        "GeminiProvider": "gemini-2.5-flash",
    }
    def __init__(self):
        self.providers=[
            OpenAIProvider(),
            GroqProvider(),
            GeminiProvider()
        ]

    def generate(self,prompt:str):
        last_exception=None

        for provider in self.providers:
            provider_name=provider.__class__.__name__

            try:
                model=self.DEFAULT_MODELS[provider_name]
                print(f"Trying {provider_name} ({model})...")

                response=provider.generate(
                    model=model,
                    prompt=prompt,
                )
                print(f"{provider_name} succeeded.")

                return response
            except Exception as e:
                print(f"{provider_name} Failed: {e}")
                last_exception=e

        raise RuntimeError(
            f"All the providers failed.Last error:{last_exception}"
        )
        
            
