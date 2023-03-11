#!/usr/bin/env python3
'''initializing class HBNBCommand.'''

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    '''implementing class HBNBCommand.'''

    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        '''ignores empty prompts.'''
        pass

    def default(self, arg):
        '''default behavior of the cmd upon receiving invalid input.'''
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** uknown syntax: {}".format(arg))
        return False

    def do_EOF(self, arg):
        '''quits the program through an interrupt ctrl+D'''
        print ("")
        return True

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_create(self, arg):
        '''usage: create <class>
        Creates a new class instance and prints its id.
        '''
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        '''usage: show <class> <id> or <class>.show(<id>)
        Displays the string representation of a class given id.
        '''
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("")
        elif argl[0] not in HBNBCommand.__classes:
            print("")
        elif len(argl) == 1:
            print("")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        '''usage destroy <class> <id> or <class>.destroy(<id>)
        Deletes a classs istance of a given id.
        '''
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("")
        elif argl[0] not in HBNBCommand.__classes:
            print("")
        elif len(argl) == 1:
            print("")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
