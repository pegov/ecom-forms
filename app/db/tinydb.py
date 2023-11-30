from typing import Dict, Optional

from tinydb import TinyDB, Query

from app.db.abc import AbstractDatabase


class TinyDBDatabase(AbstractDatabase):
    _db: TinyDB

    def __init__(self, db: TinyDB):
        self._db = db

    def get_template_name(self, fields: Dict[str, str]) -> Optional[str]:
        templates = self._db.search(Query().fragment(fields))
        if len(templates) == 0:
            return None

        return max(templates, key=lambda x: len(x)).get("name")
