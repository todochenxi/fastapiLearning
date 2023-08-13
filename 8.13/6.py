# -*- coding: utf-8 -*-
# @Time    : 2023/8/13 20:10
# @Author  : chenxi
# @FileName: 6.py
# @Software: PyCharm

from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{iten_id")
async def read_items(
        # Annotated[类型，注解1，注解2，...] 为类型添加注解/元数据
        item_id: Annotated[int, Path(title="The Id of the item to get")],
        q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    uvicorn.run("6:app", host="127.0.0.1", port=8000)