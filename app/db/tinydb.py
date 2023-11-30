from typing import Dict, Iterable

from tinydb import TinyDB

from app.db.abc import AbstractDatabase


class TinyDBDatabase(AbstractDatabase):
    _db: TinyDB

    def __init__(self, db: TinyDB):
        self._db = db

    def get_templates(self) -> Iterable[Dict[str, str]]:
        return self._db
