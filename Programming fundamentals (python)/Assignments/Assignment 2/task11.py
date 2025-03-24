from random import *
i=1
while i<=10:
    a=randint(0,100)
    b=randint(0,100)
    if a>b:
        print("First number is larger")
    if a<b:
        print("Second number is larger")
    i=i+1

