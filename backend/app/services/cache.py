import redis
import os

class RedisCache:
    def __init__(self):
        redis_url = os.getenv('REDIS_URL')
        if not redis_url:
            raise ValueError('REDIS_URL environment variable is required')
        self.client = redis.StrictRedis.from_url(redis_url, decode_responses=True)

    def get(self, key: str):
        return self.client.get(key)

    def set(self, key: str, value: str, ttl: int = 300):
        self.client.setex(key, ttl, value)

redis_cache = RedisCache()
