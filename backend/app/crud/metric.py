from sqlalchemy.orm import Session
from typing import List

from app.models.metric import Metric
from app.schemas.metric import MetricInDB

class CRUDMetric:
    def get_metrics_by_developer_and_sprint(self, db: Session, developer_id: int, sprint_id: int) -> List[MetricInDB]:
        return db.query(Metric).filter(Metric.developer_id == developer_id, Metric.sprint_id == sprint_id).all()

crud_metric = CRUDMetric()
