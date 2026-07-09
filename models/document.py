from sqlalchemy import Column, Integer, Text, ForeignKey
from db.base import Base
from pgvector.sqlalchemy import Vector

class Document(Base):
   __tablename__ = "documents"

   id = Column(Integer, primary_key=True)
   content = Column(Text)
   embedding = Column(Vector(1536))
   company_id = Column(Integer, ForeignKey("companies.id"))
