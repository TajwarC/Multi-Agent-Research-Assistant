from langchain.chat_models import ChatOpenAI
import os

llm = ChatOpenAI(
    temperature=0,
    model=os.getenv("OPENAI_MODEL", "gpt-4.1-nano"),
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def explain_concept(text: str) -> str:
    prompt = f"Explain the following scientific term or sentence in plain language: '{text}'"
    return llm.predict(prompt)
