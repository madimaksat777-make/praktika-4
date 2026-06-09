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


def ge