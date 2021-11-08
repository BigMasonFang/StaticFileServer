import os

from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse

router = APIRouter()


@router.get("/")
async def read_root():
    return {'Hello': 'world'}


@router.get("/index")
async def index():
    return RedirectResponse('/static/index.html')


@router.get("/proto")
async def proto():
    return {}