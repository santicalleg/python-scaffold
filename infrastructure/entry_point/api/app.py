from fastapi import FastAPI
from infrastructure.entry_point.api.routers import router


def create_app():

    app = FastAPI()

    app.include_router(router)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app
