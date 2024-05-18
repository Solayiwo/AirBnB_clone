#!/usr/bin/python3
"""
Unittest for City class
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        """
        self.city = City()

    def tearDown(self):
        """
        Clean up method for each test case.
        """
        del self.city

    def test_instance_creation(self):
        """
        Test that a new instance of City is created correctly.
        """
        self.assertIsInstance(self.city, City)
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_attributes(self):
        """
        Test the attributes of City class.
        """
        self.city.state_id = "state_id_123"
        self.city.name = "San Francisco"
        self.assertEqual(self.city.state_id, "state_id_123")
        self.assertEqual(self.city.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
