import abc
from abc import abstractmethod
from typing import Dict, List, Any


class ChatMLConverter(abc.ABC):
    def __init__(self, provider):
        self._provider = provider

    @property
    def provider(self):
        return self._provider

    @abstractmethod
    def to_chatml(self, prompt) -> List[Dict[str, str]]:
        pass

    @abstractmethod
    def from_chatml(self, messages: List[Dict[str, str]]) -> Any:
        pass
