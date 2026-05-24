#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the side of the square.
        """
        self.__size = size
