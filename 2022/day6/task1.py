input = "day6/input.txt"

with open(input) as f:
    while True:
        datastream = f.readline()
        package = []
        last_added_index = 0
        for char in datastream:
            last_added_index += 1
            package.append(char)
            if len(package) > 14:
                package.pop(0)
                if (len(set(package)) == len(package)):
                    print(last_added_index)
                    break   
        if not datastream:
            break 