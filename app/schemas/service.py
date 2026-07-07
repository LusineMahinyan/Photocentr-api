from datetime import datetime

from pydantic import BaseModel, Field


class ServiceCreate(BaseModel):
    name: str = Field(min_length=2, max_length=255)
    description: str = Field(max_length=500)
    price: int = Field(gt=0)


class ServiceUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=255
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )

    price: int | None = Field(
        default=None,
        gt=0
    )


class ServiceResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        from_attributes = True
