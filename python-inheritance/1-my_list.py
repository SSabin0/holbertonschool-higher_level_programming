#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list with extended printing capabilities."""

    def print_sorted(self):
        """Prints the list elements sorted in ascending order."""
        print(sorted(self))
