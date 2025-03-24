from random import *


a=[None]*1000
datasize1=100
for j in range(datasize1):
    a[j]=randint(1,1000)


b=[None]*1000
datasize2=100
for j in range(datasize2):
    b[j]=randint(1,1000)
    b[datasize2]=-1


c=[None]*(datasize1+datasize2)
i=0
c1=0
while a[i]!=None:
    c[i]=a[i]
    i+=1
    c1+=1

j=0
while b[j]!=-1:
    c[c1]=b[j]
    c1+=1
    j=j+1
print(c)


