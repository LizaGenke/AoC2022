input = "day8/input.txt"

map_of_trees = []

with open(input) as f:
    while True:
        row_of_trees = f.readline()
        if not row_of_trees:
            break 
        map_of_trees.append(row_of_trees.strip("\n"))

num_visible_trees = 0
for i,row in enumerate(map_of_trees):
    for j,column in enumerate(row):
        visible_from_top = True
        visible_from_right = True
        visible_from_bottom = True
        visible_from_left = True
        #check if visible from top
        for y in range(i, 0, -1):
            if int(map_of_trees[i][j]) <= int(map_of_trees[y-1][j]):
                visible_from_top = False
                break
        if (visible_from_top == True):
            num_visible_trees += 1
            print("tree ", i, ",", j, "visible from top")
            continue
        #check if visible from right
        for x in range(j+1, len(row), 1):
            if int(map_of_trees[i][j]) <= int(map_of_trees[i][x]):
                visible_from_right = False
                break
        if (visible_from_right == True):
            num_visible_trees += 1
            print("tree ", i, ",", j, "visible from right")
            continue
        #check if visible from bottom
        for y in range(i+1, len(map_of_trees), 1):
            if int(map_of_trees[i][j]) <= int(map_of_trees[y][j]):
                visible_from_bottom = False
                break
        if (visible_from_bottom == True):
            num_visible_trees += 1
            print("tree ", i, ",", j, "visible from bottom")
            continue
        #check if visible from left
        for x in range(j, 0, -1):
            if int(map_of_trees[i][j]) <= int(map_of_trees[i][x-1]):
                visible_from_left = False
                break
        if (visible_from_left == True):
            num_visible_trees += 1
            print("tree ", i, ",", j, "visible from left")
            continue

print(num_visible_trees)