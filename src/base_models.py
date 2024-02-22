from datetime import datetime
from typing import Annotated

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow
    )]

# class UserORM(Base):
#     __tablename__ = "users"
#
#     id: Mapped[intpk]
#     username: Mapped[str]
#
#     todos: Mapped[list["ToDoORM"]] = relationship(
#         back_populates="user"
#     )
#
#
# class ToDoORM(Base):
#     __tablename__ = "todos"
#
#     id: Mapped[intpk]
#     task: Mapped[str]
#     created_at: Mapped[created_at]
#     updated_at: Mapped[updated_at]
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
#
#     user: Mapped["UserORM"] = relationship(
#         back_populates="todos"
#     )