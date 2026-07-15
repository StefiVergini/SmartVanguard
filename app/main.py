from fastapi import FastAPI

from app.api.routes import auth, chat, upload

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="SmartVanguard API",
    description="Business Intelligence powered by AI",
    version="1.0.0"
)

# Incluimos los routers con prefijos para mejor orden
app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
app.include_router(upload.router, prefix="/files", tags=["Archivos"])
app.include_router(chat.router, prefix="/ai", tags=["Chat IA"])

@app.get("/", tags=["Health"])
def health_check():
    return {
        "status": "running",
        "service": "SmartVanguard API"
    }