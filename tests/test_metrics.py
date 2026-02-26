from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_get_metrics():
    response = client.get('/api/metrics')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_metrics_read_only():
    response = client.post('/api/metrics', json={'commits': 5, 'code_reviews': 2, 'deployments': 1, 'bug_fixes': 0})
    assert response.status_code == 405
