from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, JSON, Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class DatasetRow(Base):
    __tablename__ = "dataset_rows"

    id = Column(Integer, primary_key=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    row_number = Column(Integer)
    raw_text = Column(Text) #texto crudo para embeddings
    content_json = Column(JSON) # datos estructurados
    created_at = Column(DateTime, server_default=func.now())
    dataset = relationship(
    "Dataset",
    back_populates="rows"
    )
    embedding = relationship(
    "Embedding",
    back_populates="dataset_row",
    uselist=False
    )