
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal
LengthUnitType = Literal["m", "km", "yard", "mi"]

router = APIRouter()

HEIGHT_COEFF_LT = {
    "M_T_KM": 1000,
    "M_TO_MI": 0.000621371,
    "M_TO_YARD": 1.09361,
    "M_TO_CM": 100,
    "KM_TO_M": 1000,
    "KM_TO_MI": 0.621371,
    "KM_TO_YARD": 1093.61,
    "KM_TO_CM": 100000,
    "CM_TO_M": 0.01,
    "CM_TO_MI": 0.0109361,
    "CM_TO_KM": 0.00001,
    "CM_TO_YARD": 0.0000062137,
    "YARD_TO_KM": 0.0009144,
    "YARD_TO_M": 0.9144,
    "YARD_TO_MI": 0.000568182,
    "YARD_TO_CM": 91.44,
    "MI_TO_CM": 160934,
    "MI_TO_M": 1609.34,
    "MI_TO_YARD": 1760,
    "MI_TO_KM": 1.60934
}


class LengthInfo(BaseModel):
    length: float
    unit: LengthUnitType
    target: LengthUnitType


@router.post("/length")
def length_unit(length_info: LengthInfo):
    coeff = 1
    coeff_key = f"{length_info.unit.upper()}_TO_{length_info.target.upper()}"
    coeff = HEIGHT_COEFF_LT[coeff_key]
    return length_info.length*coeff
