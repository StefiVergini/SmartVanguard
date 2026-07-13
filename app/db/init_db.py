from app.db.base import Base
from app.db.session import engine
# importar los modelos  
# SQLAlchemy los reconozca al crear las tablas.
from app.models.company import Company
from app.models.document import Document
from app.models.user import User


# Crea las tablas en la base de datos (si no existen)
# no usar create_all en produ usar alembic
Base.metadata.create_all(bind=engine)