n= int(input("N: "))
k= int(input("K: "))
print("{",end="")
for i in range(1,n+1):
    for j in range(1,k+1):
        if i==n:
            print(f"({i},{j})",end="")
        else:
            print(f"({i},{j})",end=",")
print("}")
