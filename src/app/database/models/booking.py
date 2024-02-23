from sqlalchemy import Computed, Date, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.app.database.models import Base
from src.app.database.models.base.mixins import ModelWithIDMixin


class Booking(ModelWithIDMixin, Base):
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    date_from: Mapped[str] = mapped_column(Date, nullable=False)
    date_to: Mapped[str] = mapped_column(Date, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    total_cost: Mapped[int] = mapped_column(
        Integer,
        Computed("(date_to - date_from) * price"),
    )
    total_days: Mapped[int] = mapped_column(
        Integer,
        Computed("(date_to - date_from)"),
    )
