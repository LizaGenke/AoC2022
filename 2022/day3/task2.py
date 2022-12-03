import string

input = "day3\input.txt"
elf_items = []

with open(input) as f:
    while True:
        line = f.readline()
        if not line:
            break   
        elf_items.append(line)

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 27

sum_of_priorities = 0
group_size = 3
for i in range(0, len(elf_items), 3):
    for letter in elf_items[i]:
        if ((letter in elf_items[i+1]) and (letter in elf_items[i+2])):
            sum_of_priorities+=values[letter]
            break

print(sum_of_priorities)