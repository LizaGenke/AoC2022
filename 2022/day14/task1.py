input = "day14/input.txt"

rock_paths = []
with open(input) as f:
    while True:
        path = f.readline()
        if not path:
            break 
        rock_paths.append(path.strip("\n"))

max_x = 0
max_y = 0
for path in rock_paths:
    coords = path.split(" -> ")
    for coord in coords:
        x, y = coord.split(",")
        if int(x) > max_x:
            max_x = int(x)
        if int(y) > max_y:
            max_y = int(y)

source_x = 500
source_y = 0

cave_map = []

for row in range (max_y+1):
    cave_map.append([])
    for column in range (max_x + 1):
        cave_map[row].append(".")

cave_map[source_y][source_x] = "+"



for path in rock_paths:
    coords = path.split(" -> ")
    cur_x, cur_y = [int(i) for i in coords[0].split(",")]
    for i in range (1, len(coords)):
        old_x, old_y = cur_x, cur_y
        cur_x, cur_y = [int(i) for i in coords[i].split(",")]
        if old_x == cur_x:
            for y in range(min(old_y, cur_y), max(old_y, cur_y) + 1):
                cave_map[y][cur_x] = "#"
        else:
            for x in range(min(old_x, cur_x), max(old_x, cur_x) + 1):
                cave_map[cur_y][x] = "#"

for line in cave_map:
    for i, char in enumerate(line):
        if i > 493:
            print(char, end='')
    print("\n", end='')  
            
move_to_void = False
sand_count = 0

while (move_to_void == False):
    #try to add new sand particle
    if cave_map[1][500] != ".":
        break
    can_move = True
    sand_x = 500
    sand_y = 1
    while(can_move):
        if sand_y + 1 == len(cave_map):
            can_move = False
            move_to_void = True
            break
        if cave_map[sand_y + 1][sand_x] == ".":
            sand_y +=1
        else:
            if sand_x - 1 < 0:
                move_to_void = True
                can_move = False
                continue
            if sand_x + 1 >= len(cave_map[0]):
                move_to_void = True
                break
            if cave_map[sand_y + 1][sand_x - 1] == ".":
               sand_y += 1
               sand_x -= 1
            elif cave_map[sand_y + 1][sand_x + 1] == ".":
               sand_y += 1
               sand_x += 1
            else:
                can_move = False
                cave_map[sand_y][sand_x] = "o"
                sand_count += 1
        continue


print(sand_count)    

for line in cave_map:
    for i, char in enumerate(line):
        if i > 493:
            print(char, end='')
    print("\n", end='')  