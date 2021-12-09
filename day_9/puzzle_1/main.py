from functools import reduce

def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(list(line.strip()))
        return lines

data = read_input()

max_y = len(data)
max_x = len(data[0])

minimums = []

for i in range(max_y):
    for j in range(max_x):
        current = data[i][j]
        comparators = []
        if i != 0:
            comparators.append(data[i-1][j])
        if i < (max_y-1):
            comparators.append(data[i+1][j])
        if j !=0:
            comparators.append(data[i][j-1])
        if j < (max_x-1):
            comparators.append(data[i][j+1])
        if all(current < x for x in comparators):
            minimums.append(current)

print(sum([int(x)+1 for x in minimums]))

# def getUniqueNumbers(entry): return reduce(lambda x, y: x + bool(len(y) in [2, 3, 4, 7]), entry[1], 0)
# print(reduce(lambda x, y: x + getUniqueNumbers(y), data, 0))
