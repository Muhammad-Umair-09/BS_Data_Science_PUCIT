from random import *
a=[randint(1,1000) for i in range(100)]
print(a)

s=0
for j in range(len(a)):
    if a[j]<=99 and a[j]>=10:
        s=s+a[j]

print(s)
