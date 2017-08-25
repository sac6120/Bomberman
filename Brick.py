""" This file contains the Brick class to be used in the game. """
from colorama import Fore, Style

class Brick(object):
    """ Brick is the Brick object in the game. """
    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def design(self):
        """ design returns the design list for Wall object. """
        return [[Fore.RED + Style.BRIGHT + '/', '/', '/', '/' +
         Style.RESET_ALL], [Fore.RED + Style.BRIGHT + '/', '/',
         '/', '/' + Style.RESET_ALL]]
