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
    created = Column(DateTime, default=datetime.now())

    contacts = relationship('Contact', back_populates='user')


class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(String(200), nullable=True)

    user_id = Column(Integer, ForeignKey('user_contact.id'), nullable=True)
    user = relationship('User', back_populates='contacts')

