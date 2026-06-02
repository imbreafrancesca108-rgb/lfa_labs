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
# builds nfa
def build_nfa(config):
    sections=parse_config(config)
    alphabet=sections["Sigma"]
    states=sections["States"]
    start_state=sections["Start"][0]
    final_states=sections["Final"]
    transitions={}
    for transition in sections["Transitions"]:
        state,symbol,next_state=[ch.strip() for ch in transition.split(",")]
        if state not in transitions:
            transitions[state]={}
        if symbol not in transitions[state]:
            transitions[state][symbol]=[]
        transitions[state][symbol].append(next_state)
    # returns automata as a dictionary
    return {
        "alphabet": alphabet,
        "states": states,
        "start": start_state,
        "final": final_states,
        "transitions": transitions
    }
# verifies if a word is accepted/ or not
def verify_word(word,nfa):
    current=[nfa["start"]]
    for symbol in word:
        # if the symbol isn't in the alphabet, the word is rejected
        if symbol not in nfa["alphabet"]:
            return False
        next_states=[]
        # explores all current active states
        for state in current:
            # checks if there are transitions for that state
            if state in nfa["transitions"]:
                # checks if transitions exist for the symbol
                if symbol in nfa["transitions"][state]:
                    # adds all reachable states
                    for next_state in nfa["transitions"][state][symbol]:
                        next_states.append(next_state)
        current = next_states
        # the word is accepted if at least one of the active states is the final one
    for state in current:
        if state in nfa["final"]:
            return True
    return False