from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from pgvector.sqlalchemy import Vector 
from app.db.base import Base

class Embedding(Base):
    __tablename__ = "embeddings"
    id = Column(Integer, primary_key=True)
    dataset_row_id = Column(Integer, ForeignKey("dataset_rows.id"))
    embedding = Column(Vector(1536))
    provider = Column(String(50)) #openai, voyage, etc
    model_name = Column(String(100)) #text-embedding-3-small ej
    created_at = Column(DateTime, server_default=func.now())