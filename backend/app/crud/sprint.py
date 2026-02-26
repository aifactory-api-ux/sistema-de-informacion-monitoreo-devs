from backend.app.crud.base import CRUDBase
from backend.app.models.sprint import Sprint
from backend.app.schemas.sprint import SprintCreate, SprintUpdate

class CRUDSprint(CRUDBase[Sprint, SprintCreate, SprintUpdate]):
    pass

crud_sprint = CRUDSprint(Sprint)
