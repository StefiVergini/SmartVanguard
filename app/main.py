from fastapi import FastAPI
from db.session import engine
from db.base import Base

# IMPORTANTE: Debes importar tus modelos aquí para que 
# SQLAlchemy los reconozca al crear las tablas.
from models.user import User
from models.company import Company
from models.document import Document

from api.routes import auth, upload, chat

# Crea las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi IA API")

# Incluimos los routers con prefijos para mejor orden
app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
app.include_router(upload.router, prefix="/files", tags=["Archivos"])
app.include_router(chat.router, prefix="/ai", tags=["Chat IA"])

@app.get("/")
def health_check():
    return {"status": "running"}