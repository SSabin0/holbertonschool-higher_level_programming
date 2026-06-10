#!/usr/bin/env python3
"""
Module containing the VerboseList class that extends the built-in list
to print notification messages on modifications.
"""


class VerboseList(list):
    """A custom list that prints notifications when items are modified."""

    def append(self, item):
        """Adds an item to the end of the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        """Extends the list by appending elements from the iterable."""
        num_items = len(x)
        super().extend(x)
        print(f"Extended the list with [{num_items}] items.")

    def remove(self, item):
        """Removes the first occurrence of a value from the list."""
        # Print the message before attempting removal as requested
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Removes and returns the item at the given index (default last)."""
        # Look up the item before popping to display it in the print statement
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
