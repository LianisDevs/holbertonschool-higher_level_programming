#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This is the TestMaxInteger class

    Parameters: inherits unittest.TestCase
    """

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, "Empty list result should be None")

    def test_negative_positive_numbers(self):
        result = max_integer([1, -2, 3, -4])
        assert result == 3

    def test_positive_numbers(self):
        result = max_integer([1, 3, 4, 2])
        assert result == 4

    def test_negative_numbers(self):
        result = max_integer([-1, -3, -4, -2])
        assert result == -1

    def test_non_integers(self):
        with self.assertRaises(TypeError):
            result = max_integer(["a", 3, 4, 2])

    def test_string_list(self):
        result = max_integer(["a", "b", "c", "d"])
        assert result == "d"

    def test_list_one_element(self):
        result = max_integer([1])
        assert result == 1
