from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_get_developers():
    response = client.get('/api/developers')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_developer():
    response = client.post('/api/developers', json={'name': 'Jane Doe', 'email': 'jane@example.com', 'avatar_url': 'http://example.com/avatar.jpg'})
    assert response.status_code == 201
    assert response.json()['name'] == 'Jane Doe'
