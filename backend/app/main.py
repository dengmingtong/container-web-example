from typing import Optional
import logging
import uvicorn as uvicorn

from fastapi import FastAPI
import os

app = FastAPI()

MANDATORY_ENV_VARS = {
    'STAGE': 'DEV'
}


@app.get("/")
def read_root():
    logging.info("read_root start")
    logging.info("read_root start {}".format(os.environ.get('STAGE')))
    if 'STAGE' in os.environ: 
        return {"Stage":os.environ.get('STAGE')}
    else: 
        return {"Stage": MANDATORY_ENV_VARS['STAGE']}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    #logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S',
                        level=logging.INFO)
    uvicorn.run(app, host="0.0.0.0", port=80)    
 