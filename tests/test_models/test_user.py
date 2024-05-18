#!/usr/bin/python3
"""
Unittest for User class
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        """
        self.user = User()

    def tearDown(self):
        """
        Clean up method for each test case.
        """
        del self.user

    def test_instance_creation(self):
        """
        Test that a new instance of User is created correctly.
        """
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attributes(self):
        """
        Test the attributes of User class.
        """
        self.user.email = "user@example.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
