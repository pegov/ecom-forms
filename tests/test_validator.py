import pytest

from app.validator import FieldType, validate


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (
            "10.10.2020",
            FieldType.DATE,
        ),
        (
            "2020-10-10",
            FieldType.DATE,
        ),
        (
            "10.30.2020",  # MM.DD.YYYY
            FieldType.TEXT,
        ),
        (
            "30-10-2020",  # DD-MM-YYYY
            FieldType.TEXT,
        ),
    ],
)
def test_validate_date(input_data: str, expected: int):
    assert validate(input_data) == expected


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (
            "+7 999 888 77 66",
            FieldType.PHONE,
        ),
        (
            "+79998887766",
            FieldType.PHONE,
        ),
        (
            "+799988877661",  # 11 numbers after +7
            FieldType.TEXT,
        ),
        (
            "+7999888776",  # 9 numbers after +7
            FieldType.TEXT,
        ),
        (
            "+8999888776",  # +8
            FieldType.TEXT,
        ),
    ],
)
def test_validate_phone(input_data: str, expected: int):
    assert validate(input_data) == expected


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (
            "test@test.com",
            FieldType.EMAIL,
        ),
        (
            "test@test.com",
            FieldType.EMAIL,
        ),
        (
            "test@test",
            FieldType.TEXT,
        ),
        (
            "@test.com",
            FieldType.TEXT,
        ),
    ],
)
def test_validate_email(input_data: str, expected: int):
    assert validate(input_data) == expected
