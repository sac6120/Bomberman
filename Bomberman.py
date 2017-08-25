""" This file contains the Bomberman class to be used in the game. """

from colorama import Fore, Style
from Person import Person

class Bomberman(Person):
    """ Bomberman is the Bomberman object in the game. """
    key_directions = {
        'a' : [0, -1],
        'w' : [-1, 0],
        's' : [1, 0],
        'd' : [0, 1],
    }
    def __init__(self, x, y):
        Person.__init__(self, x, y)

    def class_name(self):
        """ class_name returns the name of the class of this instance. """
        return "Bomberman"

    def design(self):
        """ design returns design array for Bomberman. """
        return [[Fore.YELLOW + Style.BRIGHT + '[', '^', '^', ']' + Style.RESET_ALL], [Fore.YELLOW + Style.BRIGHT + ' ', ']', '[', ' ' + Style.RESET_ALL]]

    def handle_input(self, instance_of_board, key):
        """ handle_input makes the Bomberman act according to the input. """
        if key[1] is True:
            instance_of_board.create_bomb(self.x_cord, self.y_cord)
        if key[0] == '':
            return
        xnew = self.x_cord + Bomberman.key_directions[key[0]][0]
        ynew = self.y_cord + Bomberman.key_directions[key[0]][1]
        if self.can_person_move_here(xnew, ynew, instance_of_board):
            self.move_person_here(xnew, ynew, instance_of_board)

    def is_on_enemy(self, instance_of_board):
        """ is_on_enemy checks whether Bomberman is on Enemy. """
        return instance_of_board.contains(self.x_cord, self.y_cord, 'Enemy')
