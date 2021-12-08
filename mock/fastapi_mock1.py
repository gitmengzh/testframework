#   https://www.cnblogs.com/traditional/p/14733610.html

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

class Item(BaseModel):
    # name:str
    # description: str = None
    price: float
    tax: float


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/get_tax")
def get_tax(item:Item):
    if item.tax:
        price_tax = item.price + item.tax
        res = {"res": price_tax}
        return res
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")
