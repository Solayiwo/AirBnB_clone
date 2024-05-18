#!/usr/bin/python3
"""
Unittest for BaseModel class
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestCBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up for each test case."""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up method for each test case."""
        del self.model

    def test_instance_creation(self):
        """
        Test that a new instance of BaseModel is created correctly.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_unique_id(self):
        """
        Test that each instance of BaseModel has a unique id.
        """
        model1 = BaseModel()
        self.assertNotEqual(self.model.id, model1.id)
        del model1

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel class.
        """
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """
        Test the save method of the BaseModel class.
        """
        old_date = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_date, self.model.updated_at)
        self.assertTrue(
            (self.model.updated_at - self.model.created_at).total_seconds() >= 0)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_kwargs_instance(self):
        """
        Test creating an instance with keyword arguments.
        """
        model_dict = self.model.to_dict()
        model1 = BaseModel(**model_dict)
        self.assertEqual(self.model.id, model1.id)
        self.assertEqual(self.model.created_at, model1.created_at)
        self.assertEqual(self.model.updated_at, model1.updated_at)
        self.assertEqual(self.model.__str__(), model1.__str__())
        del model1
