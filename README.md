# Multi-Agent Research Assistant (Agentic AI Project)

## Overview
This project demonstrates a **multi-agent Agentic AI system** that autonomously performs research, summarizes information, and presents structured outputs. It simulates a real-world autonomous assistant capable of **multi-step reasoning, tool integration, and context-aware responses**.  

The agent accepts a user query, gathers information from multiple sources, summarizes it, and provides references — all via an interactive web interface.  

---

## Key Features

- **Multi-Agent Architecture**  
  - **Research Agents:** Retrieve information from **Tavily API**, **SerpAPI**, and **Wikipedia/Wikidata API**.  
  - **Summarization Agent:** Uses **OpenAI GPT models** to generate concise, structured summaries.  
  - **Structuring Agent:** Organizes results with numbered bullet points and citations.  
  - **Memory Agent:** Stores previous queries to maintain context for multi-step reasoning.

- **Interactive Interface:**  
  - Built with **Streamlit**, allowing users to enter queries and view structured outputs in real-time.

- **Autonomy & Context Awareness:**  
  - Demonstrates **agentic AI principles**: autonomy, task execution, memory management, and decision-making.

---

## Tech Stack

- **Python 3.x**  
- **LangChain** – Orchestration and integration of LLMs with APIs  
- **OpenAI GPT** – Summarization and NLP processing  
- **Tavily API** – General web search  
- **SerpAPI** – Google/Bing search scraping  
- **Wikipedia/Wikidata API** – Structured encyclopedic knowledge  
- **Streamlit** – Interactive web interface  
- **dotenv** – Secure API key management  

---

## Installation & Usage

1. **Clone the repository**
```bash
git clone https://github.com/devspidr/Research_Agent.git
cd Research_Agent
```


2. **Create a virtual environment and activate it**
```
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

4. **Create a .env file with your API keys:**
```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

5. **Run the Streamlit app**
```
streamlit run chat_agent.py
```

6. **Use the app**
```
streamlit run chat_agent.py
```



# Learning Outcomes / Highlights

Hands-on experience with agentic AI concepts: autonomy, multi-step reasoning, and tool usage.

Integration of multiple APIs and LLMs in a single workflow.

Designing an interactive research assistant with memory, structured output, and citations for real-world applications.
