from pydantic import BaseModel


class User(BaseModel):
    email: str
    hashed_password: str


class UserUpdate(User):
    ...


class UserCreate(User):
    ...


class FindById(BaseModel):
    id: int
