from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel

"""
Parameters that can be passed to query:
* alias
* title
* description
* deprecated

And validation parameters:
* min_length
* max_length
* regex
"""

class Item(BaseModel):
    name: str
    desc: str
    price: float
    tax: float | None = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test/{valor}")
async def test(valor: str):
    return {"valor": valor}

@app.get("/test2/")
async def test2(qvalue: str):
    return {"valor": qvalue}

# Declaring a field with default value
@app.get("/test3/{pvalue}")
async def test3(pvalue: str, qvalue: str = ""):
    return {"valor": qvalue, "pvalue": pvalue}

# Declaring a non required field
@app.get("/items/")
async def read_items(q: str | None = "Value"):
    return {}

# Now we check the length
@app.get("/itemsrestr/")
async def read_rest_items(q: Annotated[str | None, Query(max_length=50)] = None):
    return {}

@app.post("/items/")
async def create_item(item: Item):
    item.desc = item.desc + " To de olho"
    return {"new_item": item}
