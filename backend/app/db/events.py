import asyncpg
from fastapi import FastAPI
from loguru import logger

from app.core.config import settings


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to {0}", repr(settings.DATABASE_URI))

    app.state.pool = await asyncpg.create_pool(
        str(settings.DATABASE_URI),
        # min_size=MIN_CONNECTIONS_COUNT,
        # max_size=MAX_CONNECTIONS_COUNT,
    )

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    await app.state.pool.close()

    logger.info("Connection closed")