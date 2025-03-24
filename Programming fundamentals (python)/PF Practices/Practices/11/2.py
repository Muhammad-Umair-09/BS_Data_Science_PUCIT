from random import *
i=1
while i<=10:
    a=randint(1,100)
    b=randint(1,100)
    c=randint(1,100)
    print("Genereted: ",a,b,c)
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
    if a>b:
        a,b=b,a
    print("Sorted: ",a,b,c)
    i=i+1

