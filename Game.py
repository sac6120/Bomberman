""" This file contains the Game class to be used in the game. """

import random
import os
import time
import keyboard
import sys
from colorama import init, Fore, Style

from Brick import Brick
from Explosion import Explosion
from Score import Score
from Lives import Lives
from Bomb import Bomb
from Enemy import Enemy
from Board import Board

class Game(object):
    """ Game is the game object in the bomberman game. """
    def __init__(self):
        init()
        random.seed(1)
        self.game_over = False
        self.board = Board()
        self.bomberman = self.board.board[1][1][0]
        self.score = Score()
        self.lives = Lives()
        self.direction_key = ''
        self.bomb_key = ''

    def get_input(self):
        """ get_input detects key presses and sets direction_key and
        bomb_key. """
        possible_keys = ['w', 'a', 's', 'd']
        for key in possible_keys:
            try:
                if keyboard.is_pressed(key):
                    self.direction_key = key
            except:
                pass
        try:
            if keyboard.is_pressed('b'):
                self.bomb_key = True
        except:
            pass

    def get_enemies(self):
        """ get_enemies returns a list of enemies currently on the board. """
        to_return = []
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                for k in range(len(self.board.board[i][j])):
                    if isinstance(self.board.board[i][j][k], Enemy):
                        to_return.append(self.board.board[i][j][k])
        return to_return

    def get_bombs(self):
        """ get_bombs returns a list of bombs currently on the board. """
        to_return = []
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                for k in range(len(self.board.board[i][j])):
                    if isinstance(self.board.board[i][j][k], Bomb):
                        to_return.append(self.board.board[i][j][k])
        return to_return

    def get_bricks(self):
        """ get_bricks returns a list of bricks currently on the board. """
        to_return = []
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                for k in range(len(self.board.board[i][j])):
                    if isinstance(self.board.board[i][j][k], Brick):
                        to_return.append(self.board.board[i][j][k])
        return to_return

    def get_explosions(self):
        """ get_explosions returns a list of explosions currently on the
        board. """
        to_return = []
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                for k in range(len(self.board.board[i][j])):
                    if isinstance(self.board.board[i][j][k], Explosion):
                        to_return.append(self.board.board[i][j][k])
        return to_return

    def process_explosions(self):
        """ process_explosions proceses and removes the enemies/bricks/bomberman
        killed in explosion. """
        enemies = self.get_enemies()
        bricks = self.get_bricks()
        for explosion in self.get_explosions():
            if self.bomberman.x_cord == explosion.x_cord and \
            self.bomberman.y_cord == explosion.y_cord:
                self.lives.update_lives()
                self.board.remove(self.bomberman)
                self.bomberman.move_person_here(1, 1, self.board)
            for enemy in enemies:
                if enemy.x_cord == explosion.x_cord and enemy.y_cord == explosion.y_cord:
                    self.board.remove(enemy)
                    self.score.update_score_destroyed_enemy()
            for brick in bricks:
                if brick.x_cord == explosion.x_cord and brick.y_cord == explosion.y_cord:
                    self.board.remove(brick)
                    self.score.update_score_destroyed_brick()

    def sleep_taking_input(self, milli_seconds_to_stop):
        """ sleep_taking_input makes the program idle for the specified time
        but continues taking input (key detection for movement etc). """
        start = int(round(time.time() * 1000))
        while True:
            curr_time = int(round(time.time() * 1000))
            self.get_input()
            if curr_time > start + milli_seconds_to_stop:
                break

    def remove_explosions(self):
        """ remove_explosions removes the explosions after one second of bomb
        bursting. """
        for explosion in self.get_explosions():
            self.board.remove(explosion)

    def handle_game_over(self):
        """ handle_game_over checks if the game is over """
        if self.lives.lives == 0:
            print "Game Over!"
            os._exit(0)


    def game_loop(self):
        """ game_loop implements the game inf loop. """
        try:
            if keyboard.is_pressed('a'):
                pass
        except: 
                print(Fore.RED + 'Use sudo for playing the Game' + Style.RESET_ALL)
                sys.exit()
        while True:
            self.board.display()
            print str(self.score.score) +    "        " + str(self.lives.lives)

            time.sleep(0.1)
            milli_seconds_to_stop = 400
            self.sleep_taking_input(milli_seconds_to_stop)

            self.remove_explosions()

            for bomb in self.get_bombs():
                bomb.reduce_time_or_explode(self.board)

            self.handle_game_over()

            self.process_explosions()

            if self.bomberman.is_on_enemy(self.board):
                self.lives.update_lives()
                self.board.remove(self.bomberman)
                self.bomberman.move_person_here(1, 1, self.board)

            self.bomberman.handle_input(self.board, \
              [self.direction_key, self.bomb_key])
            self.direction_key = ''
            self.bomb_key = False

            for enemy in self.get_enemies():
                enemy.random_move_enemy(self.board)

            os.system("clear")