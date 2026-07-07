from fastapi import FastAPI

from app.api.v1.users import router as users_router

app = FastAPI(
    title="Слоник API",
    version="1.0.0",
)

app.include_router(users_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Добро пожаловать в API фотоцентра «Слоник»!"}
