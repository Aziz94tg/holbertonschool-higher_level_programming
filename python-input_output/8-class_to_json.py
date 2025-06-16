#!/usr/bin/python3
"""Module that defines a function to convert an object to a dictionary
suitable for JSON serialization.
"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization
    of an object.
    """
    return obj.__dict__
