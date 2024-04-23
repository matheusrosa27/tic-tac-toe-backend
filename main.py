from fastapi import FastAPI
from route import AppRoute
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Routes
app.include_router(AppRoute.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)