from pydantic import BaseModel
from typing import Optional

class MetricCreate(BaseModel):
    developer_id: int
    sprint_id: int
    commits: int
    code_reviews: int
    deployments: int
    bug_fixes: int

class MetricInDB(MetricCreate):
    id: int

    class Config:
        orm_mode = True

class KPIResponse(BaseModel):
    sprint_completion: float
    pr_review_time: float
    bug_density: float
    deployment_frequency: float
    platform_adoption: float
