from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

from config import settings


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
)

session_factory = sessionmaker(sync_engine)


def get_session():
    with session_factory() as session:
        yield session


class Base(DeclarativeBase):
    pass



