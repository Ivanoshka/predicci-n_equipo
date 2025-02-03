from fastapi import FastAPI
from database import db
from models import Partido
from pymongo import MongoClient

app = FastAPI()

@app.post("/partido/")
def agregar_partido(partido: Partido):
    db.partidos.insert_one(partido.dict())
    return {"mensaje": "Partido agregado con éxito"}
