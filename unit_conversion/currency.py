import json
from locale import currency
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal
CurrencyType = Literal["EUR", "GBP", "INR", "AUD", "CAD", "USD"]
router = APIRouter()

currency_dict = {}
with open("currency.json", "r") as file:
    content = file.read()
    currency_dict = json.loads(content)
    if "rates" in currency_dict:
        currency_dict["rates"]["USD"] = 1
    else:
        print("rates feild was not found")


@router.get(path="/currency")
def currency_change(current_unit: CurrencyType, target_unit: CurrencyType, value: float):
    coeff_current = currency_dict["rates"][current_unit]
    coeff_target = currency_dict["rates"][target_unit]
    coeff = coeff_current/coeff_target
    converted_rate = value * coeff
    return {"result": converted_rate}
