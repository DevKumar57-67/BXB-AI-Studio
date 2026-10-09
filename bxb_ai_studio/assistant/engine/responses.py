
RESPONSES = {
    "greeting": (
        "Hello! 👋 Welcome to BXB AI Assistant. "
        "What would you like help with today?"
    ),
    "identity": (
        "I'm BXB AI Assistant, the assistant built inside BXB AI Studio. "
        "I'm currently powered by a local Python response engine."
    ),
    "wellbeing": (
        "I'm running smoothly! 😊 What can I help you with?"
    ),
    "capabilities": (
        "Here's what I can help with so far:\n\n"
        "• Answer common questions\n"
        "• Explain BXB AI Studio\n"
        "• Find information in my knowledge base\n"
        "• Respond to greetings and basic conversation\n\n"
        "We're expanding my capabilities step by step."
    ),
    "thanks": (
        "You're welcome! 😊 Let me know if there's anything else I can help with."
    ),
    "goodbye": (
        "Goodbye! 👋 Thanks for chatting with BXB AI Assistant."
    ),
}


def generate_response(intent):
    return RESPONSES.get(intent)