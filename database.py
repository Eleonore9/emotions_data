from sqlalchemy import create_engine, func
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

engine = create_engine("sqlite:///emotion_data.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, 
                                    autocommit = False,
                                    autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

def init_db():
    import model
    Base.metadata.create_all(bind=engine)
