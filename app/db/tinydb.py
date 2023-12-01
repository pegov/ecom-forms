from typing import Dict, Optional

from tinydb import TinyDB

from app.db.abc import AbstractDatabase


class TinyDBDatabase(AbstractDatabase):
    _db: TinyDB

    def __init__(self, db: TinyDB):
        self._db = db

    def get_template_name(self, fields: Dict[str, str]) -> Optional[str]:
        candidate_name = ""
        candidate_len = 0
        for template in self._db:
            template_len = len(template) - 1

            if template_len > len(fields):
                continue

            name = template.pop("name")
            if (
                set(template.items()).issubset(set(fields.items()))
                and template_len > candidate_len
            ):
                candidate_name = name
                candidate_len = template_len

        if candidate_len == 0:
            return None

        return candidate_name
