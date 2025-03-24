n=5#int(input("N: "))
for i in range(n-1):
    print(chr(97),end=" ")
    for j in range(i,n+6*(i),i+1):
        print(chr(98+j),end=" ")
    print()
