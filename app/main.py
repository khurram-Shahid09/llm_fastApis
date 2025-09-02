from fastapi import FastAPI
from app.routes import llm_routes

app = FastAPI(title="LLM API")

# include routes
app.include_router(llm_routes.router, prefix="/api/v1")
