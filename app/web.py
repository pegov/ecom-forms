from typing import Iterable, Dict, Annotated

from fastapi import FastAPI, Request, Depends, HTTPException

from app.db import AbstractDatabase
from app.template import find_template_name
from app.validator import validate

app = FastAPI()


def get_templates(request: Request) -> Iterable[Dict[str, str]]:
    db: AbstractDatabase = request.app.state.db
    return db.get_templates()


TemplatesDep = Annotated[Iterable[Dict[str, str]], Depends(get_templates)]


# f_name1=value1&f_name2=value2
# I assume it is raw body, not JSON.
# So we need to split raw body by '&' and items by '=' to get data.
@app.post("/get_form")
async def get_form(request: Request, templates: TemplatesDep):
    body = (await request.body()).decode()
    items = {}
    for item in body.split("&"):
        key, value = item.split("=", 1)
        if len(key) == 0:
            raise HTTPException(400, detail="field name is empty")

        items.update({key: value})

    if len(items) == 0:
        raise HTTPException(400, detail="no data")

    name = find_template_name(templates, items)

    if name is not None:
        return {"name": name}

    res = {}
    for key, value in items.items():
        type_ = validate(value)
        res.update({key: type_})

    return res


def get_app(db: AbstractDatabase) -> FastAPI:
    app.state.db = db
    return app
