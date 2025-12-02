crates = [int(x) for x in open("2025/q3/in1.txt").read().split(',')]
print(f"part1: {sum(set(crates))}")