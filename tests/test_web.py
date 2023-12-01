from fastapi.testclient import TestClient

from app.validator import FieldType
from app.web import (
    ERROR_MESSAGE_EMPTY_FIELD_NAME,
    ERROR_MESSAGE_EMPTY_ITEM,
    ERROR_MESSAGE_INVALID_ITEM,
    ERROR_MESSAGE_NO_DATA,
    get_app,
)
from tests.mocks import MockDatabase

client = TestClient(get_app(MockDatabase()))


def test_get_form_error_no_data():
    response = client.post("/get_form", content="")
    assert response.status_code == 400
    assert response.json().get("detail") == ERROR_MESSAGE_NO_DATA


def test_get_form_error_empty_field_name():
    response = client.post("/get_form", content="fname1=value1&=value2")
    assert response.status_code == 400
    assert response.json().get("detail") == ERROR_MESSAGE_EMPTY_FIELD_NAME


def test_get_form_error_invalid_item_format():
    response = client.post("/get_form", content="fname1=value1&wrong")
    assert response.status_code == 400
    assert response.json().get("detail") == ERROR_MESSAGE_INVALID_ITEM


def test_get_form_error_empty_item():
    response = client.post("/get_form", content="fname1=value1&")
    assert response.status_code == 400
    assert response.json().get("detail") == ERROR_MESSAGE_EMPTY_ITEM


def test_get_form_found():
    response = client.post(
        "/get_form",
        content="username=user&email=test@test.com&phone=+79998887766&date_added=10.10.2020",
    )
    assert response.status_code == 200
    assert response.json().get("name") == "Sign up"


def test_get_form_not_found():
    response = client.post(
        "/get_form",
        content="user=user1&desc=desc1&new_email=test@test.com&date_updated=2020-10-10",
    )
    assert response.status_code == 200
    data = response.json()
    assert data.get("user") == FieldType.TEXT
    assert data.get("desc") == FieldType.TEXT
    assert data.get("new_email") == FieldType.EMAIL
    assert data.get("date_updated") == FieldType.DATE
