from abc import ABC, abstractmethod
from typing import Dict, Iterable


class AbstractDatabase(ABC):
    @abstractmethod
    def get_templates(self) -> Iterable[Dict[str, str]]:
        ...
