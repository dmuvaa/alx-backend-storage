#!/usr/bin/env python3

"""Import modules"""

import functools
import redis
from uuid import uuid4
from typing import Union, Callable, Optional, Any


"""create a function"""
def count_calls(method: Callable) -> Callable:
    """counts the number of times the method is called"""
    
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """function that increments the count in Redis for the given method"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """method that take a key string argument and an optional Callable argument"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Method that will automatically parametrize"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """method that with automatically parameterize int"""
        return self.get(key, fn=int)
