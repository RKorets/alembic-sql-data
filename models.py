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


#
# engine = create_engine('sqlite:///:memory:', echo=True)
#
# session = sessionmaker(bind=engine)()
#
# Base = declarative_base()
#
#
# class User(Base):
#
# 	__tablename__ = 'users'
#
# 	id = Column(Integer, primary_key=True)
# 	name = Column(String(10))
#
#
# class Contact(Base):
#
# 	__tablename__ = 'contacts'
#
# 	id = Column(Integer, primary_key=True)
# 	user_id = Column(None, ForeignKey('users.id'))
# 	email = Column(String(50))
#
#
# Base.metadata.create_all(engine)
# Base.metadata.bind = engine
#
# new_user = User(name='Vasya')
# session.add(new_user)
#
# new_user = User(name='Petya')
# session.add(new_user)
#
# session.commit()
#
# for user in session.query(User).all():
# 	print(user.id, user.name)

if __name__ == '__main__':
    main()
