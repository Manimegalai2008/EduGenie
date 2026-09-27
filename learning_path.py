async def get_learning_recommendations(
    topic: str,
    level: str = "beginner",
    weeks: int = 4
):
    if not topic.strip():
        return "Please enter a topic."

    return {
        "topic": topic,
        "level": level,
        "weeks": weeks,
        "recommendations": [
            f"Week 1: Learn the basics of {topic}",
            f"Week 2: Practice important concepts in {topic}",
            f"Week 3: Solve exercises related to {topic}",
            f"Week 4: Complete a small project using {topic}"
        ]
    }