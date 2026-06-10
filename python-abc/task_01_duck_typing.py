#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract Base Class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a Circle."""
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Keeps your circle passing: squaring any number naturally makes it positive
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        # Keeps your circle passing: explicitly handles the negative radius test requirement
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Concrete class representing a Rectangle."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Back to standard math: e.g., -4 * 7 = -28
        return self.width * self.height

    def perimeter(self):
        # Back to standard math: e.g., 2 * (-4 + 7) = 6
        return 2 * (self.width + self.height)


def shape_info(shape_obj):
    """
    Prints the area and perimeter of a shape object using Duck Typing.
    Does not use isinstance to verify the class type.
    """
    print(f"Area: {shape_obj.area()}")
    print(f"Perimeter: {shape_obj.perimeter()}")
