from fastapi import FastAPI
from route import AppRoute

app = FastAPI()

# Routes
app.include_router(AppRoute.router)