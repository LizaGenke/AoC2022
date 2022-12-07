import re

input = "day7/input.txt"

class Node:
    def __init__(self, name, children=None):
        self.name = name
        self.total_size = 0
        self.indirect_size = 0
        self.file_size = 0
        self.children = []
        self.parent = None
        for child in self.children:
            child.parent = self
    def AddChild(self,name):
        self.children.append(Node(name))
        for child in self.children:
            child.parent = self
    def __iter__(self):
        # first, yield everthing every one of the child nodes would yield.
        for child in self.children:
            for item in child:
                # the two for loops is because there's multiple children, and we need to iterate
                # over each one.
                yield item
        # finally, yield self
        yield self
    def AddValueToParent(self, value):
        if self.parent!=None:
           self.parent.total_size += value
           self.parent.AddValueToParent(value)


current_location = ["/"]
current_folder_name = "/"

root_node = Node(current_folder_name)
current_node = root_node
readContents = False
contents = []

with open(input) as f:
    while True:
        line = f.readline()
        if not line:
            if (len(contents)!=0):
                filesize = 0
                children_dirs = []
                for item in contents:
                    if item[0:4] != "dir ":
                        if re.search("[0-9]*", item)[0] != '':
                            filesize += int("".join(re.findall("[0-9]*", item)[0]))
                    else:
                        children_dirs.append(item[4:])
                for child in children_dirs:
                    current_node.AddChild(child)
                current_node.file_size = filesize
                current_node.total_size = filesize
                current_node.AddValueToParent(filesize)
                if (current_location == ["/"]):
                    root_node = current_node
                contents = []
                readContents = False
            break 
        if line[0] == "$":
            if (len(contents)!=0):
                filesize = 0
                children_dirs = []
                for item in contents:
                    if item[0:4] != "dir ":
                        if re.search("[0-9]*", item)[0] != '':
                            filesize += int("".join(re.findall("[0-9]*", item)[0]))
                    else:
                        children_dirs.append(item[4:])
                for child in children_dirs:
                    current_node.AddChild(child)
                current_node.file_size = filesize
                current_node.total_size = filesize
                current_node.AddValueToParent(filesize)
                if (current_location == ["/"]):
                    root_node = current_node
                contents = []
                readContents = False
            if line[0:6] == "$ cd /":
                current_location = ["/"]
                continue
            elif line[0:4] == "$ cd":
                print(current_location)
                if line[0:7] == "$ cd ..":
                    current_location.pop(-1)
                    current_node = current_node.parent
                else:
                    for child in current_node.children:
                        if child.name == line[5:-1]:
                            current_node = child
                            current_location.append(line[5:-1])
                            break
            else:
                if line[0:4] == "$ ls":
                    readContents = True
                    continue
        if (readContents):
            contents.append(line.strip("\n"))

sum_less_than_100000 = 0

print(root_node.total_size)

disk_space = 70000000
update_space = 30000000
space_to_free_up = root_node.total_size - (disk_space - update_space)

candidate_node = root_node

for node in root_node:
    if node.total_size>=space_to_free_up and node.total_size<candidate_node.total_size:
        candidate_node = node

print(candidate_node.total_size)