import redis

from config import (
    REDIS_HOST,
    REDIS_PORT,
    REDIS_DB,
    CACHE_TTL
)

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB
)


def get_cache(key):
    data = r.get(key)

    if data:
        return data.decode()

    return None


def set_cache(key, value):
    r.setex(key, CACHE_TTL, value)