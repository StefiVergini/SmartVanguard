from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    func,
    Text,
    JSON
)
from sqlalchemy import Index
from sqlalchemy.orm import relationship

from app.db.base import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    action = Column(String(100), nullable=False)

    entity_type = Column(String(100), nullable=False)

    entity_id = Column(Integer)

    description = Column(Text)

    ip_address = Column(String(50))

    metadata = Column(JSON)

    status = Column(String(30)) #SUCCESS FAILED WARNING

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    company = relationship(
        "Company",
        back_populates="audit_logs"
    )

    user = relationship(
        "User",
        back_populates="audit_logs"
    )

#index para mayor rapidez en la busqueda porque esta tabla genera demasiados logs
Index("idx_audit_company", AuditLog.company_id)
Index("idx_audit_user", AuditLog.user_id)
Index("idx_audit_created", AuditLog.created_at)