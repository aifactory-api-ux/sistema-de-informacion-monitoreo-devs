from sqlalchemy.orm import Session
from typing import Optional

from backend.app.crud.base import CRUDBase
from backend.app.models.developer import Developer
from backend.app.schemas.developer import DeveloperCreate, DeveloperUpdate

class CRUDDeveloper(CRUDBase[Developer, DeveloperCreate, DeveloperUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[Developer]:
        return db.query(Developer).filter(Developer.email == email).first()

    def create_with_avatar(self, db: Session, *, obj_in: DeveloperCreate, avatar_url: str) -> Developer:
        db_obj = Developer(
            name=obj_in.name,
            email=obj_in.email,
            avatar_url=avatar_url
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

crud_developer = CRUDDeveloper(Developer)
