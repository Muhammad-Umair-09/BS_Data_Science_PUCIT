from random import *
i=1
while i<=10:
    a1=randint(1,100)
    a2=randint(1,100)
    if a1>a2:
        print("1st number is larger")
    if a1<a2:
        print("2nd number is larger")
    i=i+1
