from fastapi import FastAPI
import pandas as pd
import json


app = FastAPI()


@app.get("/")
def read_main():
    return {"msg": "Hello World"}


@app.get("/api/v1/data")
def dummy_request():
    return {"data": "datos"}


@app.get("/api/v1/data/grabaciones_socorro")
def give_data():
    df = pd.read_csv(
        "/workdir/data/grabaciones_vocalizaciones_socorro/grabaciones_vocalizaciones_socorro.csv"
    )
    return df.to_json(orient="records")


@app.get("/api/v1/data/grabaciones_socorro_datapackage")
def give_datapackage():
    datapackage = json.load(
        open("/workdir/data/grabaciones_vocalizaciones_socorro/datapackage.json")
    )
    return datapackage
