#!/usr/bin/env python3
"""
Module demonstrating the Mixin design pattern in Python
using SwimMixin, FlyMixin, and a composite Dragon class.
"""


class SwimMixin:
    """Mixin class that provides swimming functionality."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying functionality."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that composes behaviors from both SwimMixin and FlyMixin,
    in addition to its own unique actions.
    """

    def roar(self):
        print("The dragon roars!")
