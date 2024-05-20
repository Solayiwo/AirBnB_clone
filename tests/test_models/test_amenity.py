#!/usr/bin/python3
"""
Unittest for Amenity class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


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
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)
        self.assertEqual(self.amenity.name, "")

    def test_attributes(self):
        """
        Test the attributes of Amenity class.
        """
        self.amenity.name = "WiFi"
        self.assertEqual(self.amenity.name, "WiFi")
        self.assertEqual(type(self.amenity.name), str)

    def test_has_attributes(self):
        "Test Test the attributes of Amenity class. "
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)

    def test_save(self):
        """Test save method"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == '__main__':
    unittest.main()
