from functools import reduce

def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            line_split = line.split(" | ")
            lines.append((line_split[0].split(), line_split[1].split()))
        return lines

data = read_input()

def decode_entry(entry):
    whole_entry = entry[0] + entry[1]
    unique_entry = set(map(lambda s: "".join(sorted(s)), whole_entry))
    translation = {}
    for number in unique_entry:
        if len(number) == 2:
            translation[1] = set(number)
        elif len(number) == 3:
            translation[7] = set(number)
        elif len(number) == 4:
            translation[4] = set(number)
        elif len(number) == 7:
            translation[8] = set(number)
        if all(x in translation for x in [1,4,7,8]):
            break

    #   Segment indices:
    #    00 
    #   1  2
    #   1  2
    #    33
    #   4  5
    #   4  5
    #    66

    segments = [""]*9
    segments[0] = (translation[7] - translation[1]).pop()

    char_count = {}
    all_chars = ["a", "b", "c", "d", "e", "f", "g"]
    for char in all_chars:
        char_count[char] = len(list(filter(lambda l: char in l, set(unique_entry))))

    for item in char_count.items():
        if item[1] == 4:
            segments[4] = item[0]
        if item[1] == 6:
            segments[1] = item[0]
    
    segments[3] = (translation[4] - translation[1] - {segments[1]}).pop()

    not_fixed_numbers = filter(lambda l: len(l) not in [2,3,4,7], unique_entry)
    segments[6] = (reduce(lambda x, y: x.intersection(set(y)), not_fixed_numbers, set(all_chars)) - set(segments)).pop()

    numbers_with_6_lines = filter(lambda l: len(l) == 6, unique_entry)
    segments[5] = (reduce(lambda x, y: x.intersection(set(y)), numbers_with_6_lines, set(all_chars)) - set(segments)).pop()

    segments[2] = (set(all_chars) - set(segments)).pop()

    return segments

def get_entry_value(entry):
    segments = decode_entry(entry)

    digits_dictionary_2 = {
        frozenset(segments[i] for i in [0,1,2,4,5,6]): "0",
        frozenset(segments[i] for i in [2,5]): "1",
        frozenset(segments[i] for i in [0,2,3,4,6]): "2",
        frozenset(segments[i] for i in [0,2,3,5,6]): "3",
        frozenset(segments[i] for i in [1,2,3,5]): "4",
        frozenset(segments[i] for i in [0,1,3,5,6]): "5",
        frozenset(segments[i] for i in [0,1,3,4,5,6]): "6",
        frozenset(segments[i] for i in [0,2,5]): "7",
        frozenset(segments[i] for i in [0,1,2,3,4,5,6]): "8",
        frozenset(segments[i] for i in [0,1,2,3,5,6]): "9",
    }

    number_digits = "".join(
        [
            digits_dictionary_2[frozenset(s)]
            for s in entry[1]
        ]
    )

    return int(number_digits)

print(sum(get_entry_value(entry) for entry in data))
