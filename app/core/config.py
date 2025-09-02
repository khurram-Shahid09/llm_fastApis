import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

class Settings:
    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "")
    LLM_API_URL: str = os.getenv("LLM_API_URL", "https://api.openai.com/v1/completions")

settings = Settings()
