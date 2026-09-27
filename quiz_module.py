async def generate_quiz(text: str, count: int = 3):
    if not text.strip():
        return "Please enter a topic for the quiz."

    questions = []

    for i in range(count):
        questions.append({
            "question": f"Sample Question {i + 1} about {text}",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer": "Option A"
        })

    return questions