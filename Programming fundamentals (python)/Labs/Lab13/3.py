from math import *
def checkerBoard(s):
    n=int(sqrt(s))
    x=0
    a=n
    if x%2==0:
        x,a=a,x
    for k in range(n):
        x,a=a,x
        for i in range(n):
            if n%2!=0:
                x,a=a,x
            for j in range(n):
                x,a=a,x
                for k in range(n):
                    print(x,end=" ")
            print()


a=int(input("Enter a perfect square: "))
checkerBoard(a)
