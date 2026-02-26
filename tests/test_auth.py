from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_login_success():
    response = client.post('/api/auth/login', json={'username': 'admin', 'password': 'password'})
    assert response.status_code == 200
    assert 'access_token' in response.json()

def test_login_failure():
    response = client.post('/api/auth/login', json={'username': 'admin', 'password': 'wrongpassword'})
    assert response.status_code == 401
    assert response.json() == {'detail': 'Invalid credentials'}
