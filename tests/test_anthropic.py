import unittest
from anthropic import AI_PROMPT, HUMAN_PROMPT

import pychatml

EXPECTED_PROMPT = f"{HUMAN_PROMPT} Hello there.\n{AI_PROMPT} Hi, I'm Claude. How can I help you?\n{HUMAN_PROMPT} Can you explain LLMs in plain English?\n{AI_PROMPT}"
EXPECTED_CHATML = [
    {"role": "user", "content": "Hello there."},
    {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
    {"role": "user", "content": "Can you explain LLMs in plain English?"},
]


class TestAnthropic(unittest.TestCase):
    def test_to_chatml(self):
        chatml = pychatml.anthropic.to_chatml(EXPECTED_PROMPT)
        assert isinstance(chatml, list)
        assert len(chatml) > 0
        assert isinstance(chatml[0], dict)
        assert chatml == EXPECTED_CHATML

    def test_from_chatml(self):
        result = pychatml.anthropic.from_chatml(EXPECTED_CHATML)
        assert isinstance(result, str)
        assert result == EXPECTED_PROMPT


if __name__ == "__main__":
    unittest.main()
