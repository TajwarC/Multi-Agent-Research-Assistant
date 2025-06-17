from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document

llm = ChatOpenAI(temperature=0)

def summarize_text(text: str) -> str:
    doc = [Document(page_content=text)]
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(doc)
    return summary
