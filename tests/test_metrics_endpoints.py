import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test trigger collection admin only
def test_trigger_collection_admin_only():
    response = client.post("/api/metrics/collect", headers={"Authorization": "Bearer admin_token"})
    assert response.status_code == 200

# Test collection endpoint validation
def test_collection_endpoint_validation():
    response = client.post("/api/metrics/collect")
    assert response.status_code == 401
