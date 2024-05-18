#!/usr/bin/python3
"""
Console module
Entry point of the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """

    prompt = '(hbnb) '
    models_dict = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'Place': Place, 'City': City, 'Amenity': Amenity, 'Review': Review}

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line input."""
        pass

    def do_create(self, cls):
        """
        Creates a new instance of BaseModel, saves it and prints the id
        Usage: create <class name>
        """
        if not cls:
            print("** class name missing **")
            return

        try:
            new_instance = eval(cls)()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.models_dict.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        if arg:
            if arg not in self.models_dict.keys():
                print("** class doesn't exist **")
                return

            instances = [str(obj) for obj in storage.all(
            ).values() if type(obj).__name__ == arg]
        else:
            instances = [str(obj) for obj in storage.all().values()]

        print(instances)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id, and saves the change.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.models_dict.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3].strip('"')

        # Check if the attribute exists and cast to the correct type
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            setattr(instance, attr_name, attr_type(attr_value))
        else:
            setattr(instance, attr_name, attr_value)

        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
