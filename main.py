from typing import Union
from datetime import date
from controller.Controller import Controller
from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/get-data")
async def get_data(date: date = Query(...)):

    controller = Controller()
    data = controller.get_data(str(date.year), str(date.month))
    return data

    