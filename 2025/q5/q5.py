def parsesword(sword):
    identifier, elements = sword.split(':')
    spine = []
    for num in map(int, elements.split(',')):
        for segment in spine:
            if num < segment[1] and segment[0] == -1:
                segment[0] = num
                break
            elif num > segment[1] and segment[2] == -1:
                segment[2] = num
                break
        else:
            spine.append([-1, num, -1])
    return identifier, spine

def getquality(sword):
    quality = ""
    for segment in sword[1]:
        quality += str(segment[1])
    return int(quality)

def getrank(sword):
    rank = []
    rank.append(getquality(sword))
    for segment in sword[1]:
        num = ""
        for digit in segment:
            if digit != -1:
                num += str(digit)
        rank.append(int(num))
    rank.append(int(sword[0]))
    return rank

# Part 1
sword = parsesword(open("2025/q5/in1.txt").read())
quality = getquality(sword)
print(f"Part 1: {quality}")

# Part 2
weakest = float('inf')
strongest = 0
for sword in map(parsesword, open("2025/q5/in2.txt").readlines()):
    quality = getquality(sword)
    weakest = min(weakest, quality)
    strongest = max(strongest, quality)
print(f"part 2: {strongest-weakest}")

# Part 3
swords = list(map(parsesword, open("2025/q5/in3.txt").read().splitlines()))
swords.sort(key=getrank, reverse=True)
checksum = 0
for pos, sword in enumerate(swords, 1):
    checksum += pos * int(sword[0])
print(f"part 3: {checksum}")