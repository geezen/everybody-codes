import re
from math import copysign

def div(x, y):
    return complex(copysign(abs(x.real) // y.real, x.real), copysign(abs(x.imag) // y.imag, x.imag))

# part 1
a = complex(*map(int, re.findall(r"\d+", open("2025/q2/ex1.txt").read())))
r = 0+0j
for _ in range(3):
    r = r * r
    r = div(r, 10+10j)
    r = r + a
print(f"[{r.real},{r.imag}]")