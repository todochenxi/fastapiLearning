from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Union

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    # images: Union[Image, None] = None
    images: Union[list[Image], None] = None  # 带有一组子模型的属性，也可以继续深度嵌套


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/images/multiple")
async def create_multiple_images(images: list[Image]):  # 纯列表请求体
    return images


# 任意dict构成的请求体
@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
"""
json仅支持str作为键，但是pydantic具有自动转换数据的功能，这意味着，即使api客户端智能将字符串作为
键发送，只要这些字符串内容仅包含整数，pydantic就会对其进行转换并进行校验。
"""