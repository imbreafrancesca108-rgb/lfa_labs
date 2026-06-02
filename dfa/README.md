# DFA Emulator

## Description

This project implements a Deterministic Finite Automaton emulator in Python.
The automaton configuration is loaded from external configuration files, while the program simulates the execution of the DFA and determines whether a given input word is accepted or rejected.
In this example, the DFA recognizes all words over the alphabet "{a, b}" that end with the sequence "ab".
## Project Structure
```
dfa/
│
├── config.cfg
├── dfa1.cfg
├── emulator.py
└── executabil.py
```
### config.cfg
Contains the name of the DFA configuration file that will be loaded by the program.
### dfa1.cfg
Contains the DFA structure, by definition:
- Alphabet (Sigma)
- States
- Start state
- Final states
- Transitions
### emulator.py
Contains 5 functions which :
- read the configuration files
- parse DFA sections
- build the dfa
- simulate the automata
- verify input words from the user
### executabil.py
Main program file, which:
- reads the configuration file
- loads the DFA
- receives input words from the user
- displays a message on whether the word is accepted or rejected
## Recognized Language
L = { w ∈ {a,b}* | w ends with "ab" }
## How the DFA Works
The automaton contains three states:
- q0: initial state
- q1: the last character as 'a'
- q2: the sequence 'ab' was just read (final state)
## Running the Program
```
Run:
python executabil.py
Type your word: ab
ACCEPTED
Type your word: aba
REJECTED
Type your word: Exit
The command `Exit` terminates the program.
```
