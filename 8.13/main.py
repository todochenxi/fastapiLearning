# -*- coding: utf-8 -*-
# @Time    : 2023/8/13 15:47
# @Author  : chenxi
# @FileName: main.py
# @Software: PyCharm

from fastapi import FastAPI
import uvicorn
from enum import Enum
from typing import Union
app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # 比较枚举成员
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    # model_name 是一个枚举成员，.value 获取枚举值
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    # 返回枚举成员
    return {"model_name": model_name, "message": "Have some residuals"}


# :path 说明该参数应匹配任意的路径，如：/homt/text.txt
@app.get("/files/{file_path: path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# 查询字符是键值对的集合，这些键值对位于url的？之后，并以&符号分割
@app.get("/items/")
async def read_item(skip: int=0, limit: int=10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# 多个路径和查询参数
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# 请求体
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
