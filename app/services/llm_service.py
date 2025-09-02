import httpx
from app.core.config import settings

async def call_llm(prompt: str) -> str:
    headers = {
        "x-goog-api-key": settings.LLM_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.post(settings.LLM_API_URL, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            # Safe extraction of generated text
            try:
                return result["candidates"][0]["content"]["parts"][0]["text"]
            except (KeyError, IndexError):
                return str(result)  # fallback for debugging
    except httpx.HTTPStatusError as e:
        return f"Error from Gemini API: {e.response.text}"
    except Exception as e:
        return f"Unexpected error: {e}"
