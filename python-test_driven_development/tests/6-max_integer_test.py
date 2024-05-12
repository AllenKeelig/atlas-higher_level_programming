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
    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m), 360)
    def test_one_negative(self):
        """Tests for list with one negative number"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)
    def test_empty_list(self):
        """Tests for empty list []"""
        e = []
        self.assertIsNone(max_integer(e))
    def test_one_element(self):
        """Tests for only one number in the list"""
        o = [1]
        self.assertEqual(max_integer(o), 1)
