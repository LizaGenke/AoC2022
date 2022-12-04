input = "day4\input.txt"

overlapping_pairs_count = 0

with open(input) as f:
    while True:
        line = f.readline()
        if not line:
            break   
        ranges = line.split(",")
        first_range = ranges[0].split("-")
        first_range_numbers = []
        for number in first_range:
            first_range_numbers.append(int(number))
        second_range = ranges[1].split("-")
        second_range_numbers = []
        for number in second_range:
            second_range_numbers.append(int(number))
        if (((first_range_numbers[0] >= second_range_numbers[0]) and (first_range_numbers[0] <= second_range_numbers[1])) or 
            ((second_range_numbers[0] >= first_range_numbers[0]) and (second_range_numbers[0] <= first_range_numbers[1]))):
            overlapping_pairs_count += 1
            print(first_range, " and ", second_range)

print(overlapping_pairs_count)