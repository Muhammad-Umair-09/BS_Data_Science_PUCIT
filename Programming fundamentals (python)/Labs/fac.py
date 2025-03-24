def fact(n):
    r = 1
    x = 1
    while x <= n:
        r = r*x
        x = x+1
    return r


print("0! is: ", fact(0))
print("1! is: ", fact(1))
print("2! is: ", fact(2))
print("5! is: ", fact(5))
print("20! is: ", fact(20))
print("128! is: ", fact(128))
print("4321! is: ", fact(4321))

