import streamlit as st
from utils.pdf_loader import extract_text_from_pdf
from graph.agent_flow import run_graph
from agents.explainer import explain_concept
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Research Assistant", layout="wide")
st.title("📚 Multi-Agent Research Assistant")

# Upload and summarise
uploaded_file = st.file_uploader("Upload a research paper (PDF)", type="pdf")

if uploaded_file and "summary" not in st.session_state:
    with st.spinner("🔍 Processing PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        result = run_graph(text)
        st.session_state.summary = result["summary"]
        st.session_state.citations = result.get("citations", [])
# Display summary
if "summary" in st.session_state:
    st.subheader("📝 Summary")
    st.write(st.session_state.summary)

    st.subheader("🔗 Suggested Citations")
    for citation in st.session_state.citations:
        title = citation.get("title", "Untitled")
        url = citation.get("url", "#")
        year = citation.get("year", "n.d.")
        st.markdown(f"- [{title}]({url}) ({year})")

# Jargon explanation chatbot
if "summary" in st.session_state:
    st.divider()
    st.subheader("🤔 Jargon Explanation Assistant")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Chat input
    with st.form("chat_form"):
        user_input = st.text_input("Enter a sentence or term to explain:", key="explain_input")
        submitted = st.form_submit_button("Explain")

    if submitted and user_input:
        explanation = explain_concept(user_input)
        st.session_state.chat_history.append({
            "user": user_input,
            "assistant": explanation
        })

    # Display chat history (reverse chronological)
    for turn in st.session_state.chat_history[::-1]:
        with st.chat_message("user"):
            st.markdown(turn["user"])
        with st.chat_message("assistant"):
            st.markdown(turn["assistant"])

    # Option to clear chat
    if st.button("🗑️ Clear Conversation"):
        st.session_state.chat_history = []
        
if not uploaded_file and "summary" not in st.session_state:
    st.info("📄 Please upload a PDF to begin.")
