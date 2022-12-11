input = "day9/input.txt"

instructions = []

with open(input) as f:
    while True:
        instruction = f.readline()
        if not instruction:
            break 
        instructions.append(instruction.strip("\n").split(" "))

tail_positions = {}

snake_len = 10

snake_x_positions = []
snake_y_positions = []

for i in range(snake_len):
    snake_x_positions.append(0)
    snake_y_positions.append(0)

tail_positions[0] = set()
tail_positions[0].add(0)

def IsNotAdjacent(x1, y1, x2, y2):
    if abs(x1 - x2) > 1:
        return True
    if abs(y1 - y2) > 1:
        return True
    return False

for instruction in instructions:
    for i in range(int(instruction[1])):
        current_instruction = instruction[0]
        for link_id in range(snake_len):
            if "R" in current_instruction:
                snake_x_positions[link_id] += 1
            if "U" in current_instruction:
                snake_y_positions[link_id] += 1
            if "L" in current_instruction:
                snake_x_positions[link_id] -= 1
            if "D" in current_instruction:
                snake_y_positions[link_id] -= 1
            if link_id == snake_len - 1:
                if snake_x_positions[link_id] not in tail_positions.keys():
                    tail_positions[snake_x_positions[link_id]] = set()
                tail_positions[snake_x_positions[link_id]].add(snake_y_positions[link_id])
                break
            if IsNotAdjacent(snake_x_positions[link_id], snake_y_positions[link_id], snake_x_positions[link_id+1], snake_y_positions[link_id+1]):
                current_instruction = []
                if snake_x_positions[link_id]>snake_x_positions[link_id+1]:
                    current_instruction.append("R")
                if snake_x_positions[link_id]<snake_x_positions[link_id+1]:
                    current_instruction.append("L")
                if snake_y_positions[link_id]>snake_y_positions[link_id+1]:
                    current_instruction.append("U")
                if snake_y_positions[link_id]<snake_y_positions[link_id+1]:
                    current_instruction.append("D")
            else:
                break
                
number_of_tail_positions = 0
for key in tail_positions.keys():
    number_of_tail_positions += len(tail_positions[key])

print(number_of_tail_positions)