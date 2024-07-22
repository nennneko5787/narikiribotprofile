from fastapi import FastAPI

from app.endpoints import callback

app = FastAPI()

app.include_router(callback.router)
