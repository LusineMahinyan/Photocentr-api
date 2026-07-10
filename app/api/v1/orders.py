from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_current_user, get_current_admin
from app.db.database import get_db
from app.models.user import User

from app.repositories.order_repository import OrderRepository
from app.repositories.cart_repository import CartRepository

from app.schemas.order import OrderCreate, OrderResponse, OrderStatusUpdate

from app.services.order_service import OrderService
from app.services.cart_service import CartService

router = APIRouter(prefix="/orders", tags=["Orders"])


# Создать заказ вручную из списка услуг
@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
    order_data: OrderCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):

    repository = OrderRepository(db)

    service = OrderService(repository)

    order = await service.create_order(current_user.id, order_data)

    if not order:
        raise HTTPException(status_code=400, detail="Услуги не найдены")

    return order


# Получить все заказы (только админ)
@router.get("/", response_model=list[OrderResponse])
async def get_all_orders(
    current_admin: User = Depends(get_current_admin), db: AsyncSession = Depends(get_db)
):

    repository = OrderRepository(db)

    service = OrderService(repository)

    return await service.get_all_orders()


# Получить свои заказы
@router.get("/my", response_model=list[OrderResponse])
async def get_my_orders(
    current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)
):

    repository = OrderRepository(db)

    service = OrderService(repository)

    return await service.get_my_orders(current_user.id)


# Получить заказ по id
@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):

    repository = OrderRepository(db)

    service = OrderService(repository)

    order = await service.get_order(order_id, current_user.id)

    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")

    return order


# Изменить статус заказа (только админ)
@router.patch("/{order_id}/status", response_model=OrderResponse)
async def update_order_status(
    order_id: int,
    status_data: OrderStatusUpdate,
    current_admin: User = Depends(get_current_admin),
    db: AsyncSession = Depends(get_db),
):

    repository = OrderRepository(db)

    service = OrderService(repository)

    order = await service.update_status(order_id, status_data)

    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")

    return order


# Создать заказ из корзины
@router.post(
    "/checkout", response_model=OrderResponse, status_code=status.HTTP_201_CREATED
)
async def checkout(
    current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)
):

    cart_repository = CartRepository(db)
    order_repository = OrderRepository(db)

    service = CartService(cart_repository, order_repository)

    order = await service.checkout(current_user.id)

    if not order:
        raise HTTPException(status_code=400, detail="Корзина пуста")

    return order
