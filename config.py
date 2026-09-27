from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "EduGenie - AI Learning Assistant"
    gemini_api_key: str = ""
    gemini_model: str = "gemini-1.5-flash"
    explanation_provider: str = "gemini"

    class Config:
        env_file = ".env"


settings = Settings()