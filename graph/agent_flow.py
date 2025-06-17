from agents.summarizer import summarize_text
from agents.citation_agent import fetch_citations

def run_graph(text):
    summary = summarize_text(text)
    citations = fetch_citations(summary[:300])  # limit to avoid long queries
    return {
        "summary": summary,
        "citations": citations
    }
