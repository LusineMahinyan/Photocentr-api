from datetime import datetime

from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    service_ids: list[int] = Field(
        min_length=1
    )


class OrderStatusUpdate(BaseModel):
    status: str


class OrderItemResponse(BaseModel):
    id: int
    service_id: int
    quantity: int
    price: int

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: int
    status: str
    created_at: datetime
    updated_at: datetime
    items: list[OrderItemResponse] = []

    class Config:
        from_attributes = True
