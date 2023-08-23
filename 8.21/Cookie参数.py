from typing import Annotated

import uvicorn
from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}


if __name__ == "__main__":
    uvicorn.run("Cookie参数:app", host="127.0.0.1", port=8000)
