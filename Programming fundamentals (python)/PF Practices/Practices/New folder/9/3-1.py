from random import *
c1=randint(0,3)
n1=randint(1,13)
c2=randint(0,3)
n2=randint(1,13)
n1=n1-1
n2=n2-1
a=["Diamond","Heart","Spade","Club"]
b=["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
print(b[n1],"of",a[c1])
print(b[n2],"of",a[c2])
i=1
if (c1<2 and c2<2):
    print("Both cards have same colour")
if c1==c2:
    print("Both cards have same type")
if n1==n2:
    print("Both cards have same number")
if n1==n2+1 or n1==n2-1:
    print("Both cards are in sequence")



