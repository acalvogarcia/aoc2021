from copy import deepcopy
from itertools import product

def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append([int(x) for x in list(line.strip())])
        return lines

data = read_input()

octo_matrix = deepcopy(data)
y_size = len(octo_matrix)
x_size = len(octo_matrix[0])

def increase_element(i,j, flashed):
    flashed_amount = 0

    if (i,j) in flashed:
        return flashed_amount, flashed

    value = octo_matrix[i][j]
    new_value = (value + 1)%10
    octo_matrix[i][j] = new_value

    if new_value == 0:
        flashed_amount = 1
        flashed.add((i,j))
        for new_i, new_j in product([i-1,i,i+1], [j-1,j,j+1]):
            if not (0 <= new_i < y_size) or not (0 <= new_j < x_size):
                continue
            new_flashed_amount, flashed = increase_element(new_i, new_j, flashed)
            flashed_amount += new_flashed_amount
    
    return flashed_amount, flashed


total_flashes = 0

for n in range(100):
    loop_flashes = 0
    flashed = set()
    for i, j in product(range(y_size), range(x_size)):
        flashed_amount, flashed = increase_element(i, j, flashed)
        loop_flashes += flashed_amount
    total_flashes += loop_flashes

print(total_flashes)
