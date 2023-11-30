from tinydb import TinyDB

from app.db import TinyDBDatabase
from app.web import get_app


db = TinyDBDatabase(TinyDB("db.json"))
app = get_app(db)
