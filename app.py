import streamlit as st
from utils.pdf_loader import extract_text_from_pdf
from graph.agent_flow import run_graph

st.set_page_config(page_title="AI Research Assistant", layout="wide")
st.title("📚 Multi-Agent Research Assistant")

pdf = st.file_uploader("Upload a research paper (PDF)", type=["pdf"])

if pdf:
    with st.spinner("🔍 Processing PDF..."):
        text = extract_text_from_pdf(pdf)
        result = run_graph(text)

    st.subheader("🔎 Summary")
    st.write(result.get("summary", "No summary available."))

    st.subheader("📚 Suggested Citations")
    for citation in result.get("citations", []):
        st.markdown(f"- [{citation['title']}]({citation['url']}) by {', '.join(a['name'] for a in citation['authors'])} ({citation['year']})")

    st.subheader("🤔 Jargon Explanation")
    user_input = st.text_input("Enter a sentence or phrase to explain:")
    if user_input:
        from agents.explainer import explain_concept
        explanation = explain_concept(user_input)
        st.success(explanation)
