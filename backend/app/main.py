import uvicorn
from fastapi import FastAPI
from fastapi import staticfiles
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.utils.errors.errors import http_error_handler
from app.api.routers.api import router as api_router
from app.core.config import settings
from app.utils.oss.oss_base import OSSBase

from app.core.events import create_start_app_handler, create_stop_app_handler


def get_app() -> FastAPI:
    app = FastAPI(title='test')

    app.add_middleware(
        CORSMiddleware,
        # allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_exception_handler(HTTPException, http_error_handler)
    # app.add_exception_handler(HTTPException, http422_error_handler)

    # router
    app.include_router(api_router)

    # mount
    app.mount("/static",
              StaticFiles(directory="../frontend/static"),
              name="static")
    # os.chdir('backend')

    # oss
    OSSBase.initialize(settings.OSS_ACCESS_KEY_ID,
                       settings.OSS_ACCESS_KEY_SECRET, settings.OSS_ENDPOINT,
                       settings.OSS_BUCKET)

    return app


app = get_app()

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
