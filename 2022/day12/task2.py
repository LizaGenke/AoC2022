input = "day12/input.txt"

class Node:
    def __init__(self):
        self.parent = None
        self.explored = False
        self.adjacent = []
        self.possible_start = False

heightmap_rows = []

with open(input) as f:
    while True:
        instruction = f.readline()
        if not instruction:
            break 
        heightmap_rows.append(instruction.strip("\n"))

width = len(heightmap_rows[0])
height = len(heightmap_rows)

graph_map = {}
end_node_id = 0

for i, row in enumerate(heightmap_rows):
    for j, column in enumerate(row):
        node_id = i*width + j
        node_value = ord(heightmap_rows[i][j])
        if heightmap_rows[i][j] == "S":
            node_value = ord("a")
        if heightmap_rows[i][j] == "E":
            end_node_id = node_id
            node_value = ord("z")
        graph_map[node_id] = Node()
        if node_value == ord("a"):
            graph_map[node_id].possible_start = True
        # right
        if (j+1 < width) and (node_value  + 1 >= ord(heightmap_rows[i][j+1])):
            graph_map[node_id].adjacent.append(i*width + j + 1)
        # up
        if (i - 1 >= 0) and (node_value  + 1 >= ord(heightmap_rows[i-1][j])):
            graph_map[node_id].adjacent.append((i-1)*width + j)
        # left
        if (j - 1 >= 0) and (node_value  + 1 >= ord(heightmap_rows[i][j-1])):
            graph_map[node_id].adjacent.append((i)*width + j - 1)
        # down
        if (i + 1 < height) and (node_value  + 1 >= ord(heightmap_rows[i+1][j])):
            graph_map[node_id].adjacent.append((i+1)*width + j)

def BFS(tree, start_node_id, end_node_id):
    Q = []
    tree[start_node_id].explored = True
    Q.append(start_node_id)
    while len(Q) != 0:
        v = Q.pop(0)
        if v == end_node_id:
            return tree[v]
        for edge in tree[v].adjacent:
            if tree[edge].explored == False:
                tree[edge].explored = True
                tree[edge].parent = v
                Q.append(edge)


shortest_path = width * height

for key in graph_map.keys():
    if graph_map[key].possible_start == True:
        for node in graph_map.keys():
            graph_map[node].explored = False
        last_node = BFS(graph_map, key, end_node_id)
        if last_node == None:
            continue
        path = []
        parent = last_node.parent
        while (parent != key):
            path.append(parent)
            parent = graph_map[parent].parent
        pathlength = len(path) + 1
        if pathlength < shortest_path:
            shortest_path = pathlength

print(shortest_path)