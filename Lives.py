""" This file contains the Lives class to be used in the game. """

class Lives(object):
    """ Lives is the Lives object in the game. """
    def __init__(self):
        self.lives = 3

    def update_lives(self):
        """ updateLives is called when the Bomberman hits an enemy or
        the explosion. """
        self.lives = self.lives - 1
