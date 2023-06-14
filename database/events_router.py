import logging

from fastapi import APIRouter
from .accessor import gino as db

from config import DB, DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER




router = APIRouter()

@router.on_event("startup")
async def startup():
    try:
        await db.set_bind(f"{DB}+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        logging.info("GINO set bind to database")
    except EnvironmentError:
        logging.critical("GINO not set bind to database")

@router.on_event("shutdown")
async def shutdown():
    await db.pop_bind().close()
    logging.info("GINO pop bind to database")