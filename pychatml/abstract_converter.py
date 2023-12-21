from abc import ABC, abstractmethod
from typing import Any, Dict, List


class ChatMLConverter(ABC):
    
    @abstractmethod
    def to_chatml(self, chat_interface: Any) -> List[Dict[str, str]]:
        """
        Converts a chat interface to the ChatML format.
        
        Args:
            chat_interface (dict): The chat interface to convert.
        
        Returns:
            str: The chat interface in ChatML format.
        """
        # TODO: Implement the conversion logic
        pass

    @abstractmethod
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