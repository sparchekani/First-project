from enum import Enum
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fitness.fitness import router as fitness_router
from unit_conversion import router as unit_router

app = FastAPI()
app.include_router(fitness_router, tags=["fitness"])
app.include_router(unit_router, tags=["unit convension"])


@app.get("/")
def home():
    return {"message": "welcome to diet and fitness API"}
