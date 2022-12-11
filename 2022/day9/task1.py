input = "day9/input.txt"

instructions = []

with open(input) as f:
    while True:
        instruction = f.readline()
        if not instruction:
            break 
        instructions.append(instruction.strip("\n").split(" "))

tail_positions = {}
tail_x = 0
tail_y = 0

head_x = 0
head_y = 0

prev_head_x = 0
prev_head_y = 0

tail_positions[0] = set()
tail_positions[0].add(0)

def IsNotAdjacent(x1, y1, x2, y2):
    if abs(x1 - x2) > 1:
        return True
    if abs(y1 - y2) > 1:
        return True
    return False

for instruction in instructions:
    if instruction[0] == "R":
        for i in range(int(instruction[1])):
           head_x += 1
           if (IsNotAdjacent(tail_x, tail_y, head_x, head_y)):
                tail_x = prev_head_x
                tail_y = prev_head_y
                if tail_x not in tail_positions.keys():
                    tail_positions[tail_x] = set()
                tail_positions[tail_x].add(tail_y)
           prev_head_x = head_x
    if instruction[0] == "U":
        for i in range(int(instruction[1])):
           head_y += 1
           if (IsNotAdjacent(tail_x, tail_y, head_x, head_y)):
                tail_x = prev_head_x
                tail_y = prev_head_y
                if tail_x not in tail_positions.keys():
                    tail_positions[tail_x] = set()
                tail_positions[tail_x].add(tail_y)
           prev_head_y = head_y
    if instruction[0] == "L":
        for i in range(int(instruction[1])):
           head_x -= 1
           if (IsNotAdjacent(tail_x, tail_y, head_x, head_y)):
                tail_x = prev_head_x
                tail_y = prev_head_y
                if tail_x not in tail_positions.keys():
                    tail_positions[tail_x] = set()
                tail_positions[tail_x].add(tail_y)
           prev_head_x = head_x
    if instruction[0] == "D":
        for i in range(int(instruction[1])):
           head_y -= 1
           if (IsNotAdjacent(tail_x, tail_y, head_x, head_y)):
                tail_x = prev_head_x
                tail_y = prev_head_y
                if tail_x not in tail_positions.keys():
                    tail_positions[tail_x] = set()
                tail_positions[tail_x].add(tail_y)
           prev_head_y = head_y

number_of_tail_positions = 0
for key in tail_positions.keys():
    number_of_tail_positions += len(tail_positions[key])

print(number_of_tail_positions)