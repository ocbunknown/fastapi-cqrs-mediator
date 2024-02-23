from pydantic import BaseModel


class UserDTO(BaseModel):
    email: str
    hashed_password: str

class UserUpdate(UserDTO):
    ...

class UserCreate(UserDTO):
    ...
