from sqlalchemy import Column, Integer, String, Float

from database import Base

class PeopleModel(Base):
    __tablename__ = 'peoples'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    year = Column(Integer)
    weight = Column(Float)

