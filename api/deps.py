def get_current_user(token: str, db: Session = Depends(get_db)): # Agrega el Depends
    try:
        # Importante: el token suele venir con el prefijo "Bearer ". 
        # Asegúrate de limpiarlo si es necesario.
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except Exception:
        raise HTTPException(status_code=401, detail="Error de autenticación")

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user