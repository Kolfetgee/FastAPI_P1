from fastapi import FastAPI

from src.apps.auth.middleware import auth_middleware
from src.routers.api_v1_router import api_v1_router

app = FastAPI(title="FastAPI Practice")

app.middleware("http")(auth_middleware)

app.include_router(api_v1_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI practice started"}
