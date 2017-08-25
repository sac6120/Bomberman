""" This file contains the Person class to be used in the game. """

class Person(object):
    """ Person is the Person object in the game. """
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y

    def class_name(self):
        """ class_name returns the name of the class of this instance. """
        return "Person"

    def can_person_move_here(self, xnew, ynew, instance_of_board):
        """ can_person_move_here checks if the Person can move on the given
        cell. """
        if abs(xnew - self.x_cord) + abs(ynew - self.y_cord) is not 1:
            return False
        if instance_of_board.contains(xnew, ynew, 'Wall'):
            return False
        if instance_of_board.contains(xnew, ynew, 'Brick'):
            return False
        if instance_of_board.contains(xnew, ynew, 'Bomb'):
            return False
        return True

    def move_person_here(self, xnew, ynew, instance_of_board):
        """ move_person_here moves the person on [xnew, ynew] cell. """
        instance_of_board.remove(self)
        instance_of_board.board[xnew][ynew].append(self)
        self.x_cord = xnew
        self.y_cord = ynew