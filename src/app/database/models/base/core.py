from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)


class Base(DeclarativeBase):
    __abstract__: bool = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    """
    Instead of

    id: Mapped[int] = mapped_column(primary_key=True, ...)

    you can use mixin with_id

    """
