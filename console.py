#!/usr/bin/python3
"""
Console module for managing objects in the HBNB application.

This module provides a command-line interface (CLI) for interacting with the
HBNB application. It supports commands for creating, showing, updating,
deleting, and listing instances of BaseModel.

Usage:
    Run this module as a standalone script to start the interactive CLI.
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


class HBNBCommand(cmd.Cmd):
    """
    Command-line interface for managing objects in the HBNB application.

    Args:
        cmd.Cmd: The base class for implementing command-line interpreters.
    """

    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        }

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it \
            (to the JSON file) and prints the id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an \
            instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            else:
                print(instances[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id \
            (save the change into the JSON file)"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            else:
                del instances[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or \
            not on the class name"""
        args = arg.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            result = []
            for key in instances:
                obj = instances[key]
                if len(args) == 0 or obj.__class__.__name__ == args[0]:
                    result.append(str(obj))
            print(result)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or \
            updating attribute (save the change into the JSON file)"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = instances[key]
                attr_name = args[2]
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    attr_value = attr_type(args[3].strip('"'))
                else:
                    attr_value = args[3].strip('"')
                setattr(obj, attr_name, attr_value)
                obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
