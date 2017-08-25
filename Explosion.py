""" This file contains the Explosion class to be used in the game. """

class Explosion(object):
    """ Explosion is the explosion object in the game. """
    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def design(self):
        """ design returns the design list for Wall object. """
        return [['^'] * 4] * 2
