# check_env.py
from dotenv import load_dotenv
import os

load_dotenv()
print("Loaded Key Prefix:", os.getenv("OPENAI_API_KEY")[:8])
