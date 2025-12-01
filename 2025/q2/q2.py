A = (158, 57)
R = (0, 0)

def add(X, Y):
    return (X[0] + Y[0], X[1] + Y[1])

def multiply(X, Y):
    return (X[0] * Y[0] - X[1] * Y[1], X[0] * Y[1] + X[1] * Y[0])

def div(X, Y):
    return (X[0]//Y[0], X[1]//Y[1])

for _ in range(3):
    R = multiply(R, R)
    R = div(R, (10, 10))
    R = add(R, A)

print(f"[{R[0]},{R[1]}]")