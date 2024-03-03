from typing import Any

from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)


class Base(DeclarativeBase):
    __abstract__: bool = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def as_dict(self) -> dict[str, Any]:
        return {
            attr: value
            for attr, value in self.__dict__.items()
            if not attr.startswith("_")
        }
