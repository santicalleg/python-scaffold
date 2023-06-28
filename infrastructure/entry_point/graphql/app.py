from fastapi import FastAPI
from infrastructure.entry_point.graphql.routers import router

def create_app():

    app = FastAPI()

    app.include_router(router, prefix="/api")

    @app.get("/health")
    async def root():
        return {"message": "Hello World"}
    
    return app