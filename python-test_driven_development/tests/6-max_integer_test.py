#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_positive_end(self):
        """Tests for all positive with max at end"""
        e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(e), 50)
    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)
