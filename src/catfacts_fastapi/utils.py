import importlib.resources as pkg_resources
import asyncio
from typing import Dict
import catfacts_fastapi
import sqlite3
import sqlalchemy
from databases import Database


metadata = sqlalchemy.MetaData()
catfacts = sqlalchemy.Table(
    "catfacts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("fact", sqlalchemy.Text),
)


async def init_catfacts_async():
    with pkg_resources.open_text(catfacts_fastapi, "catfacts.txt") as f:
        catfacts_txt = f.read().splitlines()

    con = sqlite3.connect("catfacts.db")
    cur = con.cursor()
    cur.execute("DROP table IF EXISTS catfacts")
    con.commit()
    con.close()

    engine = sqlalchemy.create_engine(
        "sqlite:///catfacts.db", echo=True, connect_args={"check_same_thread": False}
    )
    metadata.create_all(engine)

    database = Database("sqlite:///catfacts.db")

    query = catfacts.insert()
    for fact in catfacts_txt:
        values = {"fact": fact}
        await database.execute(query=query, values=values)

    await database.disconnect()


def init_catfacts():
    asyncio.run(init_catfacts_async())
