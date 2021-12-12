from copy import deepcopy
from itertools import product
from typing import Dict, List

def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(line.strip().split("-"))
        return lines

data = read_input()

def transform_data(data):
    transformed = {}
    for line in data:
        if line[0] in transformed:
            transformed[line[0]].add(line[1])
        else:
            transformed[line[0]] = {line[1]}
        if line[1] in transformed:
            transformed[line[1]].add(line[0])
        else:
            transformed[line[1]] = {line[0]}
    return transformed

mapped_points = transform_data(data)

def get_paths(point: str, path: List[str], mapped_points: Dict[str, List[str]], small_twice = False):
    path = deepcopy(path)
    if point == "end":
        return 1

    if point == "start" and path:
        return 0
    elif point.islower() and point in path:
        if small_twice == True:
            return 0
        small_twice = True
    
    if point == "start":
        path = ["start"]
    else:
        path.append(point)

    return sum(
        [
            get_paths(element, path, mapped_points, small_twice)
            for element in mapped_points[point]
        ]
    )

print(get_paths("start", [], mapped_points))
