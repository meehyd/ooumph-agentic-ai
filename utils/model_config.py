import os
from dotenv import load_dotenv
from agno.models.google import Gemini

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")  # ✅ Correct env key

if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in environment.")

model = Gemini(api_key=gemini_api_key)