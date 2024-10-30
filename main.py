from fastapi import FastAPI, Query
from datetime import date
from typing import Optional
from starlette.middleware.cors import CORSMiddleware
from controller.Controller import Controller


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


@app.get("/api/get-data")
async def get_data(date: date = Query(...)):

    controller = Controller()
    data = controller.get_data(str(date.year), str(date.month))
    return data


@app.get("/api/get-range")
async def get_range(
    startDate: Optional[date] = Query(None),
    endDate: Optional[date] = Query(None)
):
    controller = Controller()
    data = controller.get_range(str(startDate), str(endDate))
    return data
