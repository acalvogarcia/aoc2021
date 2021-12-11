def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(list(line.strip()))
        return lines

data = read_input()

characters_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

characters_value = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

illegal_characters = []
for line in data:
    current_chunk = []
    for character in line:
        if character in characters_map:
            current_chunk.append(character)
        else:
            if len(current_chunk) == 0:
                illegal_characters.append(character)
            if character != characters_map[current_chunk.pop()]:
                illegal_characters.append(character)

print(sum(characters_value[character] for character in illegal_characters))
