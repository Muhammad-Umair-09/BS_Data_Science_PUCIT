from random import *
i=1
se=0
so=0
while i<=10:
    a=randint(1,100)
    print(a)
    if a%2==0:
        se= se+a
    else:
        so=so+a
    i=i+1
print("Sum of even:",se)
print("Sum of odd:",so)
