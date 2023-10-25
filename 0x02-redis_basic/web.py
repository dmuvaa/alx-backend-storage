#!/usr/bin/env python3

"""Import Some Modules"""

import requests
from cachetools import cached, TTLCache
from functools import wraps

"""create a python class"""


class WebPageFetcher:
    """A class to fetch web pages with caching and access counting."""

    def __init__(self, maxsize=100, ttl=10):
        self.cache = TTLCache(maxsize=maxsize, ttl=ttl)
        self.url_count = {}

    def count_access(func):
        """tracks the number of times the url is accessed"""
        @wraps(func)
        def wrapper(instance, *args, **kwargs):
            """function takes url as its first argument"""
            url = args[0]
            if url in instance.url_count:
                instance.url_count[url] += 1
            else:
                instance.url_count[url] = 1
            print(f"URL '{url}' has been accessed {instance.url_count[url]} times.")
            return func(instance, *args, **kwargs)
        return wrapper

    @count_access
    @cached(cache)
    def get_page(self, url: str) -> str:
        """function uses the requests module to get the HTML content of a URL"""
        response = requests.get(url)
        response.raise_for_status()
        return response.text
