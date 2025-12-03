gears = [int(line) for line in open("2025/q4/in1.txt").readlines()]

# part 1
print(f"part 1: {2025 * gears[0] // gears[-1]}")