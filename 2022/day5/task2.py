import re

input = "day5/input.txt"

read_boxes = True
read_instructions = False

amounts = []
from_stapel = []
to_stapel = []

staples = {}

with open(input) as f:
    while True:
        line = f.readline()
        if not line:
            break   
        if (read_boxes == True):
            matches = re.finditer("[A-Z]", line)
            if (matches == None):
                read_boxes = False
                read_instructions = True
                continue
            for match in matches:
                staple_number = int((match.start()-1)/4 + 1)
                if (staple_number not in staples):
                    staples[staple_number] = []
                staples[staple_number].append(match.group())

        if (len(line) == 1):
            read_instructions = True
            continue

        if read_instructions == True:
            instructions = line.split(" from ")
            amounts.append(int(instructions[0].strip("move ")))
            directions = instructions[1].split(" to ")
            from_stapel.append(int(directions[0]))
            to_stapel.append(int(directions[1][0]))

for step, amount in enumerate(amounts):
    boxes_to_move_in_order = staples[from_stapel[step]][0:amount]
    staples[to_stapel[step]] = boxes_to_move_in_order + staples[to_stapel[step]]
    staples[from_stapel[step]] = staples[from_stapel[step]][amount:]

for key in staples:
    print(key, staples[key][0])