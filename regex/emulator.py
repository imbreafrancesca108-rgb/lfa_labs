import re

def load_config(file_name):
    lines=[]
    with open(file_name, 'r') as f:
        for line in f:
            line=line.strip()
            if line!="" and not line.startswith("//"):
                lines.append(line)
    return lines
# separate into sections : alphabet, regex
def parse_config(config):
    sections={}
    current_section= None
    for line in config:
        if line.endswith(":"):
            current_section = line[:-1]
            sections[current_section]=[]
        else:
            sections[current_section].append(line)
    return sections
# build regex 
def build_regex(config):
    sections=parse_config(config)
    alphabet=sections["Sigma"]
    regex=sections["Regex"][0]
    # convert into python syntax "|" instead of "U"
    regex=regex.replace("U","|")
    regex=regex.replace("u","|")

    return {
        "alphabet": alphabet,
        "regex": regex
    }
# check if a word is accepted or not
def verify_word(word,regex_data):
    # check the alphabet
    for symbol in word:
        if symbol not in regex_data["alphabet"]:
            return False
    pattern = "^" + regex_data["regex"] + "$"
    return re.match(pattern,word) is not None
