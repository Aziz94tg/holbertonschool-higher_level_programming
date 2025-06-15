#!/usr/bin/python3
"""Module that returns the JSON representation."""


import json


def to_json_string(my_obj):
    """Returns the JSON representation."""
    return json.dumps(my_obj)
