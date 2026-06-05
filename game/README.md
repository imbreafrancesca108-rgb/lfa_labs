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
## How the PDA Works 
The automaton uses a stack to compare the number of 0s and the number of 1s.

The automaton contains three states: 
- q0: initial state that reads 0s and pushes X on the stack for each 0 read
- q1: reads 1s and pops one X for each 1 read
- qf: final state that is reached after the whole input is consumed and only the initial stack symbol remains
## Running the Program
```
Run:
python executabil.py
Type your word: 01
ACCEPTED
Type your word: 000111
ACCEPTED
Type your word: 001
REJECTED
Type your word: Exit
The command `Exit` terminates the program.
```
