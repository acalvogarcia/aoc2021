from collections import Counter
from os import spawnl

def read_input():
    with open("input.txt", "r") as input_file:
        rules = []

        first_line = True
        for line in input_file:
            if first_line:
                template = line.strip()
                first_line = False
                continue
            if line == "\n":
                continue
            rules.append(line.strip().split(" -> "))

        return template, rules

data = read_input()

template = data[0]
rules = {key: value for key, value in data[1]}


def split_pair(pair):
    result_first_part = pair[0] + rules[pair]
    result_second_part = rules[pair] + pair[1]
    return result_first_part, result_second_part


def split_template(template, letters_counter, steps):
    if steps == 0:
        return letters_counter

    new_template = Counter()

    for pair, amount in template.items():
        first_new_pair, second_new_pair = split_pair(pair)
        new_template[first_new_pair] += amount
        new_template[second_new_pair] += amount
        letters_counter[second_new_pair[0]] += amount
    
    return split_template(new_template, letters_counter, steps-1)

template_counter = Counter(
    [template[i] + template[i+1] for i in range(len(template)-1)]
)
letters_counter = Counter(template)

result = split_template(template_counter, letters_counter, 40)
print(Counter(result).most_common()[0][1] - Counter(result).most_common()[-1][1])
