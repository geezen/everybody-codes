from math import inf

def getquality(sword):
    spine = []
    quality = ""
    for num in map(int, sword.split(':')[1].split(',')):
        for segment in spine:
            if num < segment[1] and segment[0] == -1:
                segment[0] = num
                break
            elif num > segment[1] and segment[2] == -1:
                segment[2] = num
                break
        else:
            spine.append([-1, num, -1])
            quality += str(num)
    return int(quality)

weakest = float(inf)
strongest = 0
for sword in open("2025/q5/in2.txt").readlines():
    quality = getquality(sword)
    weakest = min(weakest, quality)
    strongest = max(strongest, quality)
print(strongest-weakest)