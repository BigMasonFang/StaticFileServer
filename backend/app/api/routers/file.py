import os
from typing import Optional

from fastapi import APIRouter, File, Form
from fastapi.datastructures import UploadFile
from fastapi.responses import FileResponse, RedirectResponse

from app.utils.oss.oss_base import OSSBase
from app.business.file import FileBusiness

router = APIRouter()


@router.get("/")
async def read_root():
    return {'Hello': 'world'}


@router.get("/index")
async def index():
    return RedirectResponse('/static/index.html')


@router.get("/proto")
async def proto():
    return RedirectResponse('/static/proto.html')


@router.get('/test')
async def oss_test(get: int = 1, delete: int = 0):
    if get:
        for obj in OSSBase.get_bukect_iter(
                prefix='lung_skin_product_guideline'):
            print(obj.key)
    if delete:
        for obj in OSSBase.get_bukect_iter(
                prefix='lung_skin_product_guideline'):
            OSSBase.bucket.delete_object(obj.key)
    return 'ok'


@router.post('/upload_zip')
async def process_upload(file: UploadFile = File(...),
                         file_name: str = Form(...)):
    # read zip
    result = await file.read()

    # process zip
    if result:
        result = await FileBusiness.store_zip_bytes(result, file_name)

    return {'filenames': result}