#!/usr/bin/python3
"""
Unittest for Place class
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        """
        self.place = Place()

    def tearDown(self):
        """
        Clean up method for each test case.
        """
        del self.place

    def test_instance_creation(self):
        """
        Test that a new instance of Place is created correctly.
        """
        self.assertIsInstance(self.place, Place)
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attributes(self):
        """
        Test the attributes of Place class.
        """
        self.place.city_id = "city_id_123"
        self.place.user_id = "user_id_123"
        self.place.name = "My Place"
        self.place.description = "A nice place to stay"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 5
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = -122.4194
        self.place.amenity_ids = ["amenity_1", "amenity_2"]
        self.assertEqual(self.place.city_id, "city_id_123")
        self.assertEqual(self.place.user_id, "user_id_123")
        self.assertEqual(self.place.name, "My Place")
        self.assertEqual(self.place.description, "A nice place to stay")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 5)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.amenity_ids, ["amenity_1", "amenity_2"])


if __name__ == '__main__':
    unittest.main()
