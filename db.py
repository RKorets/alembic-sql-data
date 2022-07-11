from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///address_book.db', echo=False)
metadata = Base.metadata
DBSession = sessionmaker(bind=engine)
session = DBSession()