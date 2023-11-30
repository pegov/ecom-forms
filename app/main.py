from app.web import get_app

t1 = {
    "name": "Template 1",
    "user_email1": "email",
    "user_phone1": "phone",
}

t2 = {
    "name": "Template 2",
    "user_email2": "email",
    "user_phone2": "phone",
    "user_date_added": "date",
    "user_comment": "text",
}

templates = [t1, t2]

app = get_app(templates)
