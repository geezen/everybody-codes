# part1
crates = {int(x) for x in open("2025/q3/in1.txt").read().split(',')}
print(f"part1: {sum(crates)}")

# part2
crates = list({int(x) for x in open("2025/q3/in2.txt").read().split(',')})
crates.sort()
print(f"part2: {sum(crates[0:20])}")