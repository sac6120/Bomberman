# Bomberman

The bomberman game implemented to play in the terminal.

## Prerequisites

```
pip install keyboard Quartz colorama
```

NOTE: There is a bug in pip installing Quartz.
Check https://stackoverflow.com/questions/42530309/no-such-file-requirements-txt-error-while-installing-quartz-module

## Run the code

```
sudo python main.py
```

## Description of python files 

- Board.py: Code for generating and printing the game board.
- Bomd.py: Code for designing the bomb and calculating the time of explosion.
- Bomberman.py: Code for desiging the bomberman and the motion of moving.
- Brick.py: Code for designing the brick which blocks the moving of objects in game.
- Enemy.py: Code for designing the enemies and moving of the enemies.
- Explosion.py: Code for handling the explosion.
- Game.py: Code for the loop of the whole game.
- Lives.py: Code for handling the lives of objects in game.
- Wall.py: Code for creating blocks of brick to form the wall.
- Score.py: Code for calculating the score earned by player.
- Person.py: Code for the movement of objects.
- main.py: The enter point of the game.

## Controls
- press A to move left
- press D to move right
- press S to move down
- press W to move up
- press B to drop bomb