# PDA-based Game
## Description 
This project implements a text-based adventure game inspired by a Pushdown Automata in Python. 
The game configuration is loaded from external configuration files, while the program simulates the player's movements through different rooms and keeps track of objects collected using a stack.
The player can win the game after collecting the key from the Library, using it to unlock the potion from the Lab and reaching the Gate. Depending on the objects from the stack, the player will be redirected to Heaven or Hell.
## Project Structure
```
game/
│
├── config.cfg
├── game.cfg
├── emulator.py
└── executabil.py
```
### config.cfg 
Contains the name of the configuration file that will be loaded by the program. 
### game.cfg 
Contains the game structure: 
- Alphabet (Sigma)
- States (rooms)
- Start state
- Final states
- Transitions
### emulator.py 
Contains functions which : 
- read the configuration files
- parse PDA sections
- build the PDA-like automata
- move the player between rooms
- manage the stack
- determine the final outcome
### executabil.py 
Main program file, which: 
- reads the configuration file
- loads the game configuration
- initializes the player and stack
- receives commands from the user
- updates the object inventory
- displays a message on whether the player won or lost
## Game rooms
- START (intial room)
- Library (contains key)
- Workshop
- Lab (contains potion)
- Garden
- Gate
- Heaven
- Hell
## How the Game Works 
When a player reaches the Library, a key is added to the stack.

Stack: [key]

When a player reaches the Lab, a potion is added to the stack.

Stack: [key,potion]

The gate is the decision point:
- if the player has the potion -> Heaven
- if the player does not have the potion -> Hell
  
## Running the Program
```
Example:

You are in: START

Coordinate: N
You are in: Library
You found the key!

Coordinate: S
You are in: START

Coordinate: W
You are in: Lab
You found the potion!

Coordinate: N
You are in: Workshop

Coordinate: N
You are in: Garden

Coordinate: W
You are in heaven. You won!

To stop the game:

Coordinate: Exit

The command Exit terminates the game.
```
