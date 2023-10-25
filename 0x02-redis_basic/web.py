import requests
from functools import wraps
from time import time

# Dictionary to cache the result and track expiration
cache_dict = {}

# Dictionary to store counts of URL accesses
url_count = {}

def cache(ttl=10):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            url = args[0]
            current_time = time()
            
            if url in cache_dict and (current_time - cache_dict[url]["time"]) <= ttl:
                print(f"Fetching cached data for URL: {url}")
                return cache_dict[url]["data"]
            
            result = func(*args, **kwargs)
            cache_dict[url] = {"data": result, "time": current_time}
            return result
        return wrapper
    return decorator

def count_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        url = args[0]
        
        if f"count:{url}" in url_count:
            url_count[f"count:{url}"] += 1
        else:
            url_count[f"count:{url}"] = 1
        
        print(f"URL '{url}' has been accessed {url_count[f'count:{url}']} times.")
        return func(*args, **kwargs)
    return wrapper

@count_access
@cache(ttl=10)
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Test the function
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/2000/url/http://www.google.com"
    print(get_page(url))  # Should print the content and count
    print(get_page(url))  # Should fetch from cache and update count

