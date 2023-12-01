import os
from typing import Dict, Optional

import pytest
from tinydb import TinyDB

from app.db import TinyDBDatabase
from app.validator import FieldType

tdb = TinyDB("test.json")
data = [
    {
        "name": "Sign up",
        "username": FieldType.TEXT,
        "email": FieldType.EMAIL,
        "phone": FieldType.PHONE,
        "date_added": FieldType.DATE,
    },
    {
        "name": "Order",
        "order_id": FieldType.TEXT,
        "receiver_email": FieldType.EMAIL,
        "receiver_phone": FieldType.PHONE,
        "receiver_address": FieldType.TEXT,
        "date_registered": FieldType.DATE,
        "date_completed": FieldType.DATE,
    },
]
tdb.insert_multiple(data)
db = TinyDBDatabase(tdb)


@pytest.fixture(scope="session", autouse=True)
def cleanup():
    yield
    try:
        os.remove("test.json")
    except Exception:
        pass


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (
            {
                "username": FieldType.TEXT,
                "email": FieldType.EMAIL,
                "phone": FieldType.PHONE,
                "date_added": FieldType.DATE,
            },
            "Sign up",
        ),
        (
            {
                "order_id": FieldType.TEXT,
                "receiver_email": FieldType.EMAIL,
                "receiver_phone": FieldType.PHONE,
                "receiver_address": FieldType.TEXT,
                "date_registered": FieldType.DATE,
                "date_completed": FieldType.DATE,
                "score": FieldType.TEXT,
            },
            "Order",
        ),
        (
            {
                "": FieldType.TEXT,
                "sender_email": FieldType.EMAIL,
                "sender_phone": FieldType.PHONE,
                "date_added": FieldType.DATE,
                "comment": FieldType.TEXT,
            },
            None,
        ),
    ],
)
def test_get_template_name(input_data: Dict[str, str], expected: Optional[str]):
    assert db.get_template_name(input_data) == expected
