#!/usr/bin/python3
"""
Command Interpreter Interface
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n """
        return True

    def do_EOF(self, arg):
        """ EOF is added """
        print()
        return True

    def emptyline(self):
        """empty line if no command is given"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()