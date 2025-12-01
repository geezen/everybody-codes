names, instructions = map(lambda s: s.split(','), open("2025/q1/in1.txt").read().split("\n\n"))

cur = 0
for instruction in instructions:
    if instruction[0] == 'R':
        cur += int(instruction[1:])
    else:
        cur -= int(instruction[1:])
    cur = max(cur, 0)
    cur = min(cur, len(names) - 1)

print(names[cur])