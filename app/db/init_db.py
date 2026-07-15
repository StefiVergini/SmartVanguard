from app.db.base import Base
from app.db.session import engine
# importar los modelos  
# SQLAlchemy los reconozca al crear las tablas.
from app.db.base import Base
from app.db.session import engine

# Importa todos los modelos
import app.models


# Crea las tablas en la base de datos (si no existen)
# no usar create_all en produ usar alembic
def init_db():
    Base.metadata.create_all(bind=engine)

