from statistics import mean
from functools import reduce

def read_input():
    with open("input.txt", "r") as input_file:
        return list(map(int, input_file.readline().split(",")))

data = read_input()

def T(n): return n*(n+1)/2

final_position = int(mean(data))
print(int(reduce(lambda x,y: x + T(abs(y-final_position)), read_input(), 0)))
