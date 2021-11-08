from fastapi import FastAPI
from fastapi import staticfiles
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.utils.errors.errors import http_error_handler
from app.api.routers.api import router as api_router
# from app.core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.core.config import settings

from app.core.events import create_start_app_handler, create_stop_app_handler
from fastapi.staticfiles import StaticFiles


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

    app.include_router(api_router)
    app.mount("/static",
              StaticFiles(directory="../frontend/static"),
              name="static")
    # os.chdir('backend')

    return app


app = get_app()
