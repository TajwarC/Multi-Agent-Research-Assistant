from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

def explain_concept(text: str) -> str:
    prompt = f"Explain the following scientific term or sentence in plain language: '{text}'"
    return llm.predict(prompt)
