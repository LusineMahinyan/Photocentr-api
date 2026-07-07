from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


if TYPE_CHECKING:
    from app.models.order import Order


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"),
        nullable=False
    )

    service_id: Mapped[int] = mapped_column(
        ForeignKey("services.id"),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1
    )

    price: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )
    order: Mapped["Order"] = relationship(
        "Order",
        back_populates="items"
    )
