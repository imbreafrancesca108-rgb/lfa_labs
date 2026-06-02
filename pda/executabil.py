# this automata accepts all words that have a subsequence of 0, followed by a subsequence of 1, both of the same length
# 0^n1^n
from emulator import load_config, build_pda, verify_word
config_file=load_config("config.cfg")[0]
pda_config=load_config(config_file)
pda=build_pda(pda_config)
print(pda)
while True:
    word=input("Type your string: ")
    if word == "Exit":
         break
    if verify_word(word,pda):
        print("ACCEPTED")
    else:
        print("REJECTED")
