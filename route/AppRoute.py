from fastapi import APIRouter
from service.AppService import AppService

router = APIRouter()

@router.get("/")
async def get_status():
    status = AppService.get_status()
    return status