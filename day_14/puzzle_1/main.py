from collections import Counter

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


def split_pair(pair, steps):
    if steps == 0:
        return pair
    pair_after_rule = f"{pair[0]}{rules[pair]}{pair[1]}"
    result_first_part = split_pair(pair_after_rule[:2], steps-1)
    result_second_part = split_pair(pair_after_rule[1:], steps-1)[1:]
    return result_first_part + result_second_part


def split_template(template, steps):
    pairs_with_insertions = [
        split_pair(template[i:i+2], steps)
        for i in range(len(template)-1)
    ]
    result = pairs_with_insertions[0] + "".join([
        batch[1:] for batch in pairs_with_insertions[1:]
    ])
    return result


result = split_template(template, 40)
print(Counter(result).most_common()[0][1] - Counter(result).most_common()[-1][1])
