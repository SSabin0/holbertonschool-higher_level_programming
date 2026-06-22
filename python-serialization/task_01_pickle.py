#!/usr/bin/env python3
"""
Module for serializing and deserializing custom objects using pickle.
"""
import pickle


class CustomObject:
    """A custom class representing a person with serialization capabilities."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes the CustomObject with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes in a specific format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance and saves it to a binary file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes a binary file and returns an instance of CustomObject.
        
        Returns None if the file does not exist or is malformed.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
        except Exception:
            return None
