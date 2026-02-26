import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.cache import get_redis_client

client = TestClient(app)

@pytest.fixture
def redis_client():
    return get_redis_client()

# Test KPI calculation for sprint completion
def test_kpi_calculation_sprint_completion(redis_client):
    response = client.get("/api/kpis?sprint_id=1")
    assert response.status_code == 200
    data = response.json()
    assert "sprint_completion" in data

# Test KPI calculation for PR review
def test_kpi_calculation_pr_review(redis_client):
    response = client.get("/api/kpis?sprint_id=1")
    assert response.status_code == 200
    data = response.json()
    assert "pr_review" in data

# Test Redis cache hit
def test_redis_cache_hit(redis_client):
    redis_client.set("kpi:sprint:1", "cached_data")
    response = client.get("/api/kpis?sprint_id=1")
    assert response.status_code == 200
    assert response.json() == "cached_data"

# Test Redis cache miss
def test_redis_cache_miss(redis_client):
    redis_client.delete("kpi:sprint:1")
    response = client.get("/api/kpis?sprint_id=1")
    assert response.status_code == 200
    data = response.json()
    assert "sprint_completion" in data
