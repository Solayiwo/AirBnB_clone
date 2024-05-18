#!/usr/bin/python3
"""
Unittest for Amenity class
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up method for each test case.
        """
        del self.amenity

    def test_instance_creation(self):
        """
        Test that a new instance of Amenity is created correctly.
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(self.amenity.name, "")

    def test_attributes(self):
        """
        Test the attributes of Amenity class.
        """
        self.amenity.name = "WiFi"
        self.assertEqual(self.amenity.name, "WiFi")


if __name__ == '__main__':
    unittest.main()
