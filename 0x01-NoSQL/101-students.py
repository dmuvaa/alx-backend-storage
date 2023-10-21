#!/usr/bin/env python3

"""create a function"""


def top_students(mongo_collection):
    """function that returns all students sorted by average score"""
    pipeline = [{"$project": {"_id": 1, "name": 1,
                            "averageScore": {
                                "$avg": {
                                    "$avg": "$topics.score", },
                                }, "topics": 1, }, },
                {"$sort": {"averageScore": -1}, }, ]
    return list(mongo_collection.aggregate(pipeline))
