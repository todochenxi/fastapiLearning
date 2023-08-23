from typing import Set, Union

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@app.post("/items/",
          response_model=Item,
          # status_code=status.HTTP_201_CREATED,
          tags=["items"],
          summary="Create an item",  # 总结
          response_description="The created item",  # 只用于描述响应，description一般描述路径操作
          # 描述 和 文档字符串不能同时使用
          #description="Create an item with all the information, name, description, price, tax and a set of unique tags"
)
async def create_item(item: Item):
    """
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag string for this item
    """
    return item


@app.get("/items/", tags=["items"])  # tags参数的值是由str组成的list(一般只有一个str)， tags用于为路径操作添加标签
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


@app.get("/elements/", tags=["items"], deprecated=True)  # 弃用路径操作
async def read_elements():
    return [{"item_id": "Foo"}]


if __name__ == "__main__":
    uvicorn.run("路径操作配置:app", host="127.0.0.1", port=8000)
