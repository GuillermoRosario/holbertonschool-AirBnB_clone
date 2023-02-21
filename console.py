#!/usr/bin/python3
"""
Command Interpreter Interface
"""

import cmd


class HBNBCommand(cmd.Cmd):

    """This is my HNBB Class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True
    
    def close(self):
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        self.close()
        print()
        quit()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()