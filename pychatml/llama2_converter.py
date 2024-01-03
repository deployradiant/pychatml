import re
from typing import List, Dict, Any

from pychatml.abstract import AbstractConverter


class Llama2(AbstractConverter):
    def __init__(self):
        super().__init__(provider="llama2")

    def to_chatml(self, prompt) -> List[Dict[str, str]]:
        messages = []

        for instruction in prompt.split("[INST] "):
            system_message = re.search(
                r"<<SYS>>\n((.|\n)*)\n<</SYS>>\n\n", instruction)
            if system_message:
                messages.append(
                    {"role": "system", "content": system_message.group(1)})
                instruction = instruction.replace(system_message.group(0), "")

            user_message = re.search(r"(.*?) \[\/INST\]", instruction)
            if user_message:
                messages.append(
                    {"role": "user", "content": user_message.group(1)})
                instruction = instruction.replace(user_message.group(0), "")

            assistant_message = re.search(r" (.*?) \n", instruction)
            if assistant_message:
                messages.append(
                    {"role": "assistant",
                        "content": assistant_message.group(1)}
                )

        return messages

    def from_chatml(self, messages: List[Dict[str, str]]) -> Any:
        # taken from https://github.com/facebookresearch/llama/blob/82ce861078ce1d2a1ac17db15bda3604c684ccbe/llama/generation.py#L212
        B_INST, E_INST = "[INST]", "[/INST]"
        B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

        # LLama2 has a strict format where it expects a system prompt and then alternating user and assistant messages
        system_messages = []
        chat_messages = []
        for message in messages:
            if message["role"] == "system":
                system_messages.append(message["content"].strip())
                continue

            if len(chat_messages) > 0 and chat_messages[-1]["role"] == message["role"]:
                chat_messages[-1]["content"] += " " + \
                    message["content"].strip()
            else:
                chat_messages.append(message.copy())

        system_prompt = " ".join(system_messages)

        if len(chat_messages) > 0:
            # llama2 needs the first message to be a user message
            # based on https://github.com/facebookresearch/llama/blob/82ce861078ce1d2a1ac17db15bda3604c684ccbe/llama/generation.py#L224
            if chat_messages[0]["role"] != "user":
                chat_messages.insert(0, {"role": "user", "content": ""})

            chat_messages[0][
                "content"
            ] = f"{B_SYS}{system_prompt}{E_SYS}{chat_messages[0]['content']}"
        else:
            chat_messages.append(
                {"role": "user", "content": f"{B_SYS}{system_prompt}{E_SYS}"}
            )

        full_prompt = ""
        for prompt, answer in zip(
            chat_messages[::2],
            chat_messages[1::2],
        ):
            full_prompt += f"{B_INST} {(prompt['content']).strip()} {E_INST} {(answer['content']).strip()} \n"
        full_prompt += f"{B_INST} {(chat_messages[-1]['content']).strip()} {E_INST}"
        return full_prompt
