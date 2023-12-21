import unittest
import pychatml


EXPECTED_PROMPT = """[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<</SYS>>

Hi, how are you? [/INST] Good thanks! 
[INST] Can you help me with this math program? [/INST]"""

EXPECTED_CHATML = [
    {
        "role": "system",
        "content": """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.""",
    },
    {"role": "user", "content": "Hi, how are you?"},
    {"role": "assistant", "content": "Good thanks!"},
    {"role": "user", "content": "Can you help me with this math program?"},
]


class TestLlama2(unittest.TestCase):
    def test_to_chatml(self):
        chatml = pychatml.llama2.to_chatml(EXPECTED_PROMPT)

        assert isinstance(chatml, list)
        assert len(chatml) > 0
        assert isinstance(chatml[0], dict)
        assert chatml == EXPECTED_CHATML

    def test_from_chatml(self):
        result = pychatml.llama2.from_chatml(EXPECTED_CHATML)
        assert isinstance(result, str)
        assert result == EXPECTED_PROMPT


if __name__ == "__main__":
    unittest.main()
