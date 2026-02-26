from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import get_current_active_admin
from app.tasks.metric_collection import collect_metrics

router = APIRouter()

@router.post("/metrics/collect", status_code=status.HTTP_202_ACCEPTED)
def trigger_metric_collection(current_user=Depends(get_current_active_admin)):
    try:
        collect_metrics.delay()
        return {"message": "Metric collection triggered"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
