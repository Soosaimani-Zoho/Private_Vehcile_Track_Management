from sqlalchemy import Column, Integer, String
from .databaseconnect import Base

# Example model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)