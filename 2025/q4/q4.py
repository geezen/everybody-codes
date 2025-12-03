import math

gears = [int(line) for line in open("2025/q4/in2.txt").readlines()]

# part 1
print(f"part 1: {2025 * gears[0] // gears[-1]}")

# part 2
print(f"part 2: {math.ceil(10000000000000 * gears[-1]/ gears[0])}")