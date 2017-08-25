""" This file contains the Score class to be used in the game. """
class Score(object):
    """ Score is the Score object in the game. """
    enemy_score = 100
    brickScore = 20
    def __init__(self):
        self.score = 0

    def update_score_destroyed_enemy(self):
        """ updateScoreDestroyedEnemy adds to score points for killing an
        enemy. """
        self.score = self.score + Score.enemy_score

    def update_score_destroyed_brick(self):
        """ updateScoreDestroyedEnemy adds to score points for killing a
        brick. """
        self.score = self.score + Score.brickScore
