from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware


def get_app() -> FastAPI:
    app = FastAPI(title='test')

app = FastAPI()


@app.get("/")
async def read_root():
    return {'Hello': 'world'}
