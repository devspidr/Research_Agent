from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Optional: confirm the key
print("Loaded Key Prefix:", os.getenv("OPENAI_API_KEY")[:8])

# Initialize OpenAI model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Send a simple test message
response = llm.invoke("Hello! Can you explain what an AI agent is in one line?")

print("\n🤖 Model Response:\n", response.content)
