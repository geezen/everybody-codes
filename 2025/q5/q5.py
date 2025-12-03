spine = []
quality = ""

for num in map(int, open("2025/q5/in1.txt").read().split(':')[1].split(',')):
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
print(quality)