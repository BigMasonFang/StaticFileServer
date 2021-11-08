from fastapi import APIRouter

router = APIRouter()


@router.post('create_project')
async def create_project():
    pass