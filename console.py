#!/usr/bin/python3

"""
Command Interpreter
"""

import cmd 
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

def do_quit(self, arg):
    'Quit command to exit the program\n'
    return True

def close(self):
    return True

def do_EOF(self, arg):
    'EOF command to exit the program'
    self.close()
    print()
    quit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()   