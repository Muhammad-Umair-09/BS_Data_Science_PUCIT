from random import *
a=[None]*1000


datasize=100
for j in range(datasize):
    a[j]=randint(1,1000)

s=0
for j in range(datasize):
    if a[j]<99 and a[j]>10:
        s=s+a[j]

print(s)
