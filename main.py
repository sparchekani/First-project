from fastapi import FastAPI
from fitness.fitness import router as fitness_router
from unit_conversion import router as unit_router
from text import router as text_router


app = FastAPI()
app.include_router(fitness_router, tags=["Fitness"])
app.include_router(unit_router, tags=["Unit convension"])
app.include_router(text_router, tags=["Text"])


@app.get("/")
def home():
    return {"message": "welcome to diet and fitness API"}
