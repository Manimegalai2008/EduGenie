async def summarize_text(text: str) -> str:
    if not text.strip():
        return "Please enter some text to summarize."

    sentences = text.strip().split(".")
    summary = ". ".join(sentences[:2]).strip()

    if summary and not summary.endswith("."):
        summary += "."

    return summary