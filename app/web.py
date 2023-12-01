from typing import Annotated

from fastapi import FastAPI, Request, Depends, HTTPException

from app.db import AbstractDatabase
from app.validator import validate

ERROR_MESSAGE_EMPTY_FIELD_NAME = "field name is empty"
ERROR_MESSAGE_NO_DATA = "no data"

app = FastAPI()


def get_db(request: Request) -> AbstractDatabase:
    db: AbstractDatabase = request.app.state.db
    return db


DatabaseDep = Annotated[AbstractDatabase, Depends(get_db)]


# f_name1=value1&f_name2=value2
# I assume it is raw body, not JSON.
# So we need to split raw body by '&' and items by '=' to get data.
@app.post("/get_form")
async def get_form(request: Request, db: DatabaseDep):
    body = (await request.body()).decode()
    fields = {}
    for item in body.split("&"):
        key, value = item.split("=", 1)
        if len(key) == 0:
            raise HTTPException(400, detail=ERROR_MESSAGE_EMPTY_FIELD_NAME)

        fields.update({key: validate(value)})

    if len(fields) == 0:
        raise HTTPException(400, detail=ERROR_MESSAGE_NO_DATA)

    name = db.get_template_name(fields)

    if name is not None:
        return {"name": name}

    return fields


def get_app(db: AbstractDatabase) -> FastAPI:
    app.state.db = db
    return app
