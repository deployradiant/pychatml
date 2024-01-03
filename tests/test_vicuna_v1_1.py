import unittest
from pychatml.vicuna_v1_1_converter import Vicuna_v1_1

EXPECTED_PROMPT = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: What is ChatGPT? ASSISTANT: ChatGPT is an advanced language model developed by OpenAI. It's designed to understand and generate natural language, so it can converse with users, answer questions, and even assist with various tasks.</s>USER: So, it's like a super-advanced chatbot? ASSISTANT: Yes, but it can engage in broader conversations and more complex reasoning.</s>"
EXPECTED_CHATML = [
    {'role': 'system', 'content': "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions."},
    {'role': 'user', 'content': 'What is ChatGPT?'},
    {'role': 'assistant', 'content': "ChatGPT is an advanced language model developed by OpenAI. It's designed to understand and generate natural language, so it can converse with users, answer questions, and even assist with various tasks."},
    {'role': 'user', 'content': "So, it's like a super-advanced chatbot?"},
    {'role': 'assistant', 'content': 'Yes, but it can engage in broader conversations and more complex reasoning.'}
]


class TestVicuna_V1_1(unittest.TestCase):

    def test_to_chatml(self):
        converter = Vicuna_v1_1()
        chatml = converter.to_chatml(EXPECTED_PROMPT)
        assert isinstance(chatml, list)
        assert len(chatml) > 0
        assert isinstance(chatml[0], dict)
        assert chatml == EXPECTED_CHATML

    def test_from_chatml(self):
        converter = Vicuna_v1_1()
        result = converter.from_chatml(EXPECTED_CHATML)

        assert isinstance(result, str)
        assert result == EXPECTED_PROMPT


if __name__ == "__main__":
    unittest.main()
