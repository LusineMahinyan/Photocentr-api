from fastapi import FastAPI

app = FastAPI(title="Слоник API")

@app.get("/")
def root():
    return {"message": "Добро пожаловать в API фотоцентра Слоник"}
