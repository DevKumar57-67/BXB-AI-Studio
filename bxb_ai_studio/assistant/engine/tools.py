
import re
from collections import Counter

from django.core.serializers import python


STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "is", "are",
    "was", "were", "be", "been", "being", "to", "of", "in",
    "on", "at", "for", "from", "with", "by", "as", "it",
    "this", "that", "these", "those", "i", "you", "he", "she",
    "we", "they", "them", "their", "my", "your", "our", "me",
    "do", "does", "did", "have", "has", "had", "will", "would",
    "can", "could", "should", "not", "so", "than", "then",
}


def count_words(text):
    """Return basic text statistics."""
    words = re.findall(r"\b[\w'-]+\b", text)

    return {
        "words": len(words),
        "characters": len(text),
        "characters_without_spaces": len(
            re.sub(r"\s", "", text)
        ),
        "sentences": len(
            [s for s in split_sentences(text) if s.strip()]
        ),
        "paragraphs": len(
            [p for p in text.splitlines() if p.strip()]
        ),
    }


def split_sentences(text):
    """Split text at common sentence-ending punctuation."""
    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", text.strip())
        if sentence.strip()
    ]



def summarize_text(text, max_sentences=6):
    """
    Create a more informative extractive summary.

    Selects important sentences from the beginning, middle,
    and end of the text while avoiding redundant selections.
    This does not use a language model.
    """
    sentences = split_sentences(text)

    if not sentences:
        return "Please provide some text to summarize."

    if len(sentences) <= max_sentences:
        return " ".join(sentences)

    words = re.findall(r"\b[a-zA-Z]{2,}\b", text.lower())

    useful_words = [
        word for word in words
        if word not in STOP_WORDS
    ]

    frequencies = Counter(useful_words)

    if not frequencies:
        return " ".join(sentences[:max_sentences])

    highest_frequency = max(frequencies.values())

    word_scores = {
        word: count / highest_frequency
        for word, count in frequencies.items()
    }

    scored_sentences = []

    for index, sentence in enumerate(sentences):
        sentence_words = re.findall(
            r"\b[a-zA-Z]{2,}\b",
            sentence.lower(),
        )

        useful = [
            word for word in sentence_words
            if word not in STOP_WORDS
        ]

        if not useful:
            score = 0
        else:
            score = (
                sum(word_scores.get(word, 0) for word in useful)
                / len(useful)
            )

        # Give a small boost to sentences that introduce
        # important information early in the text.
        position_bonus = 1 / (1 + index * 0.08)
        score *= position_bonus

        scored_sentences.append((score, index, sentence))

    # Select the highest-scoring sentences.
    selected = sorted(
        scored_sentences,
        key=lambda item: item[0],
        reverse=True,
    )[:max_sentences]

    # Restore their original order.
    selected.sort(key=lambda item: item[1])

    return " ".join(
        sentence for _, _, sentence in selected
    )




def clean_text(text):
    """Normalize whitespace without changing the wording."""
    text = text.replace("\r\n", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def draft_email(purpose, tone="professional"):
    """
    Create a simple editable email template.
    The user should replace the placeholders before sending.
    """
    purpose = purpose.strip()

    if not purpose:
        return "Please describe what the email should be about."

    tone = tone.lower().strip()

    if tone == "friendly":
        greeting = "Hi [Recipient Name],"
        closing = "Best,"
    else:
        greeting = "Dear [Recipient Name],"
        closing = "Kind regards,"

    return (
        f"Subject: {purpose[:70]}\n\n"
        f"{greeting}\n\n"
        f"I hope you're doing well.\n\n"
        f"I'm writing regarding {purpose.rstrip('.')}.\n\n"
        "Please let me know if you need any additional information.\n\n"
        f"{closing}\n[Your Name]"
    )