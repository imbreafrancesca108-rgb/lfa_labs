# this automata accepts all words that end in 'ab'
from emulator import load_config, build_dfa, verify_word
config_file=load_config("config.cfg")[0]
dfa_config=load_config(config_file)
dfa=build_dfa(dfa_config)
print(dfa)
while True:
    word=input("Type your word: ")
    if word == "Exit":
         break
    if verify_word(word,dfa):
        print("ACCEPTED")
    else:
        print("REJECTED")