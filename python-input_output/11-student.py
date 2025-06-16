#!/usr/bin/python3
"""Defines a class Student with JSON serialization/deserialization capability.
"""


class Student:
    """Represents a student with public instance attributes."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.

        Args:
            attrs: List of strings to filter attributes to include.

        Returns:
            dict: Dictionary of selected or all attributes.
        """
        if isinstance(attrs, list) and \
           all(isinstance(attr, str) for attr in attrs):
            return {
                key: self.__dict__[key]
                for key in attrs if key in self.__dict__
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dictionary.

        Args:
            json: A dictionary of new attributes to set.
        """
        for key, value in json.items():
            setattr(self, key, value)
