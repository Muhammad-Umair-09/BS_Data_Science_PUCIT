from random import *
a=[randint(12000,1200001) for i in range(10)]
for i in range(len(a)):
    if a[i]<=50000:
        print(a[i],"W")
    elif a[i]<=125000:
        print(a[i],"D")
    elif a[i]<=500000:
        print(a[i],"C")
    elif a[i]<=900000:
        print(a[i],"B")
    elif a[i]<=1200000:
        print(a[i],"A")
print()
print("==========")
for i in range(len(a)):
    if a[i]<=50000 and a[i]>=12000:
        print(a[i],"W")
    if a[i]<=125000 and a[i]>=50001:
        print(a[i],"D")
    if a[i]<=500000 and a[i]>=125001:
        print(a[i],"C")
    if a[i]<=900000 and a[i]>=500001:
        print(a[i],"B")
    if a[i]<=1200000 and a[i]>=900001:
        print(a[i],"A")
print()
print("==========")
for i in range(len(a)):
    if a[i]<=50000:
        if a[i]>=12000:
            print(a[i],"W")
    if a[i]<=125000:
        if a[i]>=50001:
            print(a[i],"D")
    if a[i]<=500000:
        if a[i]>=125001:
            print(a[i],"C")
    if a[i]<=900000:
        if a[i]>=500001:
            print(a[i],"B")
    if a[i]<=1200000:
       if a[i]>=900001:
            print(a[i],"A")

