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

def fold_result(positions, move):
    return set([
        fold_position(position, move[0], move[1])
        for position in positions
    ])

print(len(fold_result(positions, moves[0])))
