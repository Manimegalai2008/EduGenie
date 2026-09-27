from config import settings


async def explain_concept(topic: str) -> str:
    if not topic.strip():
        return "Please enter a topic to explain."

    # Temporary response for testing the web interface.
    # Gemini integration can be connected here later.
    return (
        f"Explanation for: {topic}\n\n"
        f"{topic} is explained here in a simple and easy-to-understand way. "
        "This response confirms that the Explain feature is connected correctly."
    )