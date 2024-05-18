#!/usr/bin/python3
"""
Unittest for State class
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        """
        self.state = State()

    def tearDown(self):
        """
        Clean up method for each test case.
        """
        del self.state

    def test_instance_creation(self):
        """
        Test that a new instance of State is created correctly.
        """
        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "")

    def test_attributes(self):
        """
        Test the attributes of State class.
        """
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")


if __name__ == '__main__':
    unittest.main()
