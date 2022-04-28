from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    price = Column(String, nullable=False)
    stars = Column(String, nullable=True, unique=False)
    img = Column(String, nullable=False, unique=False)
    location = Column(String, nullable=False, unique=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    type_id = Column(String, nullable=True, unique=False)

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, nullable=False)
    addressType = Column(String, nullable=False, unique=True)
    contactPersonName = Column(String, nullable=False)
    contactPersonNumber = Column(Integer, nullable=False)
    address = Column(String, nullable=True, unique=False)
    latitude = Column(String, nullable=False, unique=False)
    longitude = Column(String, nullable=False, unique=False)
