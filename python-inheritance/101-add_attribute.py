#!/usr/bin/python3
"""Defines a function that adds an attribute to an object."""


def add_attribute(obj, attr_name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add an attribute to.
        attr_name: The name of the attribute to add.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
