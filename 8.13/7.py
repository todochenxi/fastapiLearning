# -*- coding: utf-8 -*-
# @Time    : 2023/8/13 21:07
# @Author  : chenxi
# @FileName: 7.py
# @Software: PyCharm
# from typing import Annotated

from typing_extensions import Annotated
import uvicorn
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    fill_name: Union[str, None] = None


@app.put("/items/{item_id}")
async def update_item(
    # item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    # q: str | None = None,
    # item: Item | None = None,
    # Body() 注解的参数会自动解析为请求体Json
    item_id: int,
    item: Annotated[Item, Body(embed=True)]
):
    results = {"item_id": item_id, "item": item}

    return results


if __name__ == "__main__":
    uvicorn.run("7:app", host="127.0.0.1", port=8000)
