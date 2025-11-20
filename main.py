from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
BASIC_ACTIVITY = 400


class Person(BaseModel):
    weight: float
    height: float


class Person_info(BaseModel):
    height: float
    weight: float
    age: int
    sex: Literal["male", "female"]


class WeightType(BaseModel):
    weight: float


@app.post("/diet")
def diet_recommendation(person: Person_info):
    height_m = person.height/100
    bmi = person.weight/(height_m**2)
    bmr = calc_bmr(person)
    if bmi > 24.9:
        calories = bmr - 500
        diet = "cut"
    elif bmi < 18.5:
        calories = bmr + 500
        diet = "bulk"
    else:
        calories = bmr
        diet = "maintain"

    return {"bmi": round(bmi, 2), "diet": diet, "calorie": calories}


@app.post("/claories")
def calorie_recommendation(person_info: Person_info):
    bmr = calc_bmr(person_info)

    return round(bmr)


def calc_bmr(person_info: Person_info):
    if person_info.sex == "male":
        bmr = 10*person_info.weight + 6.25*person_info.height - 5*person_info.age + 5
    else:
        bmr = 10*person_info.weight + 6.25 * \
            person_info.height - 5*person_info.age - 161
    return round(bmr + BASIC_ACTIVITY)


@app.post("/protein")
def calc_pro(weight: WeightType):
    min_protein = weight.weight
    max_protein = round(weight.weight*2.5)
    return {"min protein": min_protein, "max protein": max_protein}


@app.get("")
def home():
    return {"message": "welcome to diet and fitness API"}
