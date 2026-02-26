from pydantic import BaseModel
from datetime import date

class SprintBase(BaseModel):
    name: str
    start_date: date
    end_date: date
    status: str

class SprintCreate(SprintBase):
    pass

class SprintUpdate(SprintBase):
    pass

class SprintInDB(SprintBase):
    id: int

    class Config:
        orm_mode = True
