import sys


COLORS = ["BLUE", "RED", "BLACK", "MAGENTA", "GREEN", "ORANGE", "BROWN", "NAVY", "LTBLUE", "YELLOW", "WHITE", "LTGRAY", "MEDGRAY", "GRAY", "DARKGRAVY"]
# Widths of all characters in pixels
CHARWIDTHS = {
    'a': 10,
    'b': 8,
    'c': 8,
    'd': 8,
    'e': 8,
    'f': 8,
    'g': 8,
    'h': 8,
    'i': 4,
    'j': 8,
    'k': 9,
    'l': 6,
    'm': 12,
    'n': 8,
    'o': 9,
    'p': 8,
    'q': 9,
    'r': 8,
    's': 7,
    't': 8,
    'u': 10,
    'v': 8,
    'w': 12,
    'x': 9,
    'y': 8,
    'z': 8,
    'A': 8,
    'B': 8,
    'C': 8,
    'D': 8,
    'E': 8,
    'F': 8,
    'G': 8,
    'H': 8,
    'I': 9,
    'J': 8,
    'K': 8,
    'L': 8,
    'M': 10,
    'N': 9,
    'O': 8,
    'P': 8,
    'Q': 8,
    'R': 8,
    'S': 8,
    'T': 8,
    'U': 9,
    'V': 10,
    'W': 10,
    'X': 9,
    'Y': 10,
    'Z': 8,
    'θ': 8,
    ' ': 2,
    "'": 4,
    '"': 8,
    '{': 8,
    '}': 8,
    '(': 6,
    ')': 6,
    '}': 8,
    '[': 6,
    ']': 6,
    '0': 8,
    '1': 8,
    '2': 8,
    '3': 8,
    '4': 8,
    '5': 8,
    '6': 8,
    '7': 8,
    '8': 8,
    '9': 8,
    '!': 4,
    '@': 12,
    '#': 12,
    '$': 10,
    '%': 10,
    '^': 8,
    '&': 10,
    '*': 10,
    '+': 8,
    '-': 8,
    '/': 8,
    '_': 8,
    '=': 8,
    ',': 5,
    '.': 4,
    '?': 8,
    '\\': 8,
    '|': 4,
    ';': 8,
    ':': 4,
    'π': 12,
    '√': 11,
    '<': 8,
    '>': 8,
    '≤': 10,
    '≥': 10,
    '≠': 14,
    '~': 6,  # Negative symbol
    '`': 8
}
settings = {  # Keys MUST be 5 characters
    "TCHAR": ",",  # Character before text to use Text( for
    "WWRAP": 1,  # Wrap words separated by SPLIT instead of just characters
    "SPLIT": " ",  # Character that splits words to be wrapped
    "NPAGE": ";;;",  # Triggers new page code
    "NLINE": ",,,",  # Triggers new line code
}


# Processes a number that can be an increment, nothing, or set it
def parse_number(number, current):
    if number == "":
        return current
    if number[0] == "-":
        return current - int(number[1:])
    elif number[0] == "+":
        return current + int(number[1:])
    else:
        return int(number)


# Interpret line of code
def parse_line(line):
    # Too lazy to have good habits
    global page_position
    global newf
    global settings
    global color
    
    # Commet or blank lines ignored, comes first to avoid IndexError
    if line == "" or line[:2] == "//":
        newf.append(line[:])
        return None
    elif line.split(" ")[0] in settings:
        if line[5:] == "1" or line[5:] == "0":
            settings[line[:5]] == int(line[5:])
        else:
            settings[line[:5]] == line[5:]
    # Change color
    elif line in COLORS:
        newf.append(f"TextColor({line}")
        color = line[:]
    # Change cursor position
    elif line[0] == "(":
        parsing = line[1:-1].split(",")
        page_position = [parse_number(parsing[0], page_position[0]), 
        parse_number(parsing[1], page_position[1])]
        if page_position[1] >= 264:
            parse_line(settings["NLINE"])
        elif page_position[0] >= 160:
            parse_line(settings["NPAGE"])
    # New line
    elif line == settings["NLINE"]:
        try:
            for instruction in new_line:
                if instruction[0] == ",":
                    newf.append(f'Text({page_position[0]},{page_position[1]},"{instruction[1:]}"')
                    continue
                parse_line(instruction)
        except RecursionError:
            print("NEW LINE")
            RecursionError
            # raise RecursionError
    # New page
    elif line == settings["NPAGE"]:
        try:
            for instruction in new_page:
                parse_line(instruction)
        except RecursionError:
            print("NEW PAGE")
            raise RecursionError
    # Text( function is used here
    elif line[0] == settings["TCHAR"]:
        current = ""
        # Save old position and color in case new page is needed
        pxlcount = page_position[1]
        oldcolor = color[:]
        oldposition = page_position[1]
        if settings["WWRAP"]:
            word_list = line[1:].split(settings["SPLIT"])  # For word wrap, each word is taken into account for determining pixels rather than character
            words = [word + " " for word in word_list[:-1]]
            words.append(word_list[len(word_list)-1])
            for word in range(len(words)):
                for char in words[word]:
                    if char[:] not in CHARWIDTHS:
                        CHARWIDTHS[char] = 8
                if pxlcount + sum([CHARWIDTHS[char] for char in words[word]]) > 264:
                    newf.append(f'Text({page_position[0]},{page_position[1]},"{current}"')
                    page_position[0] += 12
                    if page_position[0] >= 152:
                        parse_line(settings["NPAGE"])
                        parse_line(oldcolor)
                        parse_line(f"(,{oldposition})")
                    current = ""
                    pxlcount = page_position[1]
                current += words[word]
                pxlcount += sum(CHARWIDTHS[char] for char in words[word])

        else:
            for char in range(len(line[1:])):
                if char not in CHARWIDTHS:
                    CHARWIDTHS[char] = 8
                if pxlcount + CHARWIDTHS[line[1 + char]] >= 264:
                    newf.append(f'Text({page_position[0]},{page_position[1]},"{current}"')
                    page_position[0] += 12
                    if page_position[0] >= 152:
                        parse_line(settings["NPAGE"])
                        parse_line(oldcolor)
                        parse_line(f"(,{oldposition})")
                    current = ""
                    pxlcount = page_position[1]
                current += line[1 + char]
                pxlcount += CHARWIDTHS[line[1 + char]]
        if current != "":
            newf.append(f'Text({page_position[0]},{page_position[1]},"{current}"')
        parse_line(settings["NLINE"])
    # Change text color
    elif line in COLORS:
        newf.append(f"TextColor({line}")
    # Everything else is assumed to be a proper TI-BASIC command
    else:
        newf.append(line)


# Run program
if __name__ == "__main__":
    args = sys.argv
    with open(args[1], "r") as f:
        file = f.read().split("\n")

    # Default file variables
    color = "BLACK"
    new_page = ["Pause ", "ClrDraw ", "(0,0)"]
    new_line = ["(+12,)"]
    page_position = [0,0]
    
    # Keep track of program flow
    newf = []
    mode = "normal"
    line_buffer = []
    for line in range(len(file)):
        current_line = file[line][:]
        # Check for header or newpage, or process these
        if "<l>" in current_line:
            mode = "newline"
            current_line = current_line[3:]
        elif "<p>" in current_line:
            mode = "newpage"
            current_line = current_line[3:]
            line_buffer = []
        if "</l>" in current_line:
            line_buffer.append(current_line[:-4])
            new_line = line_buffer[:]
            line_buffer = []
            mode = "normal"
            continue
        elif "</p>" in current_line:
            line_buffer.append(current_line[:-4])
            new_page = line_buffer[:]
            line_buffer = []
            mode = "normal"
            continue
        elif mode == "newline" or mode == "newpage":
            line_buffer.append(current_line)
            continue
        
        parse_line(current_line)
        
    
    # Write to output file
    newf = [newf[i] + "\n" for i in range(len(newf))]
    with open(args[2], "w") as f:
        f.writelines(newf)
