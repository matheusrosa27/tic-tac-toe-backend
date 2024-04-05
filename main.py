from fastapi import FastAPI
from routes import AppRoute

app = FastAPI()

# Routes
app.include_router(AppRoute.router)