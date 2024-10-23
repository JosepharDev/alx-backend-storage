#!/usr/bin/env python3
from pymongo import MongoClient
""" list all document in a collection """


def list_all(mongo_collection):
    """ function take a colection and return all document in it """

    return mongo_collection.find()
