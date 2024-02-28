from typing import Any, Optional

from sqlalchemy import JSON, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.app.database.models import Base
from src.app.database.models.base.mixins import ModelWithIDMixin


class Room(ModelWithIDMixin, Base):
    hotel_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    services: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON, nullable=True)
    quantity: Mapped[int] = mapped_column(Integer)
    image_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
