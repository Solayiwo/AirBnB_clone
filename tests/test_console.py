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

    def test_create(self):
        """
        Test create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertIn(f"User.{user_id}", storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show(self):
        """
        Test show command
        """
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user.id}")
            self.assertIn(user.id, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show InvalidClass 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy(self):
        """
        Test destroy command
        """
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user.id}")
            self.assertNotIn(user.id, storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy InvalidClass 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all(self):
        """
        Test all command
        """
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertIn(user.id, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update(self):
        """
        Test update command
        """
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update User {user.id} first_name "John"')
            HBNBCommand().onecmd(f"show User {user.id}")
            self.assertIn("John", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user.id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user.id} first_name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update InvalidClass 1234 name 'value'")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 1234 name 'value'")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_count(self):
        """
        Test count command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(f.getvalue().strip(), "0")

        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(f.getvalue().strip(), "1")

    def test_default_show(self):
        """
        Test <class name>.show(<id>) command
        """
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.show("{user.id}")')
            self.assertIn(user.id, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.show("1234")')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_default_destroy(self):
        """
        Test <class name>.destroy(<id>) command
        """
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.destroy("{user.id}")')
            self.assertNotIn(user.id, storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.destroy("1234")')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_default_update_with_dict(self):
        """
        Test <class name>.update(<id>, <dictionary>) command
        """
        user = User()
        user.save()
        data = {"first_name": "John", "age": 30}
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.update("{user.id}", {data})')
            HBNBCommand().onecmd(f"show User {user.id}")
            output = f.getvalue().strip()
            self.assertIn("John", output)
            self.assertIn("30", output)


if __name__ == '__main__':
    unittest.main()
