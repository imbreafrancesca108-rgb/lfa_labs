# PDA Emulator
## Description 
This project implements a Pushdown Automaton emulator in Python. 
The automaton configuration is loaded from external configuration files, while the program simulates the execution of the PDA and determines whether a given input string is accepted or rejected. 
In this example, the PDA recognizes all words over the alphabet "{0, 1}" that have a sequence of 0s followed by a sequence of 1s of the same length. 
## Project Structure
```
pda/
│
├── config.cfg
├── pda.cfg
├── emulator.py
└── executabil.py
```
### config.cfg 
Contains the name of the PDA configuration file that will be loaded by the program. 
### pda.cfg 
Contains the PDA structure, by definition: 
- Alphabet (Sigma)
- Stack symbols
- States
- Start state
- Initial stack symbols
- Final states
- Transitions
### emulator.py 
Contains 4 functions which : 
- read the configuration files
- parse PDA sections
- build the PDA
- verify input words from the user
### executabil.py 
Main program file, which: 
- reads the configuration file
- loads the PDA
- receives input words from the user
- displays a message on whether the word is accepted or rejected
## Recognized Language 
L = { 0^n1^n | n>=1 } 
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
