from random import *
a=[None]*1000


datasize=100
for j in range(datasize):
    a[randint(0,1000)]=randint(1,1000)
    a[datasize]=-1

for j in range(1000):
    if a[j]==None:
        a[j]=-1
print(a)

s=0
for j in range(1000):
    if a[j]!=-1:
        if a[j]<99 and a[j]>10:
            s=s+a[j]

print(s)
