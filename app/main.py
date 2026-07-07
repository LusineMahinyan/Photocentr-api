from fastapi import FastAPI

from app.api.v1.users import router as users_router
from app.api.v1.services import router as services_router
from app.api.v1.orders import router as orders_router

app = FastAPI(
    title="Слоник API",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Users",
            "description": "Регистрация и авторизация пользователей"
        },
        {
            "name": "Services",
            "description": "Работа с услугами фотоцентра"
        },
        {
            "name": "Orders",
            "description": "Работа с заказами фотоцентра"
        }
    ]
)

app.include_router(users_router, prefix="/api/v1")
app.include_router(services_router, prefix="/api/v1")
app.include_router(orders_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Добро пожаловать в API фотоцентра «Слоник»!"}
