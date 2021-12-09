from functools import reduce

def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            line_split = line.split(" | ")
            lines.append((line_split[0].split(), line_split[1].split()))
        return lines

data = read_input()

def getUniqueNumbers(entry): return reduce(lambda x, y: x + bool(len(y) in [2, 3, 4, 7]), entry[1], 0)
print(reduce(lambda x, y: x + getUniqueNumbers(y), data, 0))
