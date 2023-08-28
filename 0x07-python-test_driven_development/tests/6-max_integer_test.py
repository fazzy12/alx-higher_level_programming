#!/usr/bin/python3
"""
test for the def max_integer(list=[]): function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """"Test suites for TestMaxInt function"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-10]), -10)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 3, 2, 8, 5]), 8)
        self.assertEqual(max_integer([10, 5, 15, 20]), 20)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-3, -7, -2, -10]), -2)
        self.assertEqual(max_integer([-5, -2, -1]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10)
        self.assertEqual(max_integer([-5, 0, 5, -10, -2]), 5)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
        self.assertEqual(max_integer([-4, -4, -4]), -4)

    def test_large_list(self):
        lst = list(range(1, 10001))
        self.assertEqual(max_integer(lst), 10000)

    def test_mixed_large_list(self):
        lst = list(range(-5000, 5001))
        self.assertEqual(max_integer(lst), 5000)

    def test_reversed_list(self):
        lst = list(range(10, 0, -1))
        self.assertEqual(max_integer(lst), 10)

    def test_strings_in_list(self):
        lst = [1, 2, '3', 4, 5]
        with self.assertRaises(TypeError):
            max_integer(lst)

    def test_none_in_list(self):
        lst = [1, 2, None, 4, 5]
        with self.assertRaises(TypeError):
            max_integer(lst)    
