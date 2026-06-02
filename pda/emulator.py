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
# builds pda structure
def build_pda(config):
    sections=parse_config(config)

    alphabet=sections["Sigma"]
    stack_symbols=sections["Stack"]
    states=sections["States"]
    start_state=sections["Start"][0]
    stack_start=sections["StackStart"][0]
    final_states=sections["Final"]
    transitions=[]
    for transition in sections["Transitions"]:
        current_state,input_symbol,stack_top,push_symbols,next_state=[ch.strip() for ch in transition.split(",")]
        transitions.append({
            "current_state":current_state,
            "input_symbol":input_symbol,
            "stack_top":stack_top,
            "push_symbols":push_symbols,
            "next_state":next_state

        })
    # returns automata as a dictionary
    return {
        "alphabet": alphabet,
        "stack_symbols": stack_symbols,
        "states": states,
        "start": start_state,
        "stack_start": stack_start,
        "final": final_states,
        "transitions": transitions
    }
# verifies if a word is accepted/ or not
def verify_word(word,pda):
    current_state=pda["start"]
    stack=[pda["stack_start"]]
    position=0
    while True:
        found= False
        # looks for a transition that can be applied
        for transition in pda["transitions"]:
            #checks is the transition starts from the curren state
            if transition["current_state"] != current_state:
                continue
            if len(stack) ==0:
                continue
            # checks if the top of the stack macthes the transition
            if transition["stack_top"]!=stack[-1]:
                continue
            input_symbol=transition["input_symbol"]
            if input_symbol != "eps":
                if position>=len(word):
                    continue
                if word[position]!=input_symbol:
                    continue
            # apply transition
            stack.pop()
            #push new symbol if it s not eps
            if transition["push_symbols"]!="eps":
                for symbol in reversed(transition["push_symbols"]):
                    stack.append(symbol)
            if input_symbol != "eps":
                position+=1
            current_state=transition["next_state"]
            found=True
            break
        if not found:
            break
    # the word is accepeted if we ve consumed the entire input and reached the final state
    return position == len(word) and current_state in pda["final"]