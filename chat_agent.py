# streamlit_multi_agent.py
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain_tavily import TavilySearch
import json
import streamlit as st

# -----------------------------
# Load API keys
# -----------------------------
load_dotenv()
print("OPENAI key prefix:", os.getenv("OPENAI_API_KEY")[:8])
print("TAVILY key prefix:", os.getenv("TAVILY_API_KEY")[:8])

# -----------------------------
# Initialize models and tools
# -----------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
search_tool = TavilySearch(max_results=3)

# -----------------------------
# In-memory memory log
# -----------------------------
if "memory_log" not in st.session_state:
    st.session_state.memory_log = []

# -----------------------------
# Memory Agent
# -----------------------------
def get_relevant_memory(query, top_n=3):
    keywords = query.lower().split()
    relevant = []
    for entry in reversed(st.session_state.memory_log):
        if any(k in entry["query"].lower() for k in keywords):
            relevant.append(entry)
        if len(relevant) >= top_n:
            break
    return relevant

# -----------------------------
# Research Agent
# -----------------------------
def research_agent(query):
    st.write(f"🔍 Researching: **{query}**")
    search_output = search_tool.invoke(query)
    if isinstance(search_output, dict) and "results" in search_output:
        results = search_output["results"]
        sources = [r["url"] for r in results]
        content = "\n\n".join([r["content"] for r in results])
    else:
        results = []
        sources = []
        content = str(search_output)
    return content, sources

# -----------------------------
# Summarization Agent
# -----------------------------
def summarization_agent(query, text, memory_context=""):
    summary_prompt = f"{memory_context}\nSummarize the following information about '{query}' in 5 numbered bullet points. Include URLs as citations:\n\n{text}"
    summary = llm.invoke(summary_prompt)
    return summary.content

# -----------------------------
# Structuring Agent
# -----------------------------
def structuring_agent(summary_text, sources):
    structured_output = {
        "summary": summary_text,
        "sources": sources
    }
    return structured_output

# -----------------------------
# Combined Agent Workflow
# -----------------------------
def run_agents(query):
    # Memory context from previous queries
    past_context = "\n\n".join(
        [f"- {m['query']}: {m['summary']}" for m in get_relevant_memory(query)]
    )
    memory_context = f"Previously related searches:\n{past_context}\n\n" if past_context else ""

    # Step 1: Research Agent
    content, sources = research_agent(query)

    # Step 2: Summarization Agent
    summary_text = summarization_agent(query, content, memory_context)

    # Step 3: Structuring Agent
    structured_output = structuring_agent(summary_text, sources)

    # Step 4: Save to memory
    st.session_state.memory_log.append({"query": query, "summary": summary_text, "sources": sources})

    return structured_output

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🤖 Multi-Agentic AI Research Assistant")
st.write("This agent uses multiple sub-agents to autonomously research, summarize, and structure responses.")
st.write("Your past queries are remembered during this session.")

user_query = st.text_input("Enter your query:")

if st.button("Run Agent"):
    if user_query:
        result = run_agents(user_query)
        st.subheader("🧠 Structured Summary:")
        st.write(result["summary"])
        st.subheader("🔗 Sources:")
        for url in result["sources"]:
            st.write(f"- {url}")

# Display memory log
with st.expander("📚 Recent Memory"):
    for i, entry in enumerate(st.session_state.memory_log[-5:], 1):
        st.write(f"{i}. {entry['query']}")
