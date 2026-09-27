
from pydantic import BaseModel
from typing import Optional


class APIResponse(BaseModel):
    success: bool
    result: object


class QARequest(BaseModel):
    question: str


class ExplainRequest(BaseModel):
    topic: str


class QuizRequest(BaseModel):
    text: str
    count: int = 3


class SummaryRequest(BaseModel):
    text: str


class LearningPathRequest(BaseModel):
    topic: str
    level: str = "beginner"
    weeks: int = 4