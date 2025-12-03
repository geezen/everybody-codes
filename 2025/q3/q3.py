from collections import Counter

# part1
crates = {int(x) for x in open("2025/q3/in1.txt").read().split(',')}
print(f"part1: {sum(crates)}")

# part2
crates = list({int(x) for x in open("2025/q3/in2.txt").read().split(',')})
crates.sort()
print(f"part2: {sum(crates[0:20])}")

#part3
crates = [int(x) for x in open("2025/q3/in3.txt").read().split(',')]
print(f"part3: {Counter(crates).most_common(1)[0][1]}")