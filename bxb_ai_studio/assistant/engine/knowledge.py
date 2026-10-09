
KNOWLEDGE_BASE = [
    {
        "keywords": ["bxb ai studio", "ai studio"],
        "answer": (
            "BXB AI Studio is the AI tools project for the BXB ecosystem. "
            "It is designed to grow into a collection of useful assistant "
            "features, with a separate backend that can later integrate "
            "with the main BXB platform."
        ),
    },
    {
        "keywords": ["django", "technology stack"],
        "answer": (
            "BXB AI Studio currently uses Python and Django, with Django "
            "Templates for its web pages and SQLite for development data."
        ),
    },
    {
        "keywords": ["privacy", "personal data"],
        "answer": (
            "Avoid sharing passwords, authentication tokens, or sensitive "
            "personal information in chat. BXB AI Studio's data handling "
            "and privacy protections must be implemented and configured "
            "by the application."
        ),
    },
    {
        "keywords": ["paid api", "api cost", "free ai"],
        "answer": (
            "The current BXB AI engine does not require a paid model API. "
            "It uses local Python logic and stored information. More "
            "flexible language generation may require a local model or "
            "an external AI service later."
        ),
    },
]


def search_knowledge(message):
    """Return the most relevant simple keyword match, if any."""
    query = message.lower()
    best_answer = None
    best_score = 0

    for item in KNOWLEDGE_BASE:
        score = sum(
            1 for keyword in item["keywords"]
            if keyword.lower() in query
        )

        if score > best_score:
            best_score = score
            best_answer = item["answer"]

    return best_answer