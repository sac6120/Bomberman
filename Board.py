""" This file contains the Board class to be used in the game. """

import random
from colorama import Back, Style
from Wall import Wall
from Bomberman import Bomberman
from Brick import Brick
from Enemy import Enemy
from Bomb import Bomb
from Explosion import Explosion

class Board(object):
    """ Board is the Board object in the game. """
    def __init__(self):
        self.row = 21
        self.col = 21
        self.cell_row = 2
        self.cell_col = 4
        self.bricks_count = 50
        self.enemy_count = 5
        self.board = self.generate_board()

    def class_name(self):
        """ class_name returns the name of the class of this instance. """
        return "Board"

    def generate_board(self):
        """ generate_board generates the board to be used in the game. """
        to_return = []
        for i in range(self.row):
            curr_row = []
            for j in range(self.col):
                if i % 2 == 0 and j % 2 == 0:
                    curr_row.append([Wall(i, j)])
                else:
                    curr_row.append([])
            to_return.append(curr_row)

        to_return[1][1].append(Bomberman(1, 1))

        for i in range(self.row):
            to_return[i][0].append(Wall(i, 0))
            to_return[i][self.col - 1].append(Wall(i, self.col - 1))

        for j in range(self.col):
            to_return[0][j].append(Wall(0, j))
            to_return[self.row - 1][j].append(Wall(self.row - 1, j))

        for i in range(self.bricks_count):
            while True:
                rand_x = random.randint(0, self.row - 1)
                rand_y = random.randint(0, self.col - 1)
                if len(to_return[rand_x][rand_y]) == 0:
                    to_return[rand_x][rand_y].append(Brick(rand_x, rand_y))
                    break

        for i in range(self.enemy_count):
            while True:
                rand_x = random.randint(0, self.row - 1)
                rand_y = random.randint(0, self.col - 1)
                if len(to_return[rand_x][rand_y]) == 0:
                    to_return[rand_x][rand_y].append(Enemy(rand_x, rand_y))
                    break

        return to_return

    def contains(self, x_cord, y_cord, class_name):
        """ contains checks if cell [x, y] contains an instance of
        Class class_name or any instance which contains a method
        class_name which returns the argument class_name given
        as input to this method. """
        if x_cord < 0 or x_cord >= self.row:
            return False
        if y_cord < 0 or y_cord >= self.col:
            return False
        for i in self.board[x_cord][y_cord]:
            try:
                if isinstance(i, class_name):
                    return True
            except TypeError:
                pass
            try:
                if i.class_name() == class_name:
                    return True
            except AttributeError:
                pass
        return False

    def remove(self, instance):
        """ remove removes an instance of something which is on the board
        from the board. """
        new_list = []
        x = instance.x_cord
        y = instance.y_cord
        for i in self.board[x][y]:
            if i is not instance:
                new_list.append(i)
        self.board[x][y] = new_list



    def display(self):
        """ display prints the board. """
        board_to_print = []
        for i in range(self.row * self.cell_row):
            curr_row = []
            for j in range(self.col * self.cell_col):
                curr_row.append([])
            board_to_print.append(curr_row)

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                design_arr = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
                found = False
                if len(self.board[i][j]) > 0:
                    priority_list = [Enemy, Bomberman, Bomb,\
                     Brick, Wall, Explosion]
                    for class_name in priority_list:
                        for instance in self.board[i][j]:
                            if isinstance(instance, class_name):
                                if not found:
                                    design_arr = instance.design()
                                    found = True

                for num in range(2):
                    design_arr[num][0] = Back.BLACK + design_arr[num][0]
                    design_arr[num][3] = design_arr[num][3] + Style.RESET_ALL
                for ii in range(len(design_arr)):
                    for jj in range(len(design_arr[ii])):
                        my_i = i * self.cell_row + ii
                        my_j = j * self.cell_col + jj
                        board_to_print[my_i][my_j] = design_arr[ii][jj]

        string_arr = []
        for i in board_to_print:
            string_arr.append(''.join(i) + '\n')
        print ''.join(string_arr)

    def create_explosion(self, x_cord, y_cord):
        """ Creates an explosion at coordinates x_cord and y_cord on board. """
        if x_cord < 0 or y_cord < 0 or \
          x_cord >= self.row or y_cord >= self.col:
            return
        explosion = Explosion(x_cord, y_cord)
        self.board[x_cord][y_cord].append(explosion)

    def create_bomb(self, x_cord, y_cord):
        """ Creates a bomb at coordinates x_cord and y_cord on board. """
        if x_cord < 0 or y_cord < 0 or \
          x_cord >= self.row or y_cord >= self.col:
            return
        bomb = Bomb(x_cord, y_cord)
        self.board[x_cord][y_cord].append(bomb)
