import asyncio
import sys

import httpx

client = httpx.AsyncClient()

# forms are in db.json or in scripts/populate.py

r1_1 = {
    "user_id": "1",
    "user_name": "user1",
    "user_email": "user@test.com",
    "user_phone": "+79998887766",
    "date_created": "10.10.2020",
    "last_login": "2021-10-09",
    "comment": "other",
}

r1_2 = {
    "user_id": "1",
    "user_name": "user1",
    "user_email": "user@test.com",
    "user_phone": "+79998887766",
    "date_created": "10.10.2020",
    "last_login": "2021-10-09",
    "comment": "other",
    "address": "Moscow",
    "payment_method": "online",
    "status": "ok",
}

r1_3 = {
    "user_id": "1",
    "user_name": "user1",
    "user_email": "user@test.com",
    "user_phonenumber": "+79998887766",  # ! phonenumber
    "date_created": "10.10.2020",
    "last_login": "2021-10-09",
    "comment": "other",
    "address": "Moscow",
    "payment_method": "online",
    "status": "ok",
}

r2_1 = {
    "email": "test@test.com",
    "username": "user1",
    "password1": "hunter2",
    "password2": "hunter2",
}
r2_2 = {
    "email": "test@test.com",
    "username": "user1",
    "password1": "hunter2",
}

r3 = {
    "order_id": "10",
    "user_id": "1",
    "user_email": "test@test.com",
    "user_phone": "+71112223344",
    "order_address": "text",
    "date_registered": "05.05.2020",
    "date_completed": "08.05.2020",
}

r4 = {
    "event_id": "save",
    "dispatcher_id": "1",
    "dispatcher_email": "test@test.com",
    "dispatcher_phone": "+7 999 888 77 66",
    "date_created": "2015-05-05",
}


def serialize(d: dict) -> str:
    s = []
    for key, value in d.items():
        s.append(f"{key}={value}")

    return "&".join(s)


async def main():
    if len(sys.argv) < 2:
        print("USAGE: python scripts/requests.py http://127.0.0.1:8080/get_form")
        return

    url = sys.argv[1]

    for i, r in enumerate([r1_1, r1_2, r1_3, r2_1, r2_2, r3, r4]):
        print(f"REQUEST ({i}):")
        print(r)
        res = await client.post(url, content=serialize(r))
        if res.status_code != 200:
            print("ERROR", res.status_code)
            return

        print(f"RESPONSE ({i}):")
        print(res.json())


asyncio.run(main())
