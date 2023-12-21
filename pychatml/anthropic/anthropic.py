from typing import List, Dict
import re

from anthropic import AI_PROMPT, HUMAN_PROMPT


def to_chatml(prompt: str) -> List[Dict[str, str]]:
    """
    Converts the anthropic interface to the ChatML format (also used by Anthropic)

    Args:
        chat_interface (str): The prompt to convert.

    Returns:
        List[Dict[str, str]]: The chat interface in ChatML format.
    """

    # TODO(@nkulkarni): figure out why the fmtstring doesn't work in the regex
    # pattern = rf"\n\n({{HUMAN_PROMPT}}|{{AI_PROMPT}}:) ([^\n]+)"
    pattern = rf"\n\n(Human:|Assistant:) ([^\n]+)"
    matches = re.findall(pattern, prompt)

    chat_messages = []
    for match in matches:
        role = "user" if match[0] == HUMAN_PROMPT.lstrip() else "assistant"
        content = match[1].strip()
        chat_messages.append({"role": role, "content": content})
    return chat_messages


def from_chatml(chatml: List[Dict[str, str]]) -> str:
    """
    Converts a chat interface from the ChatML format.

    Args:
        chatml (str): The chat interface in ChatML format.

    Returns:
        str: The converted prompt.
    """

    stringified_prompt = ""
    if len(chatml) == 0 or chatml[0]["role"] != "user":
        stringified_prompt += HUMAN_PROMPT + " \n"

    for message in chatml:
        prefix = (
            AI_PROMPT if message["role"] in ["system", "assistant"] else HUMAN_PROMPT
        )
        stringified_prompt += f"{prefix} {message['content']}\n"
    stringified_prompt += AI_PROMPT

    return stringified_prompt
