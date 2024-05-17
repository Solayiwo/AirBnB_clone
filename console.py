#!/usr/bin/python3
"""
Console module
Entry point of the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """

    prompt = '(hbnb) '

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

        if args[0] not in ['BaseModel']:
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
            if arg not in ['BaseModel']:
                print("** class doesn't exist **")
                return

            instances = [str(obj) for obj in storage.all(
            ).values() if type(obj).__name__ == arg]
        else:
            instances = [str(obj) for obj in storage.all().values()]

        print(instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
