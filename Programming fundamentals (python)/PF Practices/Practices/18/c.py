n = int(input("N: "))
for i in range(n):
    print(" " * (i), end="")
    print("+" * (n - i))
for i in range(2, n + 1):
    print(" " * (n - i), end="")
    print("+" * i)
