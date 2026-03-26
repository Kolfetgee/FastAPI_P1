from fastapi import FastAPI

from src.routers.api_v1_router import api_v1_router

app = FastAPI(title="FastAPI Practice")

app.include_router(api_v1_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI practice started"}
