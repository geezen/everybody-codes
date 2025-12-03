import math

gears = [int(line) for line in open("2025/q4/in2.txt").readlines()]

# part 1
print(f"part 1: {2025 * gears[0] // gears[-1]}")

# part 2
print(f"part 2: {math.ceil(10000000000000 * gears[-1]/ gears[0])}")

# part 3
gears = [tuple(map(int, line.split('|'))) for line in open("2025/q4/in3.txt").readlines()]
teethturns = 100 * gears[0][0]
for gear in gears[1:-1]:
    teethturns /= gear[0]
    teethturns *= gear[1]
fullturns = teethturns // gears[-1][0]
print(f"part3: {fullturns:.0f}")