from typing import Union

from fastapi import FastAPI
from catfacts_fastapi import utils

app = FastAPI()
v2 = FastAPI()

@app.get("/")
def read_root():
    return utils.read_random()

@v2.get("/")
def read_random_v2_root():
    return utils.read_random()

@v2.get("/random")
def read_random_v2_endpoint():
    return utils.read_random()


app.mount("/v2", v2)