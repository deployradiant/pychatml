from typing import Dict, List

from pychatml.abstract import AbstractConverter


class Alpaca(AbstractConverter):
    def __init__(self, treat_instruction_as_system_prompt: bool = False):
        super().__init__(provider="alpaca")
        self.treat_instruction_as_system_prompt = treat_instruction_as_system_prompt

        self.alpaca_to_openai_mapping = {
            "instruction": "system"
            if self.treat_instruction_as_system_prompt
            else "user",
            "input": "user",
            "output": "assistant",
        }
        self.openai_to_alpaca_mapping = {
            "system": "instruction",
            "user": "input",
            "assistant": "output",
        }

    def to_chatml(self, prompt: Dict[str, str]) -> List[Dict[str, str]]:
        messages = []

        for field in ["instruction", "input", "output"]:
            if field in prompt and len(prompt[field]) > 0:
                messages.append(
                    {
                        "role": self.alpaca_to_openai_mapping[field],
                        "content": prompt[field].strip(),
                    }
                )

        return messages

    def from_chatml(self, messages: List[Dict[str, str]]) -> Dict[str, str]:
        response = {key: "" for key in self.alpaca_to_openai_mapping}

        for message in messages:
            if not message["role"] in self.openai_to_alpaca_mapping:
                raise ValueError(
                    f"Invalid role {message['role']} in chatml. Expected one of {self.openai_to_alpaca_mapping.keys()}"
                )
            if message["role"] == "user" and len(response["instruction"]) == 0:
                response["instruction"] = message["content"].strip()
                continue

            field = self.openai_to_alpaca_mapping[message["role"]]

            if len(response[field]) > 0:
                response[field] += "\n"
            response[field] += message["content"].strip()
        return response
