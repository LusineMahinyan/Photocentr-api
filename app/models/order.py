from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


if TYPE_CHECKING:
    from app.models.order_item import OrderItem


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    total_price: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    status: Mapped[str] = mapped_column(
        Enum(
            "new",
            "processing",
            "ready",
            "completed",
            "cancelled",
            name="order_status"
        ),
        default="new",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    items: Mapped[list["OrderItem"]] = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )
