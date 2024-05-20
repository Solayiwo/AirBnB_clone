#!/usr/bin/python3
"""
Unittest for Review class
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        """
        self.review = Review()

    def tearDown(self):
        """
        Clean up method for each test case.
        """
        del self.review

    def test_instance_creation(self):
        """
        Test that a new instance of Review is created correctly.
        """
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attributes(self):
        """
        Test the attributes of Review class.
        """
        self.review.place_id = "place_id_123"
        self.review.user_id = "user_id_123"
        self.review.text = "This is a great place!"
        self.assertEqual(self.review.place_id, "place_id_123")
        self.assertEqual(self.review.user_id, "user_id_123")
        self.assertEqual(self.review.text, "This is a great place!")


if __name__ == '__main__':
    unittest.main()
