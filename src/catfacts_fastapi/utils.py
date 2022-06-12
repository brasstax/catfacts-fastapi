import importlib.resources as pkg_resources
import catfacts_fastapi
import pdb
import sqlite3

def init_catfacts():
  with pkg_resources.open_text(catfacts_fastapi, "catfacts.txt") as f:
    catfacts_txt = f.read().splitlines()
  
  con = sqlite3.connect("catfacts.db")
  cur = con.cursor()
  cur.execute("DROP table IF EXISTS catfacts")
  con.commit()
  cur.execute(
    """
    CREATE TABLE catfacts(id INTEGER PRIMARY KEY AUTOINCREMENT, fact TEXT)
    """
  )
  con.commit()

  for fact in catfacts_txt:
    cur.execute("INSERT INTO catfacts(fact) VALUES (?)", (fact,))
  con.commit()
  con.close()


def read_random():
  return {"Foo": "Bar"}
