from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///nodedb.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Block(Base):
    __tablename__ = 'block'
    hash = Column(String(512), primary_key=True)
    index = Column(Integer, nullable=False)

class Database:
    def update(self, hash, block):
        session.add(block(hash=hash))
        session.commit()

Base.metadata.create_all(engine)