input = "day8/input.txt"

map_of_trees = []

with open(input) as f:
    while True:
        row_of_trees = f.readline()
        if not row_of_trees:
            break 
        map_of_trees.append(row_of_trees.strip("\n"))

max_scenic_score = 0
for i,row in enumerate(map_of_trees):
    for j,column in enumerate(row):
        viewing_distance_from_top = 0
        viewing_distance_from_right = 0
        viewing_distance_from_bottom = 0
        viewing_distance_from_left = 0
        #check if visible from top
        for y in range(i, 0, -1):
            viewing_distance_from_top +=1
            if int(map_of_trees[i][j]) <= int(map_of_trees[y-1][j]):
                break
        #check if visible from right
        for x in range(j+1, len(row), 1):
            viewing_distance_from_right += 1
            if int(map_of_trees[i][j]) <= int(map_of_trees[i][x]):
                break
        #check if visible from bottom
        for y in range(i+1, len(map_of_trees), 1):
            viewing_distance_from_bottom += 1
            if int(map_of_trees[i][j]) <= int(map_of_trees[y][j]):
                break
        #check if visible from left
        for x in range(j, 0, -1):
            viewing_distance_from_left += 1
            if int(map_of_trees[i][j]) <= int(map_of_trees[i][x-1]):
                visible_from_left = False
                break
        scenic_score = viewing_distance_from_top * viewing_distance_from_right * viewing_distance_from_bottom * viewing_distance_from_left
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)


