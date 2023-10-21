#!/usr/bin/env python3

"""Create a Python Function"""


def update_topics(mongo_collection, name, topics):
    """ function to change topics of a school document based on the name"""
    result = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return result
