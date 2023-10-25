#!/usr/bin/env python3

"""Import Some Modules"""

import requests
from cachetools import cached, TTLCache
from functools import wraps

cache = TTLCache(maxsize=100, TTL=10)

url_count = {}

"""create a python class"""


def count_access(func):
    """tracks the number of times the url is accessed"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """function takes url as its first argument"""
        url = args[0]
        if url in url_count:
            url_count[url] += 1
        else:
            url_count[url] = 1
        print(f"URL '{url}' has been accessed {url_count[url]} times.")
        return func(*args, **kwargs)
    return wrapper


@count_access
@cached(cache)
def get_page(url: str) -> str:
    """function uses the requests module to get the HTML content of a URL"""
    response = requests.get(url)
    response.raise_for_status()
    return response.text
