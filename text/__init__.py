from text.find import router as find_router
from text.replace import router as replace_router
from fastapi import APIRouter

router = APIRouter(prefix="/text")

router.include_router(find_router)
router.include_router(replace_router)
