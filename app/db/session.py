from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#para PRODUCCION DSP CAMBIAR
#engine = create_engine(
#    DATABASE_URL,
#    pool_pre_ping=True,
#    pool_recycle=3600,
#    future=True
#)