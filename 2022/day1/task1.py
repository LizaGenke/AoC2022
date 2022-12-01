input = "input.txt"
calories = []
current_elf_calories = []

with open(input) as f:
    while True:
        line = f.readline()
        if not line:
            break   
        if (len(line) == 1):
            calories.append(current_elf_calories)
            current_elf_calories = []
        else:
            current_elf_calories.append(int(line))   
 
summed_calories = []
for elf_calories_list in calories:
    calorie_sum = 0
    for calorie_item in elf_calories_list:
        calorie_sum += calorie_item
    summed_calories.append(calorie_sum)

print (max(summed_calories))