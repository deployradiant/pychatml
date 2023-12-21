import unittest
from anthropic import AI_PROMPT, HUMAN_PROMPT

from pychatml.anthropic_converter import AnthropicConverter

converter = AnthropicConverter()
EXPECTED_STRING = f"{HUMAN_PROMPT} Hello there.\n{AI_PROMPT} Hi, I'm Claude. How can I help you?\n{HUMAN_PROMPT} Can you explain LLMs in plain English?\n{AI_PROMPT}"
EXPECTED_CHATML = [
    {"role": "user", "content": "Hello there."},
    {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
    {"role": "user", "content": "Can you explain LLMs in plain English?"},
]


class TestAnthropicConverter(unittest.TestCase):
    def setUp(self):
        self.converter = AnthropicConverter()

    def test_to_chatml(self):
        chatml = converter.to_chatml(EXPECTED_STRING)
        print(chatml)
        assert isinstance(chatml, list)
        assert len(chatml) > 0
        assert isinstance(chatml[0], dict)
        assert chatml == EXPECTED_CHATML

    def test_from_chatml(self):
        result = converter.from_chatml(EXPECTED_CHATML)
        assert isinstance(result, str)
        assert result == EXPECTED_STRING


if __name__ == "__main__":
    unittest.main()
