from typing import Optional

from fastapi import FastAPI
import os

app = FastAPI()

MANDATORY_ENV_VARS = {
    'STAGE': 'DEV'
}


@app.get("/")
def read_root():
    if 'STAGE' in os.environ: 
        return {"Stage":os.environ.get('STAGE')}
    else: 
        return {"Stage": MANDATORY_ENV_VARS['STAGE']}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
 