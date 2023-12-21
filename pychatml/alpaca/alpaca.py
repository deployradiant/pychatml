from typing import List, Dict, Any


def to_chatml(
    alpaca_input: Dict[str, str], treat_instruction_as_system_prompt: bool = False
) -> List[Dict[str, str]]:
    """
    Converts the alpaca input to the ChatML format

    Args:
        alpaca_input (List[Dict[str, str]]): The alpaca input to convert

    Returns:
        List[Dict[str, str]]: The chat interface in ChatML format.
    """

    role_mapping = {
        "instruction": "system" if treat_instruction_as_system_prompt else "user",
        "input": "user",
        "output": "assistant",
    }
    messages = []

    for field in ["instruction", "input", "output"]:
        if field in alpaca_input and len(alpaca_input[field]) > 0:
            messages.append(
                {"role": role_mapping[field], "content": alpaca_input[field].strip()}
            )

    return messages


def from_chatml(messages: List[Dict[str, str]]) -> Dict[str, str]:
    """
    Converts ChatML to llama2

    Args:
        chatml (str): The chat interface in ChatML format.

    Returns:
        Dict[str, str]: The alpaca chat interface.
    """

    response = {
        "instruction": "",
        "input": "",
        "output": "",
    }

    role_mapping = {
        "system": "instruction",
        "user": "input",
        "assistant": "output",
    }

    for message in messages:
        if not message["role"] in role_mapping:
            raise ValueError(
                f"Invalid role {message['role']} in chatml. Expected one of {role_mapping.keys()}"
            )
        if message["role"] == "user" and len(response["instruction"]) == 0:
            response["instruction"] = message["content"].strip()
            continue

        field = role_mapping[message["role"]]

        if len(response[field]) > 0:
            response[field] += "\n"
        response[field] += message["content"].strip()
    return response
