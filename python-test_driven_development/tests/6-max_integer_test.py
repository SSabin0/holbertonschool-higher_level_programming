#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function."""

    def test_ordered_list(self):
        """Test a list with ordered integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list with unordered integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where the max value is at the start."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test a list with only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list with negative integers."""
        self.assertEqual(max_integer([-1, -5, -2, -10]), -1)

    def test_identical_numbers(self):
        """Test a list with identical numbers."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_float_and_int(self):
        """Test a list containing both integers and floats."""
        self.assertEqual(max_integer([1.5, 3.2, 2.5]), 3.2)
