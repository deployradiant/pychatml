import abc
from abc import abstractmethod
from typing import Dict, List, Any


class AbstractConverter(abc.ABC):
    def __init__(self, provider):
        self._provider = provider

    @property
    def provider(self):
        return self._provider

    @abstractmethod
    def to_chatml(self, prompt) -> List[Dict[str, str]]:
        """
        Converts the provider input to the ChatML format

        Args:
            prompt: The provider input to convert

        Returns:
            List[Dict[str, str]]: The chat interface in ChatML format.
        """
        pass

    @abstractmethod
    def from_chatml(self, messages: List[Dict[str, str]]) -> Any:
        pass
