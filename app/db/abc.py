from abc import ABC, abstractmethod
from typing import Dict, Optional


class AbstractDatabase(ABC):
    @abstractmethod
    def get_template_name(self, fields: Dict[str, str]) -> Optional[str]:
        ...
