import re
from typing import List, Dict


def to_chatml(vicuna_prompt: str) -> List[Dict[str, str]]:
    """
    Converts the vicuna interface to the ChatML format

    Vicuna interface from https://huggingface.co/junelee/wizard-vicuna-13b/discussions/1

    ### Human:
    <Question>
    ### Assistant:
    <Answer>

    Args:
        vicuna_prompt (string): The prompt to convert

    Returns:
        List[Dict[str, str]]: The chat interface in ChatML format.
    """
    P_EITHER = r'### Human:\n|### Assistant:\n'
    B_HUMAN, B_ASSISTANT = "### Human:\n", "### Assistant:\n"

    vicuna_prompt = vicuna_prompt.strip()

    frmt_regs = re.finditer(P_EITHER, vicuna_prompt)
    frmt_regs = [m for m in frmt_regs]
    messages = []

    # Use finditer() to find all occurrences along with their indices
    for i in range(len(frmt_regs)):
        match = frmt_regs[i]
        frmt_start_i = match.start()
        frmt_end_i = match.end()
        if i == 0 and frmt_start_i != 0:
            messages.append(
                {
                    "role": "system",
                    "content": vicuna_prompt[:frmt_start_i].strip()
                }
            )

        msg_end_i = len(vicuna_prompt)
        if i < len(frmt_regs) - 1:
            nxt = frmt_regs[i+1]
            msg_end_i = nxt.start()

        msg = vicuna_prompt[frmt_end_i: msg_end_i].strip()
        role = "assistant" if match.group() != B_HUMAN else 'user'
        messages.append(
            {
                "role": role,
                "content": msg
            }
        )

    return messages


def from_chatml(messages: List[Dict[str, str]]) -> str:
    """
    Converts ChatML to llama2

    Args:
        chatml (str): The chat interface in ChatML format.

    Returns:
        str: The converted prompt.
    """

    B_HUMAN, B_ASSISTANT = "### Human:\n", "### Assistant:\n"

    system_messages = []
    chat_messages = []
    for message in messages:
        if message["role"] == "system":
            system_messages.append(message["content"].strip())
            continue

        if len(chat_messages) > 0 and chat_messages[-1]["role"] == message["role"]:
            chat_messages[-1]["content"] += " " + message["content"].strip()
        else:
            chat_messages.append(message.copy())

    system_prompt = " ".join(system_messages)

    chat_history = [system_prompt]
    for m in chat_messages:
        b = B_HUMAN if m['role'] == 'user' else B_ASSISTANT
        chat_history.append("".join([b, m['content']]))
    return "\n".join(chat_history)
