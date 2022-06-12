from typing import Union, Dict
import logging
from os.path import exists
import sys

from fastapi import FastAPI, HTTPException
from catfacts_fastapi import utils
from databases import Database
from sqlalchemy.sql import func, select

logging.basicConfig(level=logging.INFO)
database_filename = "catfacts.db"
database = Database(f"sqlite:///{database_filename}")

app = FastAPI()
v2 = FastAPI()


async def read_random() -> Dict:
    s = select(utils.catfacts)
    query = s.order_by(func.random()).limit(1)
    results = await database.fetch_one(query=query)
    return results


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
async def read_all_v2_root():
    query = utils.catfacts.select()
    results = await database.fetch_all(query=query)
    return results


@v2.get("/random")
async def read_random_v2_endpoint():
    results = await read_random()
    return results


@v2.get("/fact/{fact_id}")
async def read_fact_by_id(fact_id: int):
    try:
        fact_id = int(fact_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Not a valid fact ID")
    query = select(utils.catfacts).where(utils.catfacts.c.id == fact_id)
    results = await database.fetch_one(query=query)
    if not results:
        raise HTTPException(status_code=404, detail="Fact ID not found")
    return results


app.mount("/v2", v2)
