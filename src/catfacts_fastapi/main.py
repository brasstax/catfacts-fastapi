from typing import Union, Dict
import logging
from os.path import exists
import sys

from fastapi import FastAPI
from databases import Database

logging.basicConfig(level=logging.INFO)
database_filename = "catfacts.db"
database = Database(f"sqlite:///{database_filename}")

app = FastAPI()
v2 = FastAPI()


async def read_random() -> Dict:
  return {"Foo": "Bar"}

@app.on_event("startup")
async def startup_event():
    if not exists(database_filename):
        logging.critical("catfacts.db does not exist in the working directory.")
        logging.critical("Please run `init-catfacts` first.")
        sys.exit(1)
    await database.connect()

@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

@app.get("/")
async def read_root():
    results = await read_random()
    return results


@v2.get("/")
async def read_random_v2_root():
    query = "SELECT * FROM catfacts"
    results = await database.fetch_all(query=query)
    return results


@v2.get("/random")
async def read_random_v2_endpoint():
    results = await read_random()
    return results


app.mount("/v2", v2)