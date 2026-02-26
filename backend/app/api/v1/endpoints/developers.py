from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app import crud, models, schemas
from backend.app.api import deps
from backend.app.services.external_api import generate_avatar_url

router = APIRouter()

@router.get("/", response_model=List[schemas.DeveloperInDB])
def read_developers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 10,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    developers = crud.crud_developer.get_multi(db, skip=skip, limit=limit)
    return developers

@router.post("/", response_model=schemas.DeveloperInDB)
def create_developer(
    *,
    db: Session = Depends(deps.get_db),
    developer_in: schemas.DeveloperCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    avatar_url = generate_avatar_url(developer_in.name)
    developer = crud.crud_developer.create_with_avatar(db=db, obj_in=developer_in, avatar_url=avatar_url)
    return developer

@router.put("/{developer_id}", response_model=schemas.DeveloperInDB)
def update_developer(
    *,
    db: Session = Depends(deps.get_db),
    developer_id: int,
    developer_in: schemas.DeveloperUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    developer = crud.crud_developer.get(db=db, id=developer_id)
    if not developer:
        raise HTTPException(status_code=404, detail="Developer not found")
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    developer = crud.crud_developer.update(db=db, db_obj=developer, obj_in=developer_in)
    return developer

@router.delete("/{developer_id}", response_model=schemas.DeveloperInDB)
def delete_developer(
    *,
    db: Session = Depends(deps.get_db),
    developer_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    developer = crud.crud_developer.get(db=db, id=developer_id)
    if not developer:
        raise HTTPException(status_code=404, detail="Developer not found")
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    developer = crud.crud_developer.remove(db=db, id=developer_id)
    return developer
