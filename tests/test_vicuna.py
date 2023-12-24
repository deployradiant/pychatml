import unittest
import pychatml


EXPECTED_PROMPT = """
    You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.
    Knowledge cutoff: 2021-09-01
    Current date: 2023-03-02
    ### Human:
    How are you?
    ### Assistant:
    I am doing well
    ### Human:
    What is the mission of the company OpenAI?
"""

EXPECTED_CHATML = [
    {'role': 'system', 'content': 'You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02'},
    {'role': 'user', 'content': 'How are you?'},
    {'role': 'assistant', 'content': 'I am doing well'},
    {'role': 'user', 'content': 'What is the mission of the company OpenAI?'}
]


class TestVicuna(unittest.TestCase):
    def test_to_chatml(self):
        chatml = pychatml.vicuna.to_chatml(EXPECTED_PROMPT)

        assert isinstance(chatml, list)
        assert len(chatml) > 0
        assert isinstance(chatml[0], dict)
        assert chatml == EXPECTED_CHATML

    def test_from_chatml(self):
        result = pychatml.vicuna.from_chatml(EXPECTED_CHATML)
        assert isinstance(result, str)
        assert result == EXPECTED_PROMPT


if __name__ == "__main__":
    unittest.main()
