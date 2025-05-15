#!/usr/bin/python3
"""
This module defines a function that prints a text
with 2 new lines after '.', '?', and ':' characters.
"""


def text_indentation(text):
    """
    Prints text with two newlines after each '.', '?', or ':'.

    Args:
        text: The input string to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1

            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
