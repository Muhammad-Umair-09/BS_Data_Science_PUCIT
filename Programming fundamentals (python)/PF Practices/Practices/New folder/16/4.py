from random import *
r=int(input("Rows: "))
c=int(input("Col: "))
for i in range(r):
    for j in range(c):
        print(randint(1,9),end="  ")
    print()
