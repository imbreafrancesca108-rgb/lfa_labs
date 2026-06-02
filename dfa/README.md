# NFA Emulator

## Description

This project implements a Non-Deterministic Finite Automaton emulator in Python.
The automaton configuration is loaded from external configuration files, while the program simulates the execution of the NFA and determines whether a given input word is accepted or rejected.
In this example, the NFA recognizes all words over the alphabet "{0, 1}" that have an even number of 0.
## Project Structure
```
nfa/
│
├── config.cfg
├── nfa.cfg
├── emulator.py
└── executabil.py
```
### config.cfg
Contains the name of the NFA configuration file that will be loaded by the program.
### nfa.cfg
Contains the NFA structure, by definition:
- Alphabet (Sigma)
- States
- Start state
- Final states
- Transitions
### emulator.py
Contains 4 functions which :
- read the configuration files
- parse NFA sections
- build the nfa
- verify input words from the user
### executabil.py
Main program file, which:
- reads the configuration file
- loads the NFA
- receives input words from the user
- displays a message on whether the word is accepted or rejected
## Recognized Language
L = { w ∈ {0,1}* | w contains an even number of 0 symbols }
## How the NFA Works
The automaton contains two states:
- q_even: initial and final state, representing an even number of 0 read so far
- q_odd: representing an odd number of 0 read so far
Reading 0 switches between the two states. Reading 1 keeps the automaton in the same state.
## Running the Program
```
Run:
python executabil.py
Type your word: 00
ACCEPTED
Type your word: 110
REJECTED
Type your word: Exit
The command `Exit` terminates the program.
```
