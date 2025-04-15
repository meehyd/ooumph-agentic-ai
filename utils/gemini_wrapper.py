import os
import requests
from dotenv import load_dotenv

from google.generativeai import GenerativeModel

# Load environment variables from .env
load_dotenv()

class GeminiPro:
    def __init__(self, id="gemini-1.5-flash"):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("🚨 GEMINI_API_KEY not found. Please check your .env file.")

        self.gen_model_id = id
        self.gen_model = GenerativeModel(self.gen_model_id)
        self.embed_url = "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedContent"

    def embed_text(self, text: str, task="retrieval_document") -> list:
        """Embed text using Gemini embedding REST API."""
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "model": "models/embedding-001",
            "content": {"parts": [{"text": text}]},
            "taskType": task
        }

        response = requests.post(
            url=f"{self.embed_url}?key={self.api_key}",
            headers=headers,
            json=payload
        )

        response.raise_for_status()
        return response.json()["embedding"]["values"]

    def get_response(self, prompt: str) -> str:
        """Generate content from Gemini model."""
        response = self.gen_model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text
        elif hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].text
        else:
            return str(response)