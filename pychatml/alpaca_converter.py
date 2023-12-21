from pychatml.chatml.abstract_converter import ChatMLConverter
from typing import List, Dict, Any


class AlpacaConverter(ChatMLConverter):
    def to_chatml(self, chat_interface) -> List[Dict[str, str]]:
        """
        Converts a chat interface to the ChatML format.

        Args:
            chat_interface (dict): The chat interface to convert.

        Returns:
            str: The chat interface in ChatML format.
        """
        # TODO: Implement the conversion logic

        pass

    def from_chatml(self, chatml: List[Dict[str, str]]) -> Any:
        """
        Converts a chat interface from the ChatML format.

        Args:
            chatml (str): The chat interface in ChatML format.

        Returns:
            dict: The converted chat interface.
        """
        # TODO: Implement the conversion logic
        pass
