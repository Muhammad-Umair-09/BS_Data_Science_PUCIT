n=int(input("N: "))
for i in range(n):
    print("+"*(n-i),end="")
    print(" "*(i*2),end="")
    print("+"*(n-i))
for i in range(2,n+1):
    print("+"*(i),end="")
    print(" "*((n-i)*2),end="")
    print("+"*(i))
