from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
# Importamos las variables desde tu archivo de configuración
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# Configuración para el hasheo de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str):
    """Transforma una contraseña plana en un hash seguro."""
    return pwd_context.hash(password)

def verify_password(password, hashed):
    """Verifica si la contraseña escrita coincide con el hash guardado."""
    return pwd_context.verify(password, hashed)

def create_access_token(data: dict):
    """Crea el token JWT para la sesión del usuario."""
    to_encode = data.copy()
    
    # Usamos la variable ACCESS_TOKEN_EXPIRE_MINUTES que viene de config.py
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    
    # Firmamos el token con nuestra llave secreta
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)