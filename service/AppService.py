from fastapi import FastAPI

class AppService():
    def __init__(self):
        self.app = FastAPI()

    def get_status():
        return {"status": "ok"}