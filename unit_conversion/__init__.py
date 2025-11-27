from unit_conversion.weight import router as weight_router
from unit_conversion.length import router as length_router
from unit_conversion.currency import router as currency_router
from fastapi import APIRouter

router = APIRouter(prefix="/unit_convension")


router.include_router(weight_router)
router.include_router(length_router)
router.include_router(currency_router)
