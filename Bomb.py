""" This file contains the Bomb class to be used in the game. """
from colorama import Fore, Style

class Bomb(object):
    """ Bomb is the Bomb object in the game. """
    directions4 = {
        0 : [0, -1],
        1 : [-1, 0],
        2 : [1, 0],
        3 : [0, 1],
    }
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
        self.time_to_explode = 3

    def class_name(self):
        """ class_name returns the name of the class of this instance. """
        return "Bomb"

    def design(self):
        """ design return the design array for bomb. """
        return [[Fore.CYAN + str(self.time_to_explode), str(self.time_to_explode),
         str(self.time_to_explode), str(self.time_to_explode) + Style.RESET_ALL]] * 2

    def reduce_time_or_explode(self, instance_of_board):
        """ reduce_time_or_explode reduces bomb time or explodes it. """
        if not instance_of_board.contains(self.x_cord, self.y_cord, 'Bomberman'):
            self.time_to_explode = self.time_to_explode - 1
            if self.time_to_explode < 0:
                instance_of_board.create_explosion(self.x_cord, self.y_cord)
                for i in [1, 2]:
                    for direction in Bomb.directions4:
                        xnew = self.x_cord + i * Bomb.directions4[direction][0]
                        ynew = self.y_cord + i * Bomb.directions4[direction][1]
                        instance_of_board.create_explosion(xnew, ynew)
                instance_of_board.remove(self)
