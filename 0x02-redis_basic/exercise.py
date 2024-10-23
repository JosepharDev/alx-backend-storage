#!/usr/bin/env python3
"""class that has a redis instance"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self) -> None:
        """Initialize the Cache class, set up a Redis client,
            and flush the Redis database."""
        self.__redis = redis.Redis()
        self.__redis.flushdb(True)

    def store(self, data:  Union[str, bytes, int, float]) -> str:
        """Store the data in Redis with a random
            key and return the key."""
        uid = str(uuid.uuid4())
        self.__redis.set(uid, data)
        return uid
