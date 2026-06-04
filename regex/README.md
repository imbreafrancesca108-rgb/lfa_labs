# REGEX Emulator
## Description 
This project implements a Regular Expression emulator in Python. 
The regular expression configuration is loaded from external configuration files, while the program determines whether a given input word is accepted or rejected by the regular expression. 
In this example, the regex recognizes all words over the alphabet "{0,1}". 
## Project Structure
```
regex/
│
├── config.cfg
├── regex.cfg
├── emulator.py
└── executabil.py
```
### config.cfg 
Contains the name of the DFA configuration file that will be loaded by the program. 
### regex.cfg 
Contains the DFA structure, by definition: 
- Alphabet (Sigma)
- Regular Expression (Regex)
### emulator.py 
Contains 4 functions which : 
- read the configuration files
- parse regex sections
- builds regex
- verify input words from the user
### executabil.py 
Main program file, which: 
- reads the configuration file
- loads the regex
- receives input words from the user
- displays a message on whether the word is accepted or rejected
## Recognized Language 
L = { w ∈ {0,1}* } 
## How the Regex Works 
The regex accepts any sequence of 0s and 1s. 
## Running the Program
```
Run:
python executabil.py
Type your word: 0101111
ACCEPTED
Type your word: 000
ACCEPTED
Type your word: 012
REJECTED
Type your word: Exit
The command `Exit` terminates the program.
```
