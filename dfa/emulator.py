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
# builds dfa
def build_dfa(config):
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
# verifies if a word is accepted/ or not
def verify_word(word,dfa):
    current=dfa["start"]
    for symbol in word:
        # if the symbol isn't in the alphabet, the word is rejected
        if symbol not in dfa["alphabet"]:
            return False
        # if there s no transition from the current state, the word is rejected
        if current not in dfa["transitions"]:
            return False
        # if there s no transitions to the current state, the word is rejected
        if symbol not in dfa["transitions"][current]:
            return False
        # we move on to the next state
        current=dfa["transitions"][current][symbol]
    return current in dfa["final"]