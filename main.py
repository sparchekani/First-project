from enum import Enum
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fitness.fitness import router as fitness_router

app = FastAPI()
app.include_router(fitness_router, tags=["fitness"])
