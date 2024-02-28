from src.app.common import dto
from src.app.database import models


def convert_user_model_to_dto(model: models.User) -> dto.User:
    return dto.User(**model.as_dict())
