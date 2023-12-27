import re
from typing import List, Dict


def to_chatml(prompt: str) -> List[Dict[str, str]]:
    """
    Converts the vicuna interface to the ChatML format

    Vicuna interface from https://huggingface.co/junelee/wizard-vicuna-13b/discussions/1

    Args:
        prompt (string): The prompt to convert

    Returns:
        List[Dict[str, str]]: The chat interface in ChatML format.
    """
    P_EITHER = r'USER: |ASSISTANT: '
    B_HUMAN, B_ASSISTANT = "USER: ", "ASSISTANT: "
    SEPARATOR = "</s>"

    prompt = prompt.strip()

    frmt_regs = re.finditer(P_EITHER, prompt)
    frmt_regs = [m for m in frmt_regs]
    messages = []

    # Use finditer() to find all occurrences along with their indices
    for i in range(len(frmt_regs)):
        match = frmt_regs[i]
        frmt_start_i = match.start()
        frmt_end_i = match.end()
        if i == 0 and frmt_start_i != 0:
            msg = prompt[:frmt_start_i].strip()
            messages.append(
                {
                    "role": "system",
                    "content": msg
                }
            )

        msg_end_i = len(prompt)
        if i < len(frmt_regs) - 1:
            nxt = frmt_regs[i+1]
            msg_end_i = nxt.start()

        msg = prompt[frmt_end_i: msg_end_i].strip()
        if SEPARATOR == msg[-len(SEPARATOR):]:
            msg = msg[:-len(SEPARATOR)]
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
    Converts ChatML to vicuna v1.1

    Args:
        chatml (str): The chat interface in ChatML format.

    Returns:
        str: The converted prompt.
    """

    B_HUMAN, B_ASSISTANT = "USER:", "ASSISTANT:"
    SEPARATOR = "</s>"

    chat_history = []
    temp = []
    for m in messages:
        if m['role'] == 'user':
            m['content'] = " ".join([B_HUMAN, m['content']])
        if m['role'] == 'assistant':
            m['content'] = " ".join([B_ASSISTANT, m['content']])
        temp.append(m['content'])
        if m['role'] == 'assistant':
            chat_history.append(" ".join(temp))
            temp = []
    if messages[-1]['role'] == 'assistant':
        chat_history.append("")
    return SEPARATOR.join(chat_history)


if __name__ == "__main__":
    txt = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: What is ChatGPT? ASSISTANT: ChatGPT is an advanced language model developed by OpenAI. It's designed to understand and generate natural language, so it can converse with users, answer questions, and even assist with various tasks.</s>USER: So, it's like a super-advanced chatbot? ASSISTANT: Yes, but it can engage in broader conversations and more complex reasoning.</s>"
    print(txt)
    print()
    chat = to_chatml(txt)
    print(chat)
    print()
    revert = from_chatml(chat)
    print(revert)
