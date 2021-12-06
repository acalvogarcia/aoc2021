import numpy
from numpy.linalg import matrix_power

def read_input():
    with open("input.txt", "r") as input_file:
        return list(map(int, input_file.readline().split(",")))

data = read_input()

lanternfish_start = numpy.array([data.count(i) for i in range(9)])
day_transformation = numpy.array([
    [1 if j==(i+1)%9 or (j==0 and i==6) else 0 for j in range(9)]
    for i in range(9)
])
lanternfish_end = matrix_power(day_transformation, 256).dot(lanternfish_start)
print(sum(lanternfish_end))

# The day transformation matrix is:
# [0 1 0 0 0 0 0 0 0]
# [0 0 1 0 0 0 0 0 0]
# [0 0 0 1 0 0 0 0 0]
# [0 0 0 0 1 0 0 0 0]
# [0 0 0 0 0 1 0 0 0]
# [0 0 0 0 0 0 1 0 0]
# [1 0 0 0 0 0 0 1 0]
# [0 0 0 0 0 0 0 0 1]
# [1 0 0 0 0 0 0 0 0]
