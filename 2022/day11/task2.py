import math

# rem is remainder in division
class Item:
    def __init__(self, starting_number):
        self.number = starting_number
        self.rem = {}
        for key in test_numbers:
            self.rem[key] = self.number % key
    def Add(self, number):
        for key in self.rem:
            self.rem[key] += number
            self.rem[key] %= key
    def Multiply(self, number):
        for key in self.rem:
            self.rem[key] *= number
            self.rem[key] %= key
    def Square(self):
        for key in self.rem:
            self.rem[key] = self.rem[key]**2
            self.rem[key] %= key
    def Test(self, number):
        if self.rem[number] == 0:
            return True
        else:
            return False

class Monkey:
    def __init__(self, starting_items, operation_type, operation_number, test_number, throw_true, throw_false):
        self.items = [Item(item) for item in starting_items]
        self.operation = operation_type
        self.coefficient = operation_number
        self.divisibility_test = test_number
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.number_of_inspections = 0
    def Inspect(self):
        if self.operation == "+":
            self.items[0].Add(self.coefficient)
        elif self.operation == "*":
            self.items[0].Multiply(self.coefficient)
        else:
            self.items[0].Square()
        self.number_of_inspections += 1
        return
    def Test(self):
        if self.items[0].Test(self.divisibility_test) == True:
            return self.items[0], self.throw_true
        else:
            return self.items[0], self.throw_false
    def Throw(self):
        self.items.pop(0)
        return
    def Add(self, item):
        self.items.append(item)
        return 

num_monkeys = 8
starting_items= [[53, 89, 62, 57, 74, 51, 83, 97], 
                 [85, 94, 97, 92, 56], 
                 [86, 82, 82],
                 [94, 68],
                 [83, 62, 74, 58, 96, 68, 85],
                 [50, 68, 95, 82],
                 [75],
                 [92, 52, 85, 89, 68, 82]]

operation_types = ["*", "+", "+", "+", "+", "+", "*", "**"]
operation_numbers = [3,2,1,5,4,8,7,None]
test_numbers = [13,19,11,17,3,7,5,2]
throw_true_id = [1,5,3,7,3,2,7,0]
throw_false_id = [5,2,4,6,6,4,0,1] 

monkeys = []

num_monkeys = 8
for i in range(num_monkeys):
    monkeys.append(Monkey(starting_items[i], operation_types[i], operation_numbers[i], test_numbers[i], throw_true_id[i], throw_false_id[i]))

number_of_rounds = 10000

for round in range(number_of_rounds):
    for monkey in monkeys:
        starting_items_len = len(monkey.items)
        for i in range(starting_items_len):
            monkey.Inspect()
            item_to_throw, throw_to_id = monkey.Test()
            monkey.Throw()
            monkeys[throw_to_id].Add(item_to_throw)

for i, monkey in enumerate(monkeys):
    print("Monkey ", i," inspected items ", monkey.number_of_inspections, " times.")