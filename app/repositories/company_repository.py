from sqlalchemy.orm import Session

from app.models.company import Company
from app.repositories.base_repository import BaseRepository

class CompanyRepository(BaseRepository[Company]):

    def __init__(self):
        super().__init__(Company)

    def get_by_name(
        self,
        db,
        name: str
    ):

        return (
            db.query(Company)
            .filter(Company.name == name)
            .first()
        )