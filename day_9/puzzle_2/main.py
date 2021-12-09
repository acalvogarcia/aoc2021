def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(list(line.strip()))
        return lines

data = read_input()

max_y = len(data)
max_x = len(data[0])

def checkBiggerNeighbours(i, j):
    current = data[i][j]
    comparators = []
    if i != 0:
        comparators.append(data[i-1][j])
    if i < (max_y-1):
        comparators.append(data[i+1][j])
    if j !=0:
        comparators.append(data[i][j-1])
    if j < (max_x-1):
        comparators.append(data[i][j+1])
    if all(current < x for x in comparators):
        return current

def checkBasin(i,j, already_found = None):
    if already_found is None:
        already_found = {(i,j)}
    bigger_neighbours = set()
    result = {(i,j)}
    current = data[i][j]
    if i != 0 and (x := data[i-1][j]) != "9" and x > current:
        bigger_neighbours.add((i-1,j))
    if i < (max_y-1) and (x := data[i+1][j]) != "9" and x > current:
        bigger_neighbours.add((i+1,j))
    if j != 0 and (x := data[i][j-1]) != "9" and x > current:
        bigger_neighbours.add((i,j-1))
    if j < (max_x-1) and (x := data[i][j+1]) != "9" and x > current:
        bigger_neighbours.add((i,j+1))
    # already_found.update(bigger_neighbours)
    for neighbour in bigger_neighbours:
        if neighbour not in already_found:
            neighbour_basin = checkBasin(neighbour[0], neighbour[1], already_found)
            result.update(neighbour_basin)
            already_found.add(neighbour)
    return result



basins = []

for i in range(max_y):
    for j in range(max_x):
        if current := checkBiggerNeighbours(i, j):
            basins.append(checkBasin(i,j))

basin_lenghts = sorted([len(basin) for basin in basins], reverse=True)
print(basin_lenghts[0]*basin_lenghts[1]*basin_lenghts[2])
# print([len(basin) for basin in basins])
# print(sum([int(x)+1 for x in minimums]))

# def getUniqueNumbers(entry): return reduce(lambda x, y: x + bool(len(y) in [2, 3, 4, 7]), entry[1], 0)
# print(reduce(lambda x, y: x + getUniqueNumbers(y), data, 0))
