from fastapi import FastAPI

from app.endpoints.api import register

app = FastAPI()

app.include_router(register.router)
