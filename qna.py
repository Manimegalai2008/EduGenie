async def answer_question(question: str) -> str:
    if not question.strip():
        return "Please enter a question."

    return (
        f"Answer for: {question}\n\n"
        "This is a simple response for testing the EduGenie Q&A feature."
    )