from typing import Annotated, Any
from fastapi import Body, FastAPI, Query, Path, status
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

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    desc: str
    price: float
    tags: list[str] = []
    tax: float | None = None
    image: Image | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

    class Config:
        schema_extra = {
                "example": {
                    "username": "Ericao",
                    "full_name": "Ericao de Moletao"
                    }
                }

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
@app.get("/items/", response_description="Uma lista de itens.")
async def read_items(q: str | None = "Value"):
    """ 
    Demonstracao da configuracao response description. Caso nenhuma seja fornecida, 
    sera retornada a padrao 'Sucessful response'
    """
    return {}

@app.get("/itemsrestr/")
async def read_rest_items(q: Annotated[str | None, Query(max_length=50)] = None):
    """
     Now we check the length, the Query is related with query parameters. The same thing can be 
     done with the Path. See the example below.
    """
    return {}

@app.get("/itempath/{valval}/$")
async def read_items_val_path(
        valval: Annotated[str, Path(max_length=10)]):
    return {"val": valval}

@app.post("/items/", tags=["Items"])
async def create_item(item: Item):
    """
    Demonstracao de tags.
    """
    item.desc = item.desc + " To de olho"
    return {"new_item": item}

@app.post("/user/")
async def create_user(user: User, status_code=status.HTTP_201_CREATED) -> User:
    """
    Exemplo contendo um retorno e uma configuracao de status de retorno.
    """
    return user

@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: Annotated[int, Body(gt=0)],
        q: str | None = None,
        ):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
