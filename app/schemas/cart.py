from pydantic import BaseModel


class CartAddService(BaseModel):
    service_id: int

class CartItemResponse(BaseModel):
    id: int
    service_id: int
    quantity: int
    price: float

class CartResponse(BaseModel):
    items: list[CartItemResponse]
    total_price: int
