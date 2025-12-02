import re
from math import copysign

def div(x, y):
    return complex(copysign(abs(x.real) // y.real, x.real), copysign(abs(x.imag) // y.imag, x.imag))

# part 1
a = complex(*map(int, re.findall(r"-?\d+", open("2025/q2/in1.txt").read())))
r = 0+0j
for _ in range(3):
    r = r * r
    r = div(r, 10+10j)
    r = r + a
print(f"[{r.real:.0f},{r.imag:.0f}]")

# part 2
a = complex(*map(int, re.findall(r"-?\d+", open("2025/q2/in2.txt").read())))
engraved = 0
for x in range(101):
    for y in range(101):
        p = a + x*10 + y*10j
        r = 0+0j
        for _ in range(100):
            r = r * r
            r = div(r, 100000+100000j)
            r = r + p
            if abs(r.real) > 1000000 or abs(r.imag) > 1000000:
                break
        else:
            engraved += 1
print(f"engraved points: {engraved}")

# part 3
a = complex(*map(int, re.findall(r"-?\d+", open("2025/q2/in3.txt").read())))
engraved = 0
for x in range(1001):
    for y in range(1001):
        p = a + x + y*1j
        r = 0+0j
        for _ in range(100):
            r = r * r
            r = div(r, 100000+100000j)
            r = r + p
            if abs(r.real) > 1000000 or abs(r.imag) > 1000000:
                break
        else:
            engraved += 1
    print(f"{(x/1001*100):.1f}%")
print(f"engraved points: {engraved}")