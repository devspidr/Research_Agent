from dotenv import load_dotenv
import os

load_dotenv()

print("OpenAI Key:", os.getenv("OPENAI_API_KEY")[:10] + "...")
print("Tavily Key:", os.getenv("TAVILY_API_KEY")[:10] + "...")
