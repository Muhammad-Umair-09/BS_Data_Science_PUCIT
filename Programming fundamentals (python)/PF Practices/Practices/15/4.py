#This can work properly if we know the max of data given
from random import *
mx=0
mn=100
mx_n=1
mn_n=1
for i in range(1,11):
    a=randint(1,100)
    b=randint(1,100)
    c=randint(1,100)
    x=round(((a+b+c)/3),1)
    print(f"{a} {b} {c}   avrg is {x}")
    if x>mx:
        amx=a
        bmx=b
        cmx=c
        mx=x
        mx_n=i
    if x<mn:
        amn=a
        bmn=b
        cmn=c
        mn=x
        mn_n=i
print(f"Set {mx_n} has highest average and elements are {amx,bmx,cmx}")
print(f"Set {mn_n} has minimum average and elements are {amn,bmn,cmn}")

