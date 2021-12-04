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

oxygen_most_common = [int(x/len(data) >= 0.5) for x in data_reduced]
co2_most_common = [int(x/len(data) <= 0.5) for x in data_reduced]

def check_measurement_value(data, preferred, check_most_common, position=0):
    if len(data) == 1:
        return data[0]
    average = functools.reduce(lambda x,y: x + y[position], data, 0)/len(data)
    reference = int(average >= 0.5 if check_most_common else average <0.5)

    filtered_data = [point for point in data if point[position] == reference]

    return check_measurement_value(filtered_data, preferred, check_most_common, position+1)

oxygen_value = "".join(map(str, check_measurement_value(data, 1, True)))
co2_value = "".join(map(str, check_measurement_value(data, 0, False)))

print(int("".join(oxygen_value), 2) * int("".join(co2_value), 2))
