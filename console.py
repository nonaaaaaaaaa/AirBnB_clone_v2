#!/usr/bin/python3
"""here is the console that user should interact with"""

import cmd
import models.engine
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """class defintion"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    classes = {"User": User, "State": State, "BaseModel": BaseModel,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        args = arg.split(' ')

        if not args[0]:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if not args or len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return

        rtrn = models.storage.all()
        if args[0] + '.' + args[1] not in rtrn:
            print("** no instance found **")
            return
        print(rtrn.get(args[0] + '.' + args[1]))

    def do_destroy(self, arg):
        args = arg.split(' ')

        if not args[0]:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if not args or len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return
        if args[0] + '.' + args[1] not in storage.all():
            print("** no instance found **")
            return
        del_instance = args[0] + '.' + args[1]
        del storage.all()[del_instance]
        storage.save()

    def do_all(self, arg):
        args = arg.split(' ')
        rtrn = models.storage.all()
        list_all = []

        if not arg:
            for i in rtrn.values():
                list_all.append(str(i))
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for i in rtrn.values():
                list_all.append(str(i))
        print(list_all)

    def do_update(self, arg):
        args = arg.split()
        objects = storage.all()

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("** no instance found **")
            else:
                obj = objects[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save


if __name__ == '__main__':
    HBNBCommand().cmdloop()
