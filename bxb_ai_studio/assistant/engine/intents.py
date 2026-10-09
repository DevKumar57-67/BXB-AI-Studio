
import re
from difflib import SequenceMatcher


INTENTS = {
    "greeting": [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
        "hello there",
    ],
    "identity": [
        "who are you",
        "what is your name",
        "tell me about yourself",
        "what is bxb ai",
    ],
    "wellbeing": [
        "how are you",
        "how are you doing",
        "are you okay",
    ],
    "capabilities": [
        "what can you do",
        "how can you help me",
        "what are your features",
        "help me",
    ],
    "thanks": [
        "thank you",
        "thanks",
        "thank you so much",
    ],
    "goodbye": [
        "bye",
        "goodbye",
        "see you later",
        "talk to you later",
    ],
}


def normalize_text(text):
    """Normalize text for more reliable matching."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s']", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def detect_intent(message):
    """
    Return the best matching intent and a confidence score.
    Confidence is a heuristic, not a calibrated probability.
    """
    normalized = normalize_text(message)

    if not normalized:
        return {"intent": "unknown", "confidence": 0.0}

    # Prefer exact matches.
    for intent, examples in INTENTS.items():
        for example in examples:
            if normalized == normalize_text(example):
                return {"intent": intent, "confidence": 1.0}

    # Match a phrase inside a longer message.
    for intent, examples in INTENTS.items():
        for example in examples:
            phrase = normalize_text(example)

            if f" {phrase} " in f" {normalized} ":
                return {"intent": intent, "confidence": 0.90}

    # Fuzzy match short variations and small typing mistakes.
    best_intent = "unknown"
    best_score = 0.0

    for intent, examples in INTENTS.items():
        for example in examples:
            score = SequenceMatcher(
                None,
                normalized,
                normalize_text(example),
            ).ratio()

            if score > best_score:
                best_score = score
                best_intent = intent

    if best_score >= 0.78:
        return {
            "intent": best_intent,
            "confidence": round(best_score, 2),
        }

    return {"intent": "unknown", "confidence": round(best_score, 2)}