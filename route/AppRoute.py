from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.Game import Game
from service.AppService import AppService

router = APIRouter()
service = AppService()

@router.get("/")
async def get_status():
    status = service.get_status()
    return status

@router.post("/check")
async def check_game(game: Game):
    result = service.check_game(game=game)
    return JSONResponse(content=result)