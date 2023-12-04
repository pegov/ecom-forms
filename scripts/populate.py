from tinydb import TinyDB

t1_1 = {
    "name": "user_form_1",
    "user_id": "text",
    "user_name": "text",
    "user_email": "email",
    "user_phone": "phone",
    "date_created": "date",
    "last_login": "date",
    "comment": "text",
}

t1_2 = {
    "name": "user_form_2",
    "user_id": "text",
    "user_name": "text",
    "user_email": "email",
    "user_phone": "phone",
    "date_created": "date",
    "last_login": "date",
    "comment": "text",
    "address": "text",
    "payment_method": "text",
}

t2 = {
    "name": "signup",
    "email": "email",
    "username": "text",
    "password1": "text",
    "password2": "text",
}

t3 = {
    "name": "order",
    "order_id": "text",
    "user_id": "text",
    "user_email": "email",
    "user_phone": "phone",
    "order_address": "text",
    "date_registered": "date",
    "date_completed": "date",
}

t4 = {
    "name": "event",
    "event_id": "text",
    "dispatcher_id": "text",
    "dispatcher_email": "email",
    "dispatcher_phone": "phone",
    "date_created": "date",
}


db = TinyDB("db.json")
db.truncate()
db.insert(t1_1)
db.insert(t1_2)
db.insert(t2)
db.insert(t3)
db.insert(t4)
