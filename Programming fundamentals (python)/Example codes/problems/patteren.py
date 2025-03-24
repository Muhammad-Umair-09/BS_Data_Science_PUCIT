N = 10
r = 1
while r <= N:
    c = 1
    while c <= r:
        print("@", end="")
        c = c + 1
    print()
    r = r + 1

print("----------------------------------")

N = 8
r = 1
while r <= N:
    c = 1
    while c <= r**2:
        print("@", end="")
        c = c + 1
    print()
    r = r + 1

print("----------------------------------")

N = 10
r = 1
while r <= N:
    c = N
    while c > N - r + 1:
        print(" ", end="")
        c = c - 1
    while c >= 1:
        print("@", end="")
        c = c - 1
    print()
    r = r + 1

