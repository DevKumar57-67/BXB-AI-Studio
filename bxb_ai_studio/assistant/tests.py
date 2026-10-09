from django.test import TestCase

# Create your tests here.

from django.test import SimpleTestCase

from .engine.intents import detect_intent
from .engine.router import get_reply


class AssistantEngineTests(SimpleTestCase):

    def test_greeting(self):
        result = detect_intent("Hello!")
        self.assertEqual(result["intent"], "greeting")

    def test_identity(self):
        result = detect_intent("Who are you?")
        self.assertEqual(result["intent"], "identity")

    def test_knowledge_base(self):
        result = get_reply("Tell me about BXB AI Studio")
        self.assertEqual(result["intent"], "knowledge")
        self.assertIn("BXB AI Studio", result["reply"])

    def test_unknown_message_has_fallback(self):
        result = get_reply("Something completely unrecognized")
        self.assertTrue(result["reply"])

    def test_empty_message(self):
        result = get_reply("")
        self.assertEqual(result["intent"], "unknown")