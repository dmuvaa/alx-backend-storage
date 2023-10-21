#!/usr/bin/env python3
""" tabulate logs """
from pymongo import MongoClient

# connect to MongoDB
client = MongoClient()
db = client.logs
collection = db.nginx

# count total number of logs
if __name__ == '__main__':
    total_logs = collection.count_documents({})
    # count number of logs with each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in http_methods:
        count = collection.count_documents({"method": method})
        method_counts[method] = count
    # count number of logs with method=GET and path=/status
    status_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
        })

    # print stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\t{method}: {count}")
    print(f"{status_count} status check")
