from math import inf

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

def getquality(spine):
    quality = ""
    for segment in spine:
        quality += str(segment[1])
    return int(quality)

def getrank(sword):
    rank = []
    rank.append(getquality(sword[1]))
    for segment in sword[1]:
        num = ""
        for digit in segment:
            if digit != -1:
                num += str(digit)
        rank.append(int(num))
    rank.append(int(sword[0]))
    return rank

# Part 2
weakest = float(inf)
strongest = 0
for sword in open("2025/q5/in2.txt").readlines():
    quality = getquality(parsesword(sword)[1])
    weakest = min(weakest, quality)
    strongest = max(strongest, quality)
print(f"part 2: {strongest-weakest}")

# Part 3
swords = list(map(parsesword, open("2025/q5/in3.txt").read().splitlines()))
swords.sort(key=getrank, reverse=True)
checksum = 0
for pos, sword in enumerate(swords):
    checksum += (pos + 1) * int(sword[0])
print(f"part 3: {checksum}")