from src.app.common import dto
from src.app.database import models


def convert_user_model_to_dto(model: models.User) -> dto.User:
    return dto.User(**model.as_dict())

def convert_user_model_to_delete_user_dto(model: models.User) -> dto.DeleteUser:
    return dto.DeleteUser(**model.as_dict())
