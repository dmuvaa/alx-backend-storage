#!/usr/bin/env python3

"""Import modules"""

import redis
from uuid import uuid4
from typing import Union


"""Create a Class"""


class Cache:
    """class for writing strings to Redis"""
    def __init__(self):
        """function for initiating strings"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that creates a store"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
