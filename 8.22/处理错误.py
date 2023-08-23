import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404,
                            detail="Item not found",
                            headers={"X-Error": "There goes my error"},)
    return {"item": items[item_id]}


if __name__ == "__main__":
    uvicorn.run("处理错误:app", host="127.0.0.1", port=8000)