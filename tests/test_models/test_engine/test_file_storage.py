#!/usr/bin/python3
"""
Unittest for FileStorage class
"""


import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        """
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = "test_file.json"
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """
        Clean up method for each test case.
        """
        try:
            os.remove("test_file.json")
        except FileNotFoundError:
            pass
        del self.storage

    def test_all_method(self):
        """
        Test the all method of FileStorage class.
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_base_model(self):
        """
        Test the new method of FileStorage class with BaseModel.
        """
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_new_user(self):
        """
        Test the new method of FileStorage class with User.
        """
        obj = User()
        self.storage.new(obj)
        key = f"User.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_new_state(self):
        """
        Test the new method of FileStorage class with State.
        """
        obj = State()
        self.storage.new(obj)
        key = f"State.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_new_city(self):
        """
        Test the new method of FileStorage class with City.
        """
        obj = City()
        self.storage.new(obj)
        key = f"City.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_new_amenity(self):
        """
        Test the new method of FileStorage class with Amenity.
        """
        obj = Amenity()
        self.storage.new(obj)
        key = f"Amenity.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_new_place(self):
        """
        Test the new method of FileStorage class with Place.
        """
        obj = Place()
        self.storage.new(obj)
        key = f"Place.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_new_review(self):
        """
        Test the new method of FileStorage class with Review.
        """
        obj = Review()
        self.storage.new(obj)
        key = f"Review.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save_base_model(self):
        """
        Test the save method of FileStorage class with User.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as file:
            data = json.load(file)
            key = f"BaseModel.{obj.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key], obj.to_dict())

    def test_save_user(self):
        """
        Test the save method of FileStorage class with User.
        """
        obj = User()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as file:
            data = json.load(file)
            key = f"User.{obj.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key], obj.to_dict())

    def test_save_state(self):
        """
        Test the save method of FileStorage class with State.
        """
        obj = State()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as file:
            data = json.load(file)
            key = f"State.{obj.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key], obj.to_dict())

    def test_save_city(self):
        """
        Test the save method of FileStorage class with City.
        """
        obj = City()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as file:
            data = json.load(file)
            key = f"City.{obj.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key], obj.to_dict())

    def test_save_amenity(self):
        """
        Test the save method of FileStorage class with Amenity.
        """
        obj = Amenity()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as file:
            data = json.load(file)
            key = f"Amenity.{obj.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key], obj.to_dict())

    def test_save_place(self):
        """
        Test the save method of FileStorage class with Place.
        """
        obj = Place()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as file:
            data = json.load(file)
            key = f"Place.{obj.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key], obj.to_dict())

    def test_save_review(self):
        """
        Test the save method of FileStorage class with Review.
        """
        obj = Review()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as file:
            data = json.load(file)
            key = f"Review.{obj.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key], obj.to_dict())

    def test_reload_method(self):
        """
        Test the reload method of FileStorage class.
        """
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        self.storage.new(b)
        self.storage.new(u)
        self.storage.new(s)
        self.storage.new(c)
        self.storage.new(a)
        self.storage.new(r)
        self.storage.new(p)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(f"BaseModel.{b.id}", self.storage.all())
        self.assertIsInstance(
            self.storage.all()[f"BaseModel.{b.id}"], BaseModel)
        self.assertIn(f"User.{u.id}", self.storage.all())
        self.assertIsInstance(self.storage.all()[f"User.{u.id}"], User)
        self.assertIn(f"State.{s.id}", self.storage.all())
        self.assertIsInstance(self.storage.all()[f"State.{s.id}"], State)
        self.assertIn(f"City.{c.id}", self.storage.all())
        self.assertIsInstance(self.storage.all()[f"City.{c.id}"], City)
        self.assertIn(f"Amenity.{a.id}", self.storage.all())
        self.assertIsInstance(self.storage.all()[f"Amenity.{a.id}"], Amenity)
        self.assertIn(f"Place.{p.id}", self.storage.all())
        self.assertIsInstance(self.storage.all()[f"Place.{p.id}"], Place)
        self.assertIn(f"Review.{r.id}", self.storage.all())
        self.assertIsInstance(self.storage.all()[f"Review.{r.id}"], Review)

    def test_reload_no_file(self):
        """
        Test the reload method when no file exists.
        """
        try:
            os.remove("test_file.json")
        except FileNotFoundError:
            pass
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
