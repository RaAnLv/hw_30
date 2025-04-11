from sqlalchemy import Column, String, Integer

from database import Base

class CookingBook(Base):
    __tablename__ = 'CookingBook'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    product_list = Column(String, index=True)
    time_cook = Column(String, index=True)
    description = Column(String, index=True)
    count = Column(Integer, index=True, default=1)
