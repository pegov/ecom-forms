import re
from datetime import datetime

# we assume only +7 ... are valid with spaces between or without
PHONE_REGEX = re.compile(r"^\+7\s?[0-9]{3}\s?[0-9]{3}\s?[0-9]{2}\s?[0-9]{2}$")

# for the MOST correct one go to stackoverflow
EMAIL_REGEX = re.compile(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,4}$")

# DD.MM.YYYY
DATE_TEMPLATE_1 = "%d.%m.%Y"
# YYYY-MM-DD
DATE_TEMPLATE_2 = "%Y-%m-%d"

DATE_TEMPLATES = [
    DATE_TEMPLATE_1,
    DATE_TEMPLATE_2,
]


class FieldType:
    DATE = "date"
    PHONE = "phone"
    EMAIL = "email"
    TEXT = "text"


def _validate_phone(s: str) -> bool:
    return re.match(PHONE_REGEX, s) is not None


def _validate_email(s: str) -> bool:
    return re.match(EMAIL_REGEX, s) is not None


def _validate_date(s: str) -> bool:
    for t in DATE_TEMPLATES:
        try:
            datetime.strptime(s, t)
            return True
        except ValueError:
            pass

    return False


VALIDATORS = {
    _validate_date: FieldType.DATE,
    _validate_phone: FieldType.PHONE,
    _validate_email: FieldType.EMAIL,
}


def validate(s: str) -> str:
    for validator, type_ in VALIDATORS.items():
        if validator(s):
            return type_

    return FieldType.TEXT
