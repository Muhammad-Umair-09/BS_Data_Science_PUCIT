def selection_sort(a):
    for j in range(len(a)-1):
        for i in range(j+1,len(a)):
            if a[j]<a[i]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    return a

from random import *
a=[randint(1,100) for i in range(10)]
print(selection_sort(a))
