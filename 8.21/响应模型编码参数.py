from typing import List, Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


items2 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude={"tax"})
async def read_item(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/name",
         response_model=Item,
         response_model_include={"name", "description"},)
async def read_item_name(item_id: str):
    return items[item_id]


if __name__ == "__main__":
    uvicorn.run("响应模型编码参数:app", host="127.0.0.1", port=8000)