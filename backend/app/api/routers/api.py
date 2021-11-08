from fastapi import APIRouter
from app.api.routers import file
from app.core.config import settings

router = APIRouter()
router.include_router(file.router, tags=['file'])
