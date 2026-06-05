# winning route example: START->Library->START->Lab->Workshop->Garden->Gate->Heaven
# N->S->W->N->N->W
# you win if you reach the gate and you have the potion , otherwise you lose
# losing route example: START->Lab->Workshop->Garden->Gate->Hell
# W->N->N->W
from emulator import load_config, build_pda, move ,update_stack, check_final
config_file=load_config("config.cfg")[0]
pda_config=load_config(config_file)
pda=build_pda(pda_config)
current=pda["start"]
stack=[]
print(pda)
print("You are in:", current)
print("Use N,S,E,W to move.")
print("Type Exit to stop the game.")
while True:
    direction=input("Coordinate:")
    if direction=="Exit":
        break
    old_room=current
    current=move(current,direction,pda)
    if current==old_room:
        print("You cannot go that way!")
    else:
        print("You are in :", current)
    stack=update_stack(current,stack)
    current=check_final(current,stack)
    if current=="Heaven":
        print("You are in heaven. You won!")
        break
    if current=="Hell":
        print("You are in hell. You lost!")
        break

