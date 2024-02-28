from typing import Any, Optional

from sqlalchemy import JSON, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.app.database.models import Base
from src.app.database.models.base.mixins import ModelWithIDMixin


class Hotel(ModelWithIDMixin, Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    services: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON, nullable=True)
    rooms_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    image_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
