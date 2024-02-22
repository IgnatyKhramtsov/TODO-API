from datetime import datetime

from pydantic import BaseModel


class UsersAddDTO(BaseModel):
    username: str


class UsersDTO(UsersAddDTO):
    id: int


class ToDosAddDTO(BaseModel):
    task: str
    user_id: int

class ToDosDTO(ToDosAddDTO):
    id: int
    created_at: datetime
    updated_at: datetime


class UsersRelDTO(UsersDTO):
    todos: list["ToDosDTO"]


class ToDosRelDTO(ToDosDTO):
    user: "UsersDTO"