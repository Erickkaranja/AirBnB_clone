#!/usr/bin/env python3
'''initializing class HBNBCommand.'''

import cmd


class HBNBCommand(cmd.Cmd):
    '''implementing class HBNBCommand.'''
    prompt = '(hbnb) '

    def do_EOF(self, line):
        '''quits the program through an interrupt ctrl+D'''
        print ("")
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        print

    def postloop(self):
        print


if __name__ == '__main__':
    HBNBCommand().cmdloop()
