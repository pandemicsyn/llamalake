from fastapi import FastAPI

from .routers import runs
from .settings import settings

app = FastAPI()
app.include_router(runs.router)


@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "meltano_project": settings.project,
    }


@app.get("/", tags=["just-a-test"])
async def root():
    return {"message": "nothing to see here, move along"}


@app.get("/health")
async def health():
    return {"status": "ok", "up": True}
