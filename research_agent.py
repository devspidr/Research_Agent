from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# Load API keys
load_dotenv()
print("OPENAI key prefix:", os.getenv("OPENAI_API_KEY")[:8])
print("TAVILY key prefix:", os.getenv("TAVILY_API_KEY")[:8])

# Initialize model and search
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
search_tool = TavilySearch(max_results=3)

# Simple in-memory log for past searches
memory_log = []

def search_and_summarize(query):
    """Perform a Tavily search and summarize results."""
    print(f"\n🔍 Searching the web for: {query}")
    search_output = search_tool.invoke(query)

    if isinstance(search_output, dict) and "results" in search_output:
        results = search_output["results"]
        sources = "\n".join([r["url"] for r in results])
        text_data = "\n\n".join([r["content"] for r in results])
    else:
        results = []
        sources = "No structured sources found"
        text_data = str(search_output)

    # Include short-term memory in the prompt
    past_context = "\n\n".join(
        [f"- {m['query']}: {m['summary']}" for m in memory_log[-3:]]
    )
    memory_section = (
        f"\nPreviously, you researched:\n{past_context}\n\n"
        if past_context else ""
    )

    summary_prompt = (
        f"{memory_section}"
        f"Summarize the following information about '{query}' in 5 bullet points.\n"
        f"Include URLs if available:\n\n{text_data}"
    )

    summary = llm.invoke(summary_prompt)
    summary_text = summary.content

    # Save to memory
    memory_log.append({"query": query, "summary": summary_text})

    print("\n🧠 Summary:\n", summary_text)
    print("\n🔗 Sources:\n", sources)

# --- Example Usage ---
search_and_summarize("Latest information about Agentic AI frameworks")
search_and_summarize("Popular Agentic AI tools and libraries")
