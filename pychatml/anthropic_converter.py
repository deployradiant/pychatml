import re
from typing import List, Dict, Any
from anthropic import AI_PROMPT, HUMAN_PROMPT

from pychatml.abstract import AbstractConverter


class Anthropic(AbstractConverter):
    def __init__(self):
        super().__init__(provider="anthropic")

    def to_chatml(self, prompt) -> List[Dict[str, str]]:
        pattern = rf"\n\n(Human:|Assistant:) ([^\n]+)"
        matches = re.findall(pattern, prompt)

        chat_messages = []
        for match in matches:
            role = "user" if match[0] == HUMAN_PROMPT.lstrip() else "assistant"
            content = match[1].strip()
            chat_messages.append({"role": role, "content": content})
        return chat_messages

    def from_chatml(self, messages: List[Dict[str, str]]) -> Any:
        stringified_prompt = ""

        if len(messages) == 0 or messages[0]["role"] != "user":
            stringified_prompt += HUMAN_PROMPT + " \n"

        for message in messages:
            prefix = (
                AI_PROMPT
                if message["role"] in ["system", "assistant"]
                else HUMAN_PROMPT
            )
            stringified_prompt += f"{prefix} {message['content']}\n"
        stringified_prompt += AI_PROMPT

        return stringified_prompt
