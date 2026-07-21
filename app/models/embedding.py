from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy import Index
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector 
from app.db.base import Base

class Embedding(Base):
    __tablename__ = "embeddings"
    id = Column(Integer, primary_key=True)
    dataset_row_id = Column(Integer, ForeignKey("dataset_rows.id"), nullable=False)
    vector = Column(Vector(1536))
    provider = Column(String(50)) #openai, voyage, etc
    model_name = Column(String(100)) #text-embedding-3-small ej
    dimensions = Column(Integer) #1536 largo del vector, pero podria cambiar
    embedding_version = Column(String(30)) # version del embedding por si se crea mas de una
    created_at = Column(DateTime, server_default=func.now())
    dataset_row = relationship(
    "DatasetRow",
    back_populates="embedding"
    )

Index("idx_embedding_dataset_row", Embedding.dataset_row_id)