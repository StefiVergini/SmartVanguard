@router.post("/register")
def register(email: str, password: str, company_name: str, db: Session = Depends(get_db)):
    # Ya no necesitas crear 'db' manualmente, FastAPI lo hace y lo cierra por ti.
    company = Company(name=company_name, business_type="general")
    db.add(company)
    db.flush() # flush() obtiene el ID de la compañía sin cerrar la transacción

    user = User(
        email=email,
        password=hash_password(password),
        company_id=company.id
    )
    db.add(user)
    db.commit()
    return {"msg": "ok"}