def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(int(line.strip()))
        
    return lines

data = read_input()

def get_increases_amount(depths_list):
    if len(depths_list) == 1:
        return 0
    current = depths_list[0]
    next_list = depths_list[1:]

    return int(current<next_list[0]) + get_increases_amount(next_list)

print(get_increases_amount(data))
