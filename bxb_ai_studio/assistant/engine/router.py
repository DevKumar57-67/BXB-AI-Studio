
import re

from .intents import detect_intent
from .knowledge import search_knowledge
from .responses import generate_response
from .tools import count_words, summarize_text, clean_text, draft_email


def make_result(reply, intent, confidence=0.95):
    """Return a consistent chatbot response."""
    return {
        "reply": reply,
        "intent": intent,
        "confidence": confidence,
    }


def extract_tool_text(message, pattern):
    """Remove a tool command and return the user's text."""
    return re.sub(
        pattern,
        "",
        message,
        count=1,
        flags=re.IGNORECASE,
    ).strip(" \t\n:,-")


def handle_tool_request(message):
    """Recognize and run supported text tools."""
    text = message.strip()

    # 1. Word count and text statistics
    word_pattern = (
        r"^\s*(?:please\s+)?"
        r"(?:count\s+(?:the\s+)?words|word\s+count|"
        r"text\s+statistics|analyze\s+text)"
        r"(?:\s+in\s+this\s+text)?\s*[:\-]?\s*"
    )

    if re.match(word_pattern, text, re.IGNORECASE):
        content = extract_tool_text(text, word_pattern)

        if not content:
            return make_result(
                "Please include the text you want me to analyze.",
                "word_count",
            )

        stats = count_words(content)

        reply = (
            f"Words: {stats['words']}\n"
            f"Characters: {stats['characters']}\n"
            f"Characters without spaces: "
            f"{stats['characters_without_spaces']}\n"
            f"Sentences: {stats['sentences']}\n"
            f"Paragraphs: {stats['paragraphs']}"
        )

        return make_result(reply, "word_count")

    # 2. Summarize text
    summary_pattern = (
        r"^\s*(?:please\s+)?"
        r"(?:summarize|summarise|summary\s+of)"
        r"(?:\s+(?:this|the\s+following)\s+text)?"
        r"\s*[:\-]?\s*"
    )

    if re.match(summary_pattern, text, re.IGNORECASE):
        content = extract_tool_text(text, summary_pattern)

        if not content:
            return make_result(
                "Please include the text you want me to summarize.",
                "summarize",
            )

        return make_result(summarize_text(content), "summarize")

    # 3. Clean text
    clean_pattern = (
        r"^\s*(?:please\s+)?"
        r"(?:clean\s+text|clean\s+up\s+text|"
        r"fix\s+spacing|normalize\s+whitespace)"
        r"\s*[:\-]?\s*"
    )

    if re.match(clean_pattern, text, re.IGNORECASE):
        content = extract_tool_text(text, clean_pattern)

        if not content:
            return make_result(
                "Please include the text you want me to clean.",
                "clean_text",
            )

        cleaned = clean_text(content)

        return make_result(cleaned, "clean_text")

    # 4. Draft an email
    email_pattern = (
        r"^\s*(?:please\s+)?"
        r"(?:draft|write|create|make)"
        r"\s+(?:(?:me)\s+)?"
        r"(?:a|an)\s+"
        r"(?:(?:friendly|professional)\s+)?"
        r"email"
        r"(?:\s+(?:about|regarding|for|to))?"
        r"\s*[:\-]?\s*"
    )

    if re.match(email_pattern, text, re.IGNORECASE):
        purpose = extract_tool_text(text, email_pattern)

        if not purpose:
            return make_result(
                "Please describe what the email should be about.",
                "draft_email",
            )

        tone = (
            "friendly"
            if re.search(r"\bfriendly\b", text, re.IGNORECASE)
            else "professional"
        )

        return make_result(
            draft_email(purpose, tone=tone),
            "draft_email",
        )

    return None



def get_reply(message):
    """
    Route messages to text tools, conversational responses,
    the knowledge base, or the fallback response.
    """

    # Try explicit tool requests first so greetings do not
    # intercept commands such as "count words: Hello world".
    tool_result = handle_tool_request(message)

    if tool_result is not None:
        return tool_result

    # Preserve existing conversational behavior.
    result = detect_intent(message)
    intent = result["intent"]

    if intent != "unknown":
        return {
            "reply": generate_response(intent),
            "intent": intent,
            "confidence": result["confidence"],
        }

    # Search the existing knowledge base.
    knowledge_answer = search_knowledge(message)

    if knowledge_answer:
        return {
            "reply": knowledge_answer,
            "intent": "knowledge",
            "confidence": 0.80,
        }

    return {
        "reply": (
            "I couldn't find a reliable answer to that yet. "
            "Try asking about BXB AI Studio, Django, privacy, "
            "or my capabilities. You can also ask me to summarize "
            "text, count words, clean text, or draft an email."
        ),
        "intent": "unknown",
        "confidence": result["confidence"],
    }

