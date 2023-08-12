# FastApi
from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse

from loguru import logger

# config
from app.config.environment import get_environment_variables

env = get_environment_variables()

# schemas
from app.schemas.information import InformationRequest

information_router = APIRouter(
    prefix="",
    tags=["information"],
    responses={404: {"description": "Not found"}},
)

@information_router.get("/")
def home():
    content = {
        "message": "this is microservice ONE"
    }

    logger.info(f"This app its run in mode debug f{env.DEBUG}")

    return JSONResponse(status_code=status.HTTP_200_OK, content=content)
