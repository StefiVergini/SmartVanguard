import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL: str = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440  # dura la sesion 24 hs, luego config en el front

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definida.")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY no está definida.")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY no está definida.")

