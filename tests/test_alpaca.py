import unittest
import pychatml


EXPECTED_INPUT = {
    "instruction": "Evaluate this sentence for spelling and grammar mistakes",
    "input": "He finnished his meal and left the resturant",
    "output": "He finished his meal and left the restaurant.",
}

EXPECTED_CHATML_WITH_SYSTEM = [
    {
        "role": "system",
        "content": "Evaluate this sentence for spelling and grammar mistakes",
    },
    {"role": "user", "content": "He finnished his meal and left the resturant"},
    {"role": "assistant", "content": "He finished his meal and left the restaurant."},
]

EXPECTED_CHATML_WITHOUT_SYSTEM = [
    {
        "role": "user",
        "content": "Evaluate this sentence for spelling and grammar mistakes",
    },
    {"role": "user", "content": "He finnished his meal and left the resturant"},
    {"role": "assistant", "content": "He finished his meal and left the restaurant."},
]


class TestAlpaca(unittest.TestCase):
    def test_to_chatml(self):
        chatml = pychatml.alpaca.to_chatml(EXPECTED_INPUT, True)
        assert isinstance(chatml, list)
        assert len(chatml) > 0
        assert isinstance(chatml[0], dict)
        assert chatml == EXPECTED_CHATML_WITH_SYSTEM

        chatml = pychatml.alpaca.to_chatml(EXPECTED_INPUT)
        assert isinstance(chatml, list)
        assert len(chatml) > 0
        assert isinstance(chatml[0], dict)
        assert chatml == EXPECTED_CHATML_WITHOUT_SYSTEM

    def test_from_chatml(self):
        result = pychatml.alpaca.from_chatml(EXPECTED_CHATML_WITH_SYSTEM)
        assert isinstance(result, dict)
        assert result == EXPECTED_INPUT

        result = pychatml.alpaca.from_chatml(EXPECTED_CHATML_WITHOUT_SYSTEM)
        assert isinstance(result, dict)
        assert result == EXPECTED_INPUT


if __name__ == "__main__":
    unittest.main()
