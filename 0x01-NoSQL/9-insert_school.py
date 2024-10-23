#!/usr/bin/env python3
""" Python function that inserts a new document
    in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """ function that insert a document into a collection"""
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
