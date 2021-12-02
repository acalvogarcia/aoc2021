def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(line.strip())
        
    return lines

data = read_input()

position = [0,0,0]

for move in data:
    move_split = move.split(" ")
    if move.startswith("forward"):
        position[0] += int(move_split[1])
        position[1] += int(move_split[1])*position[2]
    elif move.startswith("down"):
        position[2] += int(move_split[1])
    elif move.startswith("up"):
        position[2] -= int(move_split[1])

print(position[0]*position[1])
