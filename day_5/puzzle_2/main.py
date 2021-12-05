from typing import List

class Movement:
    def __init__(self, line):
        line_split = list(map(lambda s: s.split(","), line.split(" -> ")))
        self.x1 = int(line_split[0][0])
        self.y1 = int(line_split[0][1])
        self.x2 = int(line_split[1][0])
        self.y2 = int(line_split[1][1])

    def get_points_travelled(self):
        if self.x1 != self.x2 and self.y1 != self.y2:
            if self.x2 > self.x1:
                x_points = [self.x1 + i for i in range(self.x2 - self.x1 + 1)]
            else:
                x_points = [self.x1 - i for i in range(self.x1 - self.x2 + 1)]
            if self.y2 > self.y1:
                y_points = [self.y1 + i for i in range(self.y2 - self.y1 + 1)]
            else:
                y_points = [self.y1 - i for i in range(self.y1 - self.y2 + 1)]
            for i in range(len(x_points)):
                yield (x_points[i], y_points[i])
        elif self.x1 != self.x2:
            if self.x2 > self.x1:
                for x in range(self.x1, self.x2+1):
                    yield (x, self.y1)
            else:
                for x in range(self.x1, self.x2-1, -1):
                    yield (x, self.y1)
        elif self.y1 != self.y2:
            if self.y2 > self.y1:
                for y in range(self.y1, self.y2+1):
                    yield (self.x1, y)
            else:
                for y in range(self.y1, self.y2-1, -1):
                    yield (self.x1, y)

    def __repr__(self):
        return f"({self.x1}, {self.y1}) -> ({self.x2}, {self.y2})"


def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(Movement(line))
        
    return lines

data: List[Movement] = read_input()

all_points_travelled = {}

for movement in data:
    for point in movement.get_points_travelled():
        if point in all_points_travelled:
            all_points_travelled[point] += 1
        else:
            all_points_travelled[point] = 1

print(len(list(filter(lambda x: x > 1, all_points_travelled.values()))))
