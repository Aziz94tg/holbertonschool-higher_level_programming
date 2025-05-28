#!/usr/bin/python3
"""Defines a class MyInt that inverts equality operators."""


class MyInt(int):
    """MyInt behaves like int, but inverts == and !=."""

    def __eq__(self, other):
        """Override ==."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override !=."""
        return super().__eq__(other)
