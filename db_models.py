from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float,Text


Base = declarative_base()

class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key = True, index= True)
    name= Column(String(100))
    description = Column(String(Text))
    price = Column(Float)
    quantity = Column(Integer)
