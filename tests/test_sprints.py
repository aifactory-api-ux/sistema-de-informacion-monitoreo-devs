from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_get_sprints():
    response = client.get('/api/sprints')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_sprint():
    response = client.post('/api/sprints', json={'name': 'Sprint 2', 'start_date': '2023-02-01', 'end_date': '2023-02-15', 'status': 'planned'})
    assert response.status_code == 201
    assert response.json()['name'] == 'Sprint 2'
