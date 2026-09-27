from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import settings
from models import (
    APIResponse,
    ExplainRequest,
    LearningPathRequest,
    QARequest,
    QuizRequest,
    SummaryRequest,
)
from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


BASE_DIR = Path(__file__).resolve().parent

print("MAIN.PY LOADED")
app = FastAPI(
    title="EduGenie - AI Learning Assistant",
    version="1.0.0",
    description="Google Gemini powered educational assistant",
)

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "app_name": settings.app_name,
    },
)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "application": settings.app_name,
        "gemini_configured": bool(settings.gemini_api_key),
        "model": settings.gemini_model,
        "explanation_provider": settings.explanation_provider,
    }


@app.post("/qa", response_model=APIResponse)
async def qa(payload: QARequest):
    result = await answer_question(payload.question)

    return APIResponse(
        success=True,
        result=result,
    )


@app.post("/explain", response_model=APIResponse)
async def explain(payload: ExplainRequest):
    result = await explain_concept(payload.topic)

    return APIResponse(
        success=True,
        result=result,
    )


@app.post("/quiz", response_model=APIResponse)
async def quiz(payload: QuizRequest):
    result = await generate_quiz(
        payload.text,
        payload.count,
    )

    return APIResponse(
        success=True,
        result=result,
    )


@app.post("/summarize", response_model=APIResponse)
async def summarize(payload: SummaryRequest):
    result = await summarize_text(payload.text)

    return APIResponse(
        success=True,
        result=result,
    )


@app.post(
    "/learn/recommendations",
    response_model=APIResponse,
)
async def learning_path(payload: LearningPathRequest):
    result = await get_learning_recommendations(
        topic=payload.topic,
        level=payload.level,
        weeks=payload.weeks,
    )

    return APIResponse(
        success=True,
        result=result,
    )