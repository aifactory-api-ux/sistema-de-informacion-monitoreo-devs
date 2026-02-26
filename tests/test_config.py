import os
from backend.app.core.config import settings

def test_environment_variables():
    assert os.getenv('DATABASE_URL') is not None, 'DATABASE_URL is not set'
    assert os.getenv('REDIS_URL') is not None, 'REDIS_URL is not set'
    assert os.getenv('JWT_SECRET') is not None, 'JWT_SECRET is not set'

def test_settings():
    assert settings.PROJECT_NAME == 'DevPulse', 'Project name is incorrect'
    assert settings.API_V1_STR == '/api/v1', 'API version string is incorrect'
