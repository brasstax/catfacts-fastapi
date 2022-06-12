from typing import Union
import logging
from os.path import exists
import sys

from fastapi import FastAPI
from catfacts_fastapi import utils
from databases import Database

logging.basicConfig(level=logging.INFO)
database_filename = "catfacts.db"
database = Database(f"sqlite:///{database_filename}")

app = FastAPI()
v2 = FastAPI()


@app.on_event("startup")
async def startup_event():
    if not exists(database_filename):
        logging.critical("catfacts.db does not exist in the working directory.")
        logging.critical("Please run `init-catfacts` first.")
        sys.exit(1)
    await database.connect()


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