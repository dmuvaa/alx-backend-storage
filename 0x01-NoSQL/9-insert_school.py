#!/usr/bin/env python3


"""create a function"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection"""
    _id = mongo_collection.insert_one(kwargs).inserted_id
    return _id
