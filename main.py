from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Person(BaseModel):
    weight: float
    height: float


@app.post("/diet")
def diet_recommendation(person: Person):
    height_m = person.height/100
    bmi = person.weight/(height_m**2)
    if bmi > 24.9:
        diet = "Cut"
    elif bmi < 18.5:
        diet = "Bulk"
    else:
        diet = "maintain"

    return {"bmi": round(bmi, 2), "diet": diet}
