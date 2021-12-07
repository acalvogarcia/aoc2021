from statistics import mean
from functools import reduce
from math import floor, ceil

def read_input():
    with open("input.txt", "r") as input_file:
        return list(map(int, input_file.readline().split(",")))

data = read_input()

def T(n): return n*(n+1)/2

mean_position = mean(data)
result = min(
    int(reduce(lambda x,y: x + T(abs(y-floor(mean_position))), data, 0)),
    int(reduce(lambda x,y: x + T(abs(y-ceil(mean_position))), data, 0))
)
print(result)