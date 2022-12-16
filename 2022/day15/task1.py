import re
input = "day15/input.txt"

sensor_data = []
row_to_check = {}
chosen_row = 2000000

with open(input) as f:
    while True:
        line = f.readline()
        if not line:
            break 
        pattern = '-*\d+'
        match = re.findall(pattern, line)
        int_match = [int(i) for i in match]
        print(int_match)
        if int_match[1] == chosen_row:
            row_to_check[0] = "S"
        if int_match[3] == chosen_row:
            row_to_check[0] = "B"
        sensor_data.append(int_match)

for sensor in sensor_data:
    distance = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
    dist_to_chosen_row = abs(sensor[1] - chosen_row)
    if dist_to_chosen_row <= distance:
        for x in range (sensor[0] - (distance - dist_to_chosen_row), sensor[0] + (distance - dist_to_chosen_row) + 1):
            if x not in row_to_check.keys():
                row_to_check[x] = "#"

cant_be_b = 0
for value in row_to_check.values():
    if value != "B":
        cant_be_b += 1
    if value == "B":
        print("hello")

print(cant_be_b)
    