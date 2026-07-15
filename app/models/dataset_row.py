from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, JSON
from app.db.base import Base

class DatasetRow(Base):
    __tablename__ = "dataset_rows"

    id = Column(Integer, primary_key=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id"))
    row_number = Column(Integer)
    content_json = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())