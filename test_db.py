from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///absolute/path/to/foo.db', echo=True)
Base = declarative_base()

id = Column(Integer, primary_key=True)
name = Column(String)

Base.metadata.create_all(engine)
