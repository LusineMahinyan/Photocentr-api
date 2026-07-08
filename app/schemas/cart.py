from pydantic import BaseModel


class CartAddService(BaseModel):
    service_id: int

class CartItemResponse(BaseModel):
    service_id: int
    quantity: int
    price: int

class CartResponse(BaseModel):
    items: list[CartItemResponse]
    total_price: int
