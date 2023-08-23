from typing import List, Union

import uvicorn
from fastapi import FastAPI
from  fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{items_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


# 用patch进行部分更新数据的警告，即只发送要更新的数据，其余数据保持不变
# 使用pydantic的excluede_unset参数，更细那部分数据时，可以在pydantic模型的.dict()中使用exclude_unset
# 参数，比如，item.dict(exclude_unset=True)
# 这段代码生成的dict只包含创建item模型时显示设置的数据，而不包含默认值。
# 然后再用它生成一个只含已设置（在请求中所发送）数据，且省略了默认值的dict：
@app.patch("/items_patch/{item_id}", response_model=Item)
async def update_item_with_patch(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    update_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(update_item)
    return update_item


if __name__ == "__main__":
    uvicorn.run("请求体-更新数据:app", host="127.0.0.1", port=8000)

