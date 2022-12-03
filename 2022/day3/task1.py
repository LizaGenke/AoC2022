import string

input = "day3\input.txt"
compatment1items = []
compartment2items = []

with open(input) as f:
    while True:
        line = f.readline()
        if not line:
            break   
        compatment1items.append(line[0:int((len(line)-1)/2)])
        compartment2items.append(line[int((len(line)-1)/2):-1])

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 27

sum_of_priorities = 0
for i in range(len(compatment1items)):
    for letter in compatment1items[i]:
        if letter in compartment2items[i]:
            sum_of_priorities+=values[letter]
            break

print(sum_of_priorities)