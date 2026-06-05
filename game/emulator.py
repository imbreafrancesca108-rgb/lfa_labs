#loads configuration file and selects lines needed
def load_config(file_name):
    lines=[]
    with open(file_name,'r') as f:
        for line in f:
            line=line.rstrip()
            if line !="" and not line.strip().startswith("//"):
                lines.append(line)
    return lines
# splits configuration into sections
def parse_config(config):
    sections={}
    current_section=None
    for line in config:
        if line.endswith(":") and not line.startswith("\t"):
            current_section=line[:-1]
            sections[current_section]=[]
        else:
            sections[current_section].append(line.strip())
    return sections
# builds the pda-like automaton
def build_pda(config):
    sections=parse_config(config)
    alphabet=sections["Sigma"]
    states=sections["States"]
    start_state=sections["Start"][0]
    final_states=sections["Final"]
    transitions={}
    for transition in sections["Transitions"]:
        state,symbol,next_state=transition.split(",")
        if state not in transitions:
            transitions[state]={}
        transitions[state][symbol]=next_state
    # returns automata as a dictionary
    return {
        "alphabet": alphabet,
        "states": states,
        "start": start_state,
        "final": final_states,
        "transitions": transitions
    }
# moves from one room to another
def move(current,direction,pda):
    #invalid direction
    if direction not in pda["alphabet"]:
        return current
    #current room has no transitions
    if current not in pda["transitions"]:
        return current
    #no transition exists for this direction
    if direction not in pda["transitions"][current]:
        return current
    #valid transition
    return pda["transitions"][current][direction]
# updates stack with objects collected
def update_stack(current, stack):
    if current=="Library" and "key" not in stack:
        stack.append("key")
        print("You found the key !")
    if current=="Lab":
        if "key" in stack and "potion" not in  stack:
            stack.append("potion")
            print("You found the potion !")
        elif "key" not in stack:
            print("Potion is locked. You need a key !")
    return stack

#decides if a player reaches Heaven or Hell
def check_final(current,stack):
    if current=="Gate":
        if "potion" in stack:
            return "Heaven"
        else:
            return "Hell"
    return current