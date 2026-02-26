import pytest
from app.services.cache import get_redis_client

@pytest.fixture
def redis_client():
    return get_redis_client()

# Test cache set and get
def test_cache_set_get(redis_client):
    redis_client.set("test_key", "test_value")
    value = redis_client.get("test_key")
    assert value == "test_value"

# Test cache expiry
def test_cache_expiry(redis_client):
    redis_client.setex("test_key_expiry", 1, "test_value")
    value = redis_client.get("test_key_expiry")
    assert value == "test_value"
    import time
    time.sleep(2)
    value = redis_client.get("test_key_expiry")
    assert value is None
