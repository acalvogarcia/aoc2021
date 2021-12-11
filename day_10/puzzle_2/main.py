from statistics import median

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
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

incomplete_chunks = []
for line in data:
    current_chunk = []
    line_corrupted = False
    for character in line:
        if character in characters_map:
            current_chunk.append(character)
        elif len(current_chunk) == 0:
            line_corrupted = True
            break
        elif character != characters_map[current_chunk.pop()]:
            line_corrupted = True
            break
    if not line_corrupted:
        incomplete_chunks.append(current_chunk)

chunk_completions = []
for chunk in incomplete_chunks:
    missing_closers = []
    for idx, character in enumerate(chunk):
        if character in characters_map:
            if (closer := characters_map[character]) not in chunk[idx+1:]:
                missing_closers.append(closer)
    chunk_completions.append(list(reversed(missing_closers)))

def get_completion_value(completion):
    result = 0
    for character in completion:
        result = result*5 + characters_value[character]
    return result

print(median(get_completion_value(completion) for completion in chunk_completions))
