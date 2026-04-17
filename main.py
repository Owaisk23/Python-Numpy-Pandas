from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
# import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/hello')
def hello():
    return {'msg': "Hello"}

@app.get('/bye')
def bye():
    return {'msg': "bye"}