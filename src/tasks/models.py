import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from base_models import intpk, created_at, updated_at


class Status(enum.Enum):
    completed = "completed"
    planned = "planned"


class PriorityORM(Base):
    __tablename__ = "priorities"

    id: Mapped[intpk]
    name: Mapped[str]

    def __repr__(self):
        return self.name


class TasksORM(Base):
    __tablename__ = "tasks"

    id: Mapped[intpk]
    task: Mapped[str]
    status: Mapped[Status] = mapped_column(default=Status.planned)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    priority_id: Mapped[int] = mapped_column(ForeignKey("priorities.id", ondelete="CASCADE"), server_default="1")
    # priority: Mapped["PriorityORM"] = relationship(back_populates="priorities")
    # user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    # user: Mapped["UserORM"] = relationship(
    #     back_populates="todos"
    # )



