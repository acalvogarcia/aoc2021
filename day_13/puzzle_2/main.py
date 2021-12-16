from pprint import pprint

def read_input():
    with open("input.txt", "r") as input_file:
        positions = set()
        moves = []
        for line in input_file:
            if line == "\n":
                break
            line_split = line.strip().split(",")
            positions.add((int(line_split[0]), int(line_split[1])))
        for line in input_file:
            move_split = line.strip().removeprefix("fold along ").split("=")
            moves.append(
                (
                    int(move_split[0] == "y"),
                    int(move_split[1])
                )
            )
        return positions, moves

data = read_input()

positions = data[0]
moves = data[1]


def fold_position(position, fold_direction, fold_value):
    position_list = [position[0], position[1]]
    if position[fold_direction] > fold_value:
        position_list[fold_direction] = 2*fold_value - position_list[fold_direction]
    
    return tuple(position_list)

def fold_result(positions, moves):
    move = moves[0]
    folded_positions = set([
        fold_position(position, move[0], move[1])
        for position in positions
    ])
    if len(moves) == 1:
        return folded_positions
    return fold_result(folded_positions, moves[1:])

def get_screen_output(positions):
    x_size = max(position[0] for position in positions)+1
    y_size = max(position[1] for position in positions)+1

    display = [["."]*x_size for i in range(y_size)]

    for position in positions:
        display[position[1]][position[0]] = "#"

    display = ["".join(line) for line in display]

    return display

for line in get_screen_output(fold_result(positions, moves)):
    print(line)
