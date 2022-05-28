from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String(300))
    name = Column(String(50))
    email = Column(String(200))
    password = Column(String(500))
