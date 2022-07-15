from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from db import Base

metadata = Base.metadata


class User(Base):
    __tablename__ = 'user_contact'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    address = Column(String(150), nullable=True)
    created = Column(DateTime, default=datetime.now())

    email = relationship('Email', back_populates='user')
    phone = relationship('Phone', back_populates='user')


class Email(Base):
    __tablename__ = "email"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), nullable=True)

    user_id = Column(Integer, ForeignKey('user_contact.id'), nullable=True)
    user = relationship('User', back_populates='email')


class Phone(Base):
    __tablename__ = "phone"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(50), nullable=True)

    user_id = Column(Integer, ForeignKey('user_contact.id'), nullable=True)
    user = relationship('User', back_populates='phone')