from statistics import median
from functools import reduce

def read_input():
    with open("input.txt", "r") as input_file:
        return list(map(int, input_file.readline().split(",")))

data = read_input()

final_position = int(median(data))
print(reduce(lambda x,y: x + abs(y-final_position), data, 0))
