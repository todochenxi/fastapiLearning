from typing import Annotated

import uvicorn
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}



if __name__ == "__main__":
    uvicorn.run("Header参数:app", host="127.0.0.1", port=8000)