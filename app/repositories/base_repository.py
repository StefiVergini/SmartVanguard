from datetime import datetime
from typing import Type, TypeVar, Generic

from sqlalchemy.orm import Session

from app.db.base import Base

#create a generic model, which is the base of all repositories
ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(
        self,
        db: Session,
        id: int,
        include_deleted: bool = False
    ):

        query = db.query(self.model).filter(
            self.model.id == id
        )

        if hasattr(self.model, "is_deleted") and not include_deleted:
            query = query.filter(
                self.model.is_deleted == False
            )

        return query.first()

    def get_all(
        self,
        db: Session,
        include_deleted: bool = False
    ):

        query = db.query(self.model)

        if hasattr(self.model, "is_deleted") and not include_deleted:
            query = query.filter(
                self.model.is_deleted == False
            )

        return query.all()

    def create(
        self,
        db: Session,
        **kwargs
    ) -> ModelType:

        obj = self.model(**kwargs)

        db.add(obj)
        db.commit()
        db.refresh(obj)

        return obj

    def update(
        self,
        db: Session,
        obj: ModelType,
        **kwargs
    ) -> ModelType:

        for key, value in kwargs.items():
            setattr(obj, key, value)

        db.commit()
        db.refresh(obj)

        return obj

    def update_fields(
        self,
        db: Session,
        obj: ModelType,
        **fields
    ):

        for field, value in fields.items():
            setattr(obj, field, value)

        db.commit()
        db.refresh(obj)

        return obj

    def soft_delete(
        self,
        db: Session,
        obj: ModelType,
        deleted_by: int | None = None
    ):

        if not hasattr(obj, "is_deleted"):
            raise AttributeError(
                f"{self.model.__name__} no soporta soft delete."
            )

        obj.is_deleted = True
        obj.deleted_at = datetime.utcnow()
        obj.deleted_by = deleted_by

        db.commit()
        db.refresh(obj)

        return obj
    
    def restore(
        self,
        db: Session,
        obj
    ):

        obj.is_deleted = False
        obj.deleted_at = None
        obj.deleted_by = None

        db.commit()
        db.refresh(obj)

        return obj
    
    def delete(
        self,
        db: Session,
        obj: ModelType
    ):

        db.delete(obj)
        db.commit()

    def exists(
        self,
        db: Session,
        include_deleted: bool = False,
        **filters
    ):

        query = db.query(self.model).filter_by(**filters)

        if hasattr(self.model, "is_deleted") and not include_deleted:
            query = query.filter(
                self.model.is_deleted == False
            )

        return query.first() is not None

    def get_first(
        self,
        db: Session,
        include_deleted: bool = False,
        **filters
    ):

        query = db.query(self.model).filter_by(**filters)

        if hasattr(self.model, "is_deleted") and not include_deleted:
            query = query.filter(
                self.model.is_deleted == False
            )

        return query.first()
    
    def count(
        self,
        db: Session,
        include_deleted: bool = False
    ):

        query = db.query(self.model)

        if hasattr(self.model, "is_deleted") and not include_deleted:
            query = query.filter(
                self.model.is_deleted == False
            )

        return query.count()
    
    def count_by(
        self,
        db: Session,
        include_deleted: bool = False,
        **filters
    ):

        query = db.query(self.model).filter_by(**filters)

        if hasattr(self.model, "is_deleted") and not include_deleted:
            query = query.filter(
                self.model.is_deleted == False
            )

        return query.count()
    
    def paginate(
        self,
        db: Session,
        page: int = 1,
        page_size: int = 20,
        include_deleted: bool = False
    ):

        query = db.query(self.model)

        if hasattr(self.model, "is_deleted") and not include_deleted:
            query = query.filter(
                self.model.is_deleted == False
            )

        offset = (page - 1) * page_size

        return (
            query
            .offset(offset)
            .limit(page_size)
            .all()
        )
    
    def paginate_by(
        self,
        db: Session,
        page: int = 1,
        page_size: int = 20,
        include_deleted: bool = False,
        **filters
    ):

        query = db.query(self.model).filter_by(**filters)

        if hasattr(self.model, "is_deleted") and not include_deleted:
            query = query.filter(
                self.model.is_deleted == False
            )

        offset = (page - 1) * page_size

        return (
            query
            .offset(offset)
            .limit(page_size)
            .all()
        )
    
    def order_by(
        self,
        db: Session,
        column,
        descending=False
    ):

        query = db.query(self.model)

        if descending:
            query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())

        return query.all()
    
    def get_or_404(
        self,
        db: Session,
        id: int
    ):

        obj = self.get_by_id(db, id)

        if obj is None:
            raise ValueError("Object not found")

        return obj
    
    # For inserting thousands of rows efficiently
    # Session.bulk_save_objects() perform high-speed, lower-latency
    # INSERT and UPDATE operations by accepting a list of 
    # mapped Object-Relational Mapping (ORM) instances
    def bulk_create(
        self,
        db: Session,
        objects: list[ModelType]
    ):

        db.bulk_save_objects(objects)
        db.commit()