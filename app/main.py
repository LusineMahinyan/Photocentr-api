from fastapi import FastAPI

app = FastAPI(
    title="Photocentr API",
    description="Backend API для фотоцентра",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Добро пожаловать в Photocentr API!"}
