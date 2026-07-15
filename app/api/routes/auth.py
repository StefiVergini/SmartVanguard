from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import RegisterRequest
from app.api.deps import get_db
from app.models.company import Company
from app.models.user import User
from app.core.security import hash_password

router = APIRouter()


@router.post("/register")
@router.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):
    company = Company(
        name=data.company_name,
        business_type="general"
    )

    db.add(company)
    db.flush()

    user = User(
        email=data.email,
        password=hash_password(data.password),
        company_id=company.id
    )

    db.add(user)
    db.commit()

    return {"msg": "ok"}