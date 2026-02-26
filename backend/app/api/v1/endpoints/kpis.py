from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.metric_calculation import metric_calculation_service
from app.services.cache import redis_cache
from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/kpis", response_model=schemas.KPIResponse)
def get_kpis(developer_id: int, sprint_id: int, db: Session = Depends(deps.get_db)):
    cache_key = f"kpis:{developer_id}:{sprint_id}"
    cached_kpis = redis_cache.get(cache_key)
    if cached_kpis:
        return cached_kpis

    metrics = crud.crud_metric.get_metrics_by_developer_and_sprint(db, developer_id=developer_id, sprint_id=sprint_id)
    if not metrics:
        raise HTTPException(status_code=404, detail="Metrics not found")

    kpis = schemas.KPIResponse(
        sprint_completion=metric_calculation_service.calculate_sprint_completion(metrics),
        pr_review_time=metric_calculation_service.calculate_pr_review_time(metrics),
        bug_density=metric_calculation_service.calculate_bug_density(metrics),
        deployment_frequency=metric_calculation_service.calculate_deployment_frequency(metrics),
        platform_adoption=metric_calculation_service.calculate_platform_adoption(metrics)
    )

    redis_cache.set(cache_key, kpis.dict())
    return kpis
