from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app import crud, models, schemas
from backend.app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.SprintInDB])
def read_sprints(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 10,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    sprints = crud.crud_sprint.get_multi(db, skip=skip, limit=limit)
    return sprints

@router.post("/", response_model=schemas.SprintInDB)
def create_sprint(
    *,
    db: Session = Depends(deps.get_db),
    sprint_in: schemas.SprintCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    sprint = crud.crud_sprint.create(db=db, obj_in=sprint_in)
    return sprint

@router.put("/{sprint_id}", response_model=schemas.SprintInDB)
def update_sprint(
    *,
    db: Session = Depends(deps.get_db),
    sprint_id: int,
    sprint_in: schemas.SprintUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    sprint = crud.crud_sprint.get(db=db, id=sprint_id)
    if not sprint:
        raise HTTPException(status_code=404, detail="Sprint not found")
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    sprint = crud.crud_sprint.update(db=db, db_obj=sprint, obj_in=sprint_in)
    return sprint

@router.delete("/{sprint_id}", response_model=schemas.SprintInDB)
def delete_sprint(
    *,
    db: Session = Depends(deps.get_db),
    sprint_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    sprint = crud.crud_sprint.get(db=db, id=sprint_id)
    if not sprint:
        raise HTTPException(status_code=404, detail="Sprint not found")
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    sprint = crud.crud_sprint.remove(db=db, id=sprint_id)
    return sprint
