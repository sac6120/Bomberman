""" This file contains the Enemy class to be used in the game. """

from colorama import Fore, Style
from Person import Person
import random

class Enemy(Person):

    directions4 = {
        0 : [0, -1],
        1 : [-1, 0],
        2 : [1, 0],
        3 : [0, 1],
    }

    def __init__(self, x, y):
        from Bomberman import Bomberman
        Person.__init__(self, x, y)
        self.straight_time = -1
        self.direction = -1
    
    def class_name(self):
        """ class_name returns the name of the class of this instance. """
        return "Enemy"
    
    def design(self):
        return [[Fore.GREEN + '-', '@', '@', '-' + Style.RESET_ALL], [Fore.BLUE + Style.BRIGHT +  ' ', 'v', 'v', ' ' + Style.RESET_ALL]] 

    def check_enemy_on_bomberman(self, instance_of_board):
        for i in instance_of_board.board[self.x_cord][self.y_cord]:
            if isinstance(i, Bomberman):
                return True
        return False

    def _assign_direction(self, instance_of_board):
        directions = range(4)
        random.shuffle(directions)
        for direct in directions:
            if direct is not self.direction:
                xnew = self.x_cord + Enemy.directions4[direct][0]
                ynew = self.y_cord + Enemy.directions4[direct][1]
                if self.can_person_move_here(xnew, ynew, instance_of_board):
                    self.direction = direct
                    self.straight_time = random.randint(0, 6)
                    break

    def random_move_enemy(self, instance_of_board):

        if self.direction == -1:
            self._assign_direction(instance_of_board)

        if self.direction == -1:
            return

        if self.straight_time < 0:
            self._assign_direction(instance_of_board)

        xnew = self.x_cord + Enemy.directions4[self.direction][0]
        ynew = self.y_cord + Enemy.directions4[self.direction][1]
        if not self.can_person_move_here(xnew, ynew, instance_of_board):
            self._assign_direction(instance_of_board)

        xnew = self.x_cord + Enemy.directions4[self.direction][0]
        ynew = self.y_cord + Enemy.directions4[self.direction][1]
        if self.can_person_move_here(xnew, ynew, instance_of_board):
            self.move_person_here(xnew, ynew, instance_of_board)
            
        self.straight_time = self.straight_time - 1