from fastapi import FastAPI
from infrastructure.entry_point.graphql.routers import router
from domain.usecases import bank_account_usecase


def create_app():

    app = FastAPI()

    app.include_router(router, prefix="/api")

    @app.get("/health")
    async def root():
        return {"message": "Hello World"}

    return app
