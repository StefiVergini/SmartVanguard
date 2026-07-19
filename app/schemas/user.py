from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    full_name: str
    role: str
    company_id: int
    created_at: datetime
    is_active: bool