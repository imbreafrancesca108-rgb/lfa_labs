
from emulator import load_config, build_grammar, verify_word
config_file=load_config("config.cfg")[0]
grammar_config=load_config(config_file)
grammar=build_grammar(grammar_config)
print(grammar)
while True:
    word=input("Type your string: ")
    if word == "Exit":
         break
    if verify_word(word,grammar):
        print("ACCEPTED")
    else:
        print("REJECTED")
