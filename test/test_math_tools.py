"""Unittests for simple math tools."""

import unittest
from src.math_tools import triple, square


class TestMathToolkit(unittest.TestCase):
    def test_triple(self):
        """
        given an integer number as an input
        when the value is multiplied by 3
        then a value three times as large is returned.
        """
        self.assertEqual(triple(5), 15)
        self.assertEqual(triple(1), 3)
        self.assertEqual(triple(0), 0)
        with self.assertRaises(TypeError):
            triple('hello')

    def test_square(self):
        """
        given an integer number as an input
        when the value is multiplied by itself
        then a value of itself multiplied is returned.
        """
        self.assertEqual(square(5), 25)
        self.assertEqual(square(1), 1)
        self.assertEqual(square(0), 0)
        with self.assertRaises(TypeError):
            square('hello')

    def test_bug_652834(self):
        """Bug test pattern.

        Bug: square(-5) -> 0

        Build a new test case for the big. However make sure
        it fails to reproduce the test case, then make it succeed.

        given a negative integer number as
            an input
        when the value is multiplied by itself
        then a positive value of itself multiplied
            is returned.
        """
        self.assertEqual(square(-5), 25)

    def test_bug_652836(self):
        """Bug: square(-2.5) -> 0

        given a negative float number as an
            input
        when the value is multiplied by itself
        then a positive float value of itself
            multiplied is returned.
        """
        self.assertEqual(square(-2.5), 6.25)


if __name__ == '__main__':
    unittest.main()
