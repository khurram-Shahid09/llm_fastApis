from fastapi import APIRouter
from app.models.schemas import PromptRequest, LLMResponse
from app.services.llm_service import call_llm

router = APIRouter(tags=["LLM"])

@router.post("/generate", response_model=LLMResponse)
async def generate_text(data: PromptRequest):
    result = await call_llm(data.prompt)
    return LLMResponse(response=result)
