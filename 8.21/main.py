from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, List


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    # tags: list = []   # 未声明类型
    tags: set[str] = set()


@app.put("/items/{item_id")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

