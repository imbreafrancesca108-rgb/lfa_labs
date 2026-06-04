from emulator import *
config_file=load_config("config.cfg")[0]
regex_config=load_config(config_file)
regex=build_regex(regex_config)
print(regex["regex"])

while True:
    word=input("Enter a string: ")
    if word=="Exit":
        break
    if verify_word(word,regex):
        print("ACCEPTED")
    else:
        print("REJECTED")
