#!/usr/bin/python3
"""
Unittest for the console (command interpreter)
"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import json


class TestConsole(unittest.TestCase):
    """
    Test cases for the console
    """

    def setUp(self):
        """
        Set up method for each test case.
        """
        storage._FileStorage__file_path = "test_file.json"
        storage._FileStorage__objects = {}
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")

    def tearDown(self):
        """
        Clean up method for each test case.
        """
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")

    def test_quit(self):
        """
        Test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """
        Test EOF command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_help(self):
        """
        Test help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands", f.getvalue())

    def test_emptyline(self):
        """
        Test empty line input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """
        Test create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            base_model_id = f.getvalue().strip()
            self.assertIn(f"BaseModel.{base_model_id}", storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertIn(f"User.{user_id}", storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            state_id = f.getvalue().strip()
            self.assertIn(f"State.{state_id}", storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            city_id = f.getvalue().strip()
            self.assertIn(f"City.{city_id}", storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            self.assertIn(f"Amenity.{id}", storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            self.assertIn(f"Place.{id}", storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            self.assertIn(f"Review.{id}", storage.all().keys())

    def test_show(self):
        """
        Test show command
        """
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(r)
        storage.new(p)
        storage.save()
        storage.reload()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {u.id}")
            self.assertIn(u.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {b.id}")
            self.assertIn(b.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {s.id}")
            self.assertIn(s.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City {c.id}")
            self.assertIn(c.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity {a.id}")
            self.assertIn(a.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {p.id}")
            self.assertIn(p.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review {r.id}")
            self.assertIn(r.id, f.getvalue().strip())

    def test_destroy(self):
        """
        Test destroy command
        """
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(r)
        storage.new(p)
        storage.save()
        storage.reload()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {b.id}")
            self.assertNotIn(f"BaseModel.{b.id}", storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {u.id}")
            self.assertNotIn(f"User.{u.id}", storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy State {s.id}")
            self.assertNotIn(f"State.{s.id}", storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy City {c.id}")
            self.assertNotIn(f"City.{c.id}", storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Amenity {a.id}")
            self.assertNotIn(f"Amenity.{a.id}", storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Place {p.id}")
            self.assertNotIn(f"Place.{p.id}", storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Review {r.id}")
            self.assertNotIn(f"Review.{r.id}", storage.all().keys())

    def test_all(self):
        """
        Test all command
        """
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(r)
        storage.new(p)
        storage.save()
        storage.reload()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all User")
            self.assertIn(u.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all BaseModel")
            self.assertIn(b.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all State")
            self.assertIn(s.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all City")
            self.assertIn(c.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all Amenity")
            self.assertIn(a.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all Place")
            self.assertIn(p.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all Review")
            self.assertIn(r.id, f.getvalue().strip())

    def test_update(self):
        """
        Test update command
        """
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(r)
        storage.new(p)
        storage.save()
        storage.reload()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update BaseModel {b.id} first_name "John"')
            HBNBCommand().onecmd(f"show BaseModel {b.id}")
            self.assertIn("John", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update User {u.id} first_name "John"')
            HBNBCommand().onecmd(f"show User {u.id}")
            self.assertIn("John", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update State {s.id} name "Congo"')
            HBNBCommand().onecmd(f"show State {s.id}")
            self.assertIn("Congo", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update City {c.id} name "Brazzaville"')
            HBNBCommand().onecmd(f"show City {c.id}")
            self.assertIn("Brazzaville", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Amenity {a.id} city_id "{c.id}"')
            HBNBCommand().onecmd(f"show Amenity {a.id}")
            self.assertIn(c.id, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Place {p.id} city_id "{c.id}"')
            HBNBCommand().onecmd(f"show Place {p.id}")
            self.assertIn(c.id, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Review {r.id} user_id "{u.id}"')
            HBNBCommand().onecmd(f"show Review {r.id}")
            self.assertIn(u.id, f.getvalue().strip())

    def test_default_all(self):
        """
        Test <class_name>.all() command
        """
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(r)
        storage.new(p)
        storage.save()
        storage.reload()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.all()")
            self.assertIn(u.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.all()")
            self.assertIn(b.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.all()")
            self.assertIn(s.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.all()")
            self.assertIn(c.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.all()")
            self.assertIn(a.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.all()")
            self.assertIn(p.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.all()")
            self.assertIn(r.id, f.getvalue().strip())

    def test_count(self):
        """
        Test count command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(f.getvalue().strip(), "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(f.getvalue().strip(), "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual(f.getvalue().strip(), "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual(f.getvalue().strip(), "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(f.getvalue().strip(), "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual(f.getvalue().strip(), "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual(f.getvalue().strip(), "0")

        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(r)
        storage.new(p)
        storage.save()
        storage.reload()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(f.getvalue().strip(), "1")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(f.getvalue().strip(), "1")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual(f.getvalue().strip(), "1")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual(f.getvalue().strip(), "1")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(f.getvalue().strip(), "1")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual(f.getvalue().strip(), "1")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual(f.getvalue().strip(), "1")

    def test_default_show(self):
        """
        Test <class name>.show(<id>) command
        """
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(r)
        storage.new(p)
        storage.save()
        storage.reload()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.show("{u.id}")')
            self.assertIn(u.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.show("{b.id}")')
            self.assertIn(b.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'State.show("{s.id}")')
            self.assertIn(s.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'City.show("{c.id}")')
            self.assertIn(c.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Amenity.show("{a.id}")')
            self.assertIn(a.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Place.show("{p.id}")')
            self.assertIn(p.id, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Review.show("{r.id}")')
            self.assertIn(r.id, f.getvalue().strip())

    def test_default_destroy(self):
        """
        Test <class name>.destroy(<id>) command
        """
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(r)
        storage.new(p)
        storage.save()
        storage.reload()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.destroy("{u.id}")')
            self.assertNotIn(u.id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.destroy("{b.id}")')
            self.assertNotIn(b.id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'State.destroy("{s.id}")')
            self.assertNotIn(s.id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'City.destroy("{c.id}")')
            self.assertNotIn(c.id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Amenity.destroy("{a.id}")')
            self.assertNotIn(a.id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Place.destroy("{p.id}")')
            self.assertNotIn(p.id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Review.destroy("{r.id}")')
            self.assertNotIn(r.id, storage.all().keys())

    def test_default_update_with_dict(self):
        """
        Test <class name>.update(<id>, <dictionary>) command
        """
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(r)
        storage.new(p)
        storage.save()
        storage.reload()
        t = f'BaseModel.update("{b.id}", {{"first_name": "John", "age": 30}})'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(t)
            HBNBCommand().onecmd(f"show BaseModel {b.id}")
            output = f.getvalue().strip()
            self.assertIn("John", output)
            self.assertIn("30", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'User.update("{u.id}", {{"first_name": "John", "age": 30}})')
            HBNBCommand().onecmd(f"show User {u.id}")
            output = f.getvalue().strip()
            self.assertIn("John", output)
            self.assertIn("30", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'State.update("{s.id}", {{"name": "Congo"}})')
            HBNBCommand().onecmd(f"show State {s.id}")
            output = f.getvalue().strip()
            self.assertIn("Congo", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'City.update("{c.id}", {{"name": "Congo"}})')
            HBNBCommand().onecmd(f"show City {c.id}")
            output = f.getvalue().strip()
            self.assertIn("Congo", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'Amenity.update("{a.id}", {{"name": "Siaf"}})')
            HBNBCommand().onecmd(f"show Amenity {a.id}")
            output = f.getvalue().strip()
            self.assertIn("Siaf", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'Place.update("{p.id}", {{"name": "Congo"}})')
            HBNBCommand().onecmd(f"show Place {p.id}")
            output = f.getvalue().strip()
            self.assertIn("Congo", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'Review.update("{r.id}", {{"comment": "Good"}})')
            HBNBCommand().onecmd(f"show Review {r.id}")
            output = f.getvalue().strip()
            self.assertIn("Good", output)


if __name__ == '__main__':
    unittest.main()
