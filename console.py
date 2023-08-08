#!/usr/bin/python3
import cmd
import json
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    intro = "Welcome to the HBNB command interpreter. \
        Type 'help' to list commands."

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
        except IndexError:
            if args[0] not in models.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            if args[0] not in models.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        if not arg:
            print([str(value) for key, value in models.storage.all().items()])
        else:
            if arg not in models.classes:
                print("** class doesn't exist **")
            else:
                print([str(value) for key, value in models.storage.all(
                ).items() if arg == key.split('.')[0]])

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in models.storage.all():
                instance = models.storage.all()[key]
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    if hasattr(instance, attr_name):
                        setattr(instance, attr_name, attr_value)
                        instance.save()
                    else:
                        print("** attribute doesn't exist **")
            else:
                print("** no instance found **")
        except IndexError:
            if args[0] not in models.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
