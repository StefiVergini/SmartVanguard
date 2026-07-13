from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class User(Base):
   __tablename__ = "users"

   id = Column(Integer, primary_key=True)
   email = Column(String, unique=True)
   password = Column(String)
   company_id = Column(Integer, ForeignKey("companies.id"))
