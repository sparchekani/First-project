from enum import Enum
from typing import Literal
from fastapi import APIRouter
from pydantic import BaseModel, Field


router = APIRouter(prefix="/fitness")

ACTIVITY_FACTOR = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "heavy": 1.725
}

MIN_PROTEIN_COEF = 1.2
MAX_PROTEIN_COEF = 2.5


class ActivityFactorEnum(Enum):
    sedentary = "sedentary"
    light = "light"
    moderate = "moderate"
    heavy = "heavy"


class Person(BaseModel):
    weight: float
    height: float


class PersonInfo(BaseModel):
    height: float = Field(..., gt=20,
                          description="height must be more than 20 cm")
    weight: float = Field(..., gt=10,
                          description="weight mut be more than 10 kg")
    age: int = Field(..., gt=18,
                     description="age must be more than 18 years old")
    sex: Literal["male", "female"]
    activity_factor: ActivityFactorEnum


class WeightType(BaseModel):
    weight: float


@router.post("/diet")
def diet_recommendation(person: PersonInfo):
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


@router.post("/calories")
def calorie_recommendation(PersonInfo: PersonInfo):
    bmr = calc_bmr(PersonInfo)

    return round(bmr)


def calc_bmr(PersonInfo: PersonInfo):
    if PersonInfo.sex == "male":
        bmr = 10*PersonInfo.weight + 6.25*PersonInfo.height - 5*PersonInfo.age + 5
    else:
        bmr = 10*PersonInfo.weight + 6.25 * \
            PersonInfo.height - 5*PersonInfo.age - 161
    activitiy_factor = ACTIVITY_FACTOR[PersonInfo.activity_factor.value]
    return round(bmr * activitiy_factor)


@router.post("/macros")
def calc_pro(person: PersonInfo):
    min_protein = person.weight*MIN_PROTEIN_COEF
    max_protein = round(person.weight*MAX_PROTEIN_COEF)
    bmr = calc_bmr(person)
    fat_calorie = bmr*0.3
    carb_calorie = bmr
    return {"min protein": min_protein, "max protein": max_protein}


@router.get("/")
def home():
    return {"message": "welcome to diet and fitness API"}
