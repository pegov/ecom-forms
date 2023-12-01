from typing import Annotated

from fastapi import FastAPI, Request, Depends, HTTPException

from app.db import AbstractDatabase
from app.validator import validate

ERROR_MESSAGE_EMPTY_FIELD_NAME = "empty field name"  # "=value1"
ERROR_MESSAGE_EMPTY_ITEM = "empty item"  # "fname1=value1&"
ERROR_MESSAGE_INVALID_ITEM = "invalid item"  # "fname1=value1&wrong"
ERROR_MESSAGE_NO_DATA = "no data"  # ""

app = FastAPI()


def get_db(request: Request) -> AbstractDatabase:
    db: AbstractDatabase = request.app.state.db
    return db


DatabaseDep = Annotated[AbstractDatabase, Depends(get_db)]


# f_name1=value1&f_name2=value2
# I assume it is raw body, not JSON.
# So we need to split raw body by '&' and items by '=' to get the data.
@app.post("/get_form")
async def get_form(request: Request, db: DatabaseDep):
    body = (await request.body()).decode()
    fields = {}
    items = body.split("&")
    if len(items) == 1 and not items[0]:
        raise HTTPException(400, detail=ERROR_MESSAGE_NO_DATA)

    for item in items:
        if not item:
            raise HTTPException(400, detail=ERROR_MESSAGE_EMPTY_ITEM)

        pair = item.split("=", 1)
        if len(pair) < 2:
            raise HTTPException(400, detail=ERROR_MESSAGE_INVALID_ITEM)

        key, value = pair
        if not key:
            raise HTTPException(400, detail=ERROR_MESSAGE_EMPTY_FIELD_NAME)

        fields.update({key: validate(value)})

    name = db.get_template_name(fields)

    if name is not None:
        return {"name": name}

    return fields


def get_app(db: AbstractDatabase) -> FastAPI:
    app.state.db = db
    return app
