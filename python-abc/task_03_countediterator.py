#!/usr/bin/env python3
"""
Module containing the CountedIterator class that wraps an iterator
and counts how many items have been successfully retrieved.
"""


class CountedIterator:
    """An iterator wrapper that keeps track of the number of items fetched."""

    def __init__(self, iterable):
        """Initializes the iterator object and the iteration counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Returns the current number of items that have been iterated."""
        return self.counter

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the counter.
        Raises StopIteration if there are no items left.
        """
        # Fetch the item first. If it raises StopIteration, the function 
        # ends here and the counter will not increment incorrectly.
        item = next(self.iterator)
        
        # If successfully fetched, increment the counter and return the item.
        self.counter += 1
        return item

    def __iter__(self):
        """Returns the iterator object itself to support standard iteration."""
        return self
