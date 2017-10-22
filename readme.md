----------
How To Run
----------

sudo python -i [filename]
Filename here is main.py. Use sudo for running the game. 

--------------
Modules Needed
--------------

* keyboard
to install - sudo pip install keyboard

* colorama
to install - sudo pip install colorama

--------------
Game Controls 
--------------

Key     Action

a       move left
d       move right
w       move up
s       move down
b       drop bomb

----------
Game Rules
----------

You control Bomberman and your task is to kill all the enemies. There are 3 lives only. Bomb creates explosion in four surrounding. If any person or brick is there it will get destroyed. If You destriy enemy you will get 200 points and for destroying brick 20 points.
You can use as many bombs you want, can drop multiple bombs at the same time. If you destroy all the enemies you will win the game.

--------------
File Structure
--------------
.
├── Board.py
├── Board.pyc
├── Bomberman.py
├── Bomberman.pyc
├── Bomb.py
├── Bomb.pyc
├── Brick.py
├── Brick.pyc
├── Enemy.py
├── Enemy.pyc
├── Explosion.py
├── Explosion.pyc
├── Game.py
├── Game.pyc
├── Lives.py
├── Lives.pyc
├── main.py
├── Person.py
├── Person.pyc
├── Score.py
├── Score.pyc
├── Wall.py
└── Wall.pyc 

------------------------
Description of each file
------------------------
Board.py -> This file conatains the class Board. Which is responsible for generating and print the board. It also contains some function like remove and contains. All the functions are explained in the file as comments

Bomberman.py -> It contains the class Bomberman. It contains the design of object bomberman and some functions responsible for motion of bomberman.

Bomb.py -> This file contains the Bomb class. It contains function for designing bomb, for handling time of explosion.

Brick.py -> This file contains the Brick class. Function in this file is design of brick.

Enemy.py -> This file contains Enemy class. Several functions are there i this file for design of enemy, random motion of enemy, assigning directions, etc.

Explosion.py -> This file contains the class Explosion. It creates the design of explosion.

Game.py -> This file contains the Game class. functions in this file are get_input, get_enemies, get_explosions, etc. Seveeral functions in thi file are responsible for getting instances, it also handels exxplosion process and games over, contains game loop.

Lives.py -> This file contains the Lives class. update_lives function is there used to change the life.

main.py -> This file instantiates the game object and runs the game loop

Person.py -> This file contains the class person. Function for moving person and check if person can move, are there.

Score.py -> This file contains the Score class to be used in the game. update_score function is there.

Wall.py -> This file contains the Wall class to be used in the game. Function for designing wall is there.
