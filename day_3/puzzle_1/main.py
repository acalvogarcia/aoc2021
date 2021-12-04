import functools

def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(line.strip())
        
    return lines

data = read_input()

data = list(map(lambda s: [int(c) for c in s], data))
data_reduced = functools.reduce(lambda x,y: list(map(sum, zip(x,y))), data)

gamma = "".join([str(int(x > len(data)/2)) for x in data_reduced])
epsilon = "".join([str(int(x <= len(data)/2)) for x in data_reduced])

print(int(gamma, 2) * int(epsilon, 2))
