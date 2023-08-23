from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

import uvicorn
from fastapi import FastAPI, Body

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
        item_id: int,
        start_datetime: Annotated[datetime | None, Body()] = None,  # 完整的时间
        end_datetime: Annotated[datetime | None, Body()] = None,  # 时分秒
        repeat_at: Annotated[time | None, Body()] = None,  # 时分秒
        process_after: Annotated[timedelta | None, Body()] = None,  # 总秒数
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


if __name__ == "__main__":
    uvicorn.run("额外数据类型:app", host="127.0.0.1", port=8000)