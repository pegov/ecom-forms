from app.template import find_template_name

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

q1 = {
    "user_email1": "test@test.com",
    "user_phone1": "+7 999 888 77 88",
    "user_date_added": "1997-12-03",
    "user_comment": "comment1 asdf",
}

q2 = {
    "user_email2": "test@test.com",
    "user_phone2": "+7 999 888 77 88",
    "user_date_added": "15.08.2003",
    "user_comment": "comment1 asdf",
}

q3 = {"user_email1": "text1", "user_phone2": "1997-12-28"}

q4 = {"asdf": "fdfas"}

qs = [
    (
        q1,
        "Template 1",
    ),
    (
        q2,
        "Template 2",
    ),
    (
        q3,
        None,
    ),
    (
        q4,
        None,
    ),
]


def main():
    templates = [t1, t2]

    for item in qs:
        q, result = item[0], item[1]

        name = find_template_name(templates, q)
        assert name == result


if __name__ == "__main__":
    main()
    print("success")
