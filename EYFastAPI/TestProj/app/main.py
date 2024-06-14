import logging
from fastapi import FastAPI
from controllers import controller

logging.basicConfig(level=logging.INFO)

appl = FastAPI()

appl.include_router(controller.router)