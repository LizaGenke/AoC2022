input = "day10/input.txt"

instructions = []

with open(input) as f:
    while True:
        instruction = f.readline()
        if not instruction:
            break 
        instructions.append(instruction.strip("\n"))

current_cycle = 1
x =  1
sum = 0

for instruction in instructions:
    if instruction == "noop":
        if current_cycle % 40 == 20:
            sum += x * current_cycle
        current_cycle += 1
    if instruction[0:4] == "addx":
        if current_cycle % 40 == 20:
            sum += x * current_cycle
        current_cycle += 1
        if current_cycle % 40 == 20:
            sum += x * current_cycle
        x += int(instruction[5:])
        current_cycle += 1

print(sum)     