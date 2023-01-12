from sqlalchemy import Column, Integer, String

from app.infrastructure.database.postgre import Base


class PersonModel(Base):
    __tablename__ = "person"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    address = Column(String(32))
    state = Column(String(2))
