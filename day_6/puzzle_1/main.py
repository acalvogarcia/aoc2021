from typing import Dict


def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(list(map(int, line.split(","))))
        
    return lines


data = read_input()[0]
lanternfish_data = {days: data.count(days) for days in range(9)}


def get_lanternfish_amount(lanternfish: Dict[int, int], days: int):
    if days == 0:
        return lanternfish
    new_lanternfish = {i: lanternfish[i+1] for i in range(8)}
    new_lanternfish[8] = lanternfish[0]
    new_lanternfish[6] = new_lanternfish[6] + lanternfish[0]
    return get_lanternfish_amount(new_lanternfish, days-1)


final_lanternfish = get_lanternfish_amount(lanternfish_data, 80)
print(sum(final_lanternfish.values()))
