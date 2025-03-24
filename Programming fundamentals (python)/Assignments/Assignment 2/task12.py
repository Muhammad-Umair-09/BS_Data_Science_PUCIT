from random import *
i=1
while i<=10:
    a=randint(0,500)
    b=randint(0,500)
    c=randint(0,500)
    print("Generated: ",a,b,c)
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
    if a>b:
        a,b=b,a
    print("Sorted: ",a,b,c)
    i=i+1
