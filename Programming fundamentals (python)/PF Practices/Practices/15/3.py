from random import *
mx=0
n=1
for i in range(1,11):
    a=randint(1,100)
    b=randint(1,100)
    c=randint(1,100)
    x=round(((a+b+c)/3),1)
    print(f"{a} {b} {c}   avrg is {x}")
    if x>mx:
        mx=x
        n=i
print(f"Set {n} has highest average")

