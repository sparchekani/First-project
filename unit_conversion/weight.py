from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal

router = APIRouter()

WeightUnitType = Literal["kg", "lb", "g", "oz"]

KG_TO_LB_COEFF = 2.2046226218
KG_TO_G_COEFF = 1000
LB_TO_KG_COEFF = 0.45359237
LB_TO_G_COEFF = 453.59237
G_TO_KG_COEFF = 0.001
G_TO_LB_COEFF = 2.2046226218
OZ_TO_G_COEFF = 28.3495
OZ_TO_KG_COEFF = 0.0283495
OZ_TO_LB_COEFF = 0.0625
G_TO_OZ_COEFF = 0.03527
KG_TO_OZ_COEFF = 35.27
LB_TO_OZ_COEFF = 16

WEIGHT_COEFF_LT = {
    "KG_TO_LB": 2.2046226218,
    "KG_TO_G": 1000,
    "LB_TO_KG": 0.45359237,
    "LB_TO_G": 453.59237,
    "G_TO_KG": 0.001,
    "G_TO_LB": 2.2046226218,
    "OZ_TO_G": 28.3495,
    "OZ_TO_KG": 0.0283495,
    "OZ_TO_LB": 0.0625,
    "G_TO_OZ": 0.03527,
    "KG_TO_OZ": 35.27,
    "LB_TO_OZ": 16
}


class WeightInfo(BaseModel):
    weight: float
    unit: WeightUnitType
    target: WeightUnitType


@router.post("/weight")
def weight_unit(weight_info: WeightInfo):
    coeff = 1
    coeff_key = f"{weight_info.unit.upper()}_TO_{weight_info.target.upper()}"
    coeff = WEIGHT_COEFF_LT[coeff_key]
    return weight_info.weight*coeff
