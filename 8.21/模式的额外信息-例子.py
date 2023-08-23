import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Union, Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    # 使用Config和schema_extra为pydantic模型声明一个示例
    model_config = {
        "json_schema_extra": {"examples": [
            {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 34.5,
                "tax": 3.2,
            }
        ]}
    }


class Item2(BaseModel):
    # Field的附加参数
    """
    在Field，Path，Query，Body和其他之后将会看到的工厂函数，可以为JSON模式声明额外信息，也可以通过给
    工厂函数传递其他的任意参数来给JSON模式声明额外信息，比如增加example
    """
    name: str = Field(examples=["Foo"])
    description: Union[str, None] = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: Union[float, None] = Field(default=None, examples=[3.2])


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, item2: Item2):
    results = {"item_id": item_id, "item": item, "item2": item2}
    return results


class Item3(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/body/{item_id}")
async def body_item(
        item_id: int,
        item: Annotated[
            Item3,
            Body(
                examples=[
                    {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 34.5,
                        "tax": 3.2,
                    }
                ]
            )
        ]
):
    """
    可以通过传递额外信息给Field同样的方式操作Path，Query，Body等，比如可以将请求体的example传递给Body
    """
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    uvicorn.run("模式的额外信息-例子:app", host="127.0.0.1", port=8000)
