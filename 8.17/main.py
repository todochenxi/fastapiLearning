from typing import Annotated, Union

import uvicorn
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    result = {"item_id": item_id, "item": item}
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)