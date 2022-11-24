#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_arg(self):
        """to test for various arguments"""
        self.assertAlmostEqual(max_integer([], None))
        self.assertAlmostEqual(max_integer([2, 3, 4, 5, 6], 6))
        self.assertAlmostEqual(max_integer([2, 4, 6, 6, 8], 8))
        self.assertAlmostEqual(max_integer([5], 5))
        self.assertAlmostEqual(max_integer([2.5, 3.8, 7, 8.3], 8.3))

    def test_argType(self):
        self.assertRaises(TypeError, max_integer, [2, 3, 6, 'sring'])
        self.assertRaises(TypeError, max_integer, [2, 3, 6, (8, 7, 9)])
        self.assertRaises(TypeError, max_integer, [2, 3, 6, 2 + 5j])
        self.assertRaises(TypeError, max_integer, [2, 3, 6,], [7, 8, 9])
        self.assertRaises(TypeError, max_integer, [2, 3, 6, {'no': 8, 'yes': 12}])
