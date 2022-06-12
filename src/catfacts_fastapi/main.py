from typing import Union
import logging

from fastapi import FastAPI
from catfacts_fastapi import utils

logging.basicConfig(level=logging.INFO)

app = FastAPI()
v2 = FastAPI()


@app.on_event("startup")
async def startup_event():
    logging.info("Hello!")


@app.get("/")
async def read_root():
    return utils.read_random()


@v2.get("/")
async def read_random_v2_root():
    return utils.read_random()


@v2.get("/random")
async def read_random_v2_endpoint():
    return utils.read_random()


app.mount("/v2", v2)
