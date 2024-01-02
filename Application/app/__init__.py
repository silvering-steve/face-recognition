from .routers import *
from .resources import *

from fastapi import FastAPI

app = FastAPI()

app.include_router(recognition_routes.router, prefix="/v1", tags=["V1"])