import re
input = "day15/input.txt"

sensor_data = []
row_to_check = {}


with open(input) as f:
    while True:
        line = f.readline()
        if not line:
            break 
        pattern = '-*\d+'
        match = re.findall(pattern, line)
        int_match = [int(i) for i in match]
        print(int_match)

        sensor_data.append(int_match)

found_row = False

limit = 4000000

for chosen_row in range (0, limit + 1):
    if found_row:
        break
    print("Row: ", chosen_row)
    row_values = []
    for sensor in sensor_data:
        distance = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
        if sensor[1] == chosen_row and sensor[0] >=0 and sensor[0] <=limit:
            row_values.append([sensor[0], sensor[0]])
        if sensor[3] == chosen_row and sensor[2] >=0 and sensor[2] <=limit:
            row_values.append([sensor[2], sensor[2]])
        dist_to_chosen_row = abs(sensor[1] - chosen_row)
        if dist_to_chosen_row <= distance:
            vals = [max(0,sensor[0] - (distance - dist_to_chosen_row)), min(sensor[0] + (distance - dist_to_chosen_row), limit)]
            row_values.append(vals)
        
    if len(row_values) == 1:
        if row_values[0] ==0 and row_values[1] == limit:
            continue

    sorted_row_values = sorted(row_values, key=lambda element: (element[0], element[1]))
    coverage = []
    coverage.append(sorted_row_values[0])
    if chosen_row == 11:
        print(0)
    for value in sorted_row_values:
        if (value[0] <= coverage[0][1] + 1):
            coverage[0][0] = min(coverage[0][0], value[0])
            coverage[0][1] = max(coverage[0][1], value[1])
        else:
            found_row = True
            print ((coverage[0][1] + 1)*limit + chosen_row)
            print(coverage)
        if coverage[0][0] == 0 and coverage[0][1] == limit:
            break
    