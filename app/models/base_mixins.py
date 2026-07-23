from sqlalchemy import Column, Boolean, DateTime, Integer, ForeignKey


class SoftDeleteMixin:

    is_deleted = Column(
        Boolean,
        default=False,
        nullable=False
    )

    deleted_at = Column(
        DateTime
    )

    deleted_by = Column(
        Integer,
        ForeignKey("users.id")
    )