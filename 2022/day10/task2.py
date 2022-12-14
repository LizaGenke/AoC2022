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
sprite = 3
current_pixel = 0
end_text = []
end_text.append([])
row = 0

for instruction in instructions:
    if instruction == "noop":
        if (current_cycle - 1) % 40 == 0:
            end_text.append([])
            row += 1
        current_pixel = (current_cycle - 1) % 40
        if (current_pixel >= x - 1) and (current_pixel <= x + 1):
            end_text[row].append("#")
        else:
            end_text[row].append(".")
        current_cycle += 1
    if instruction[0:4] == "addx":
        if (current_cycle - 1) % 40 == 0:
            end_text.append([])
            row += 1
        current_pixel = (current_cycle - 1) % 40
        if (current_pixel >= x - 1) and (current_pixel <= x + 1):
            end_text[row].append("#")
        else:
            end_text[row].append(".")
        current_cycle += 1
        if (current_cycle - 1) % 40 == 0:
            end_text.append([])
            row += 1
        current_pixel = (current_cycle - 1) % 40
        if (current_pixel >= x - 1) and (current_pixel <= x + 1):
            end_text[row].append("#")
        else:
            end_text[row].append(".")
        x += int(instruction[5:])
        current_cycle += 1


print(len(end_text))

for line in end_text:
    for char in line:
        print(char, end='')
    print("\n", end='')  