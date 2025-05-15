#!/usr/bin/python3
"""
This module defines a function that print My name is
<first_name> <last_name>.
"""

def say_my_name(first_name, last_name=""):
     """
    Prints a first name and a last name.

    Args:
        First name.
        Last name.

    Returns:
        My name is <first_name> <last_name>.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
    return
