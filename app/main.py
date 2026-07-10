from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.core.exceptions import http_exception_handler

from app.api.v1.users import router as users_router
from app.api.v1.services import router as services_router
from app.api.v1.orders import router as orders_router
from app.api.v1.cart import router as cart_router


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


# Разрешаем работу React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users_router, prefix="/api/v1")
app.include_router(services_router, prefix="/api/v1")
app.include_router(orders_router, prefix="/api/v1")
app.include_router(cart_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": "Добро пожаловать в API фотоцентра «Слоник»!"
    }
