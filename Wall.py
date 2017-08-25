""" This file contains the Wall class to be used in the game. """
from colorama import Fore, Style

class Wall(object):
    """ Wall is the wall object in the game. """
    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def class_name(self):
        """ class_name returns the name of the class of this instance. """
        return "Wall"

    def design(self):
        """ design returns the design list for Wall object. """
        return [[Fore.WHITE + '#', '#', '#', '#' + Style.RESET_ALL],
         [Fore.WHITE + '#', '#', '#', '#' + Style.RESET_ALL]]
