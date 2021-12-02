def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(int(line.strip()))
        
    return lines

data = read_input()
    

count = 0
for idx, line in enumerate(data):
    if idx < 3:
        continue

    if sum(data[idx-i-1] for i in range(3)) < sum(data[idx-i] for i in range(3)):
        count += 1

print(count)
