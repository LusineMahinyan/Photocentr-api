from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.repositories.cart_repository import CartRepository
from app.schemas.cart import CartAddService,  CartResponse
from app.services.cart_service import CartService
from app.repositories.order_repository import OrderRepository

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

@router.post("/add")
async def add_service_to_cart(
    data: CartAddService,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    cart_repository = CartRepository(db)
    order_repository = OrderRepository(db)

    service = CartService(
        cart_repository,
        order_repository
    )

    return await service.add_service(
        current_user.id,
        data.service_id
    )


@router.get(
    "/",
    response_model=CartResponse
)
async def get_cart(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    cart_repository = CartRepository(db)
    order_repository = OrderRepository(db)

    service = CartService(
        cart_repository,
        order_repository
    )

    return await service.get_cart(
        current_user.id
    )

@router.delete(
    "/item/{item_id}"
)
async def remove_item(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    cart_repository = CartRepository(db)
    order_repository = OrderRepository(db)

    service = CartService(
        cart_repository,
        order_repository
    )

    success = await service.remove_item(
        current_user.id,
        item_id
    )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Товар не найден в корзине"
        )

    return {
        "message": "Товар удален из корзины"
    }

@router.delete(
    "/clear"
)
async def clear_cart(
        current_user: User = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):

    repository = CartRepository(db)

    service = CartService(
        repository
    )

    result = await service.clear_cart(
        current_user.id
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Корзина не найдена"
        )

    return {
        "message": "Корзина очищена"
    }
