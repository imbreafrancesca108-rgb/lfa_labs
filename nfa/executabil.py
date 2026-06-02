# this automata accepts all words that have an even number of '0'
from emulator import load_config, build_nfa, verify_word
config_file=load_config("config.cfg")[0]
nfa_config=load_config(config_file)
nfa=build_nfa(nfa_config)
print(nfa)
while True:
    word=input("Type your string: ")
    if word == "Exit":
         break
    if verify_word(word,nfa):
        print("ACCEPTED")
    else:
        print("REJECTED")