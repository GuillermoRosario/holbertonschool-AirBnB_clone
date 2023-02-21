#!/usr/bin/python3
"""
Command Interpreter OFFICIAL
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """This is my HNBB Class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True
    
    def close(self):
        """Close command"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        self.close()
        print()
        quit()

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
