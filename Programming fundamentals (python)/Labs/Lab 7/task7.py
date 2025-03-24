from random import *
i=0
a=[None]*25
while i<25:
    a[i]=randint(25021,289820)
    i=i+1

sum=0
j=0
while j<len(a):
    sum=sum+a[j]
    j=j+1
    avrg=sum/len(a)
print("Average is: ",avrg)

Min=a[0]
Max=a[0]
k=1
while k<len(a):
    if Min>a[k]:
        Min=a[k]
    if Max<a[k]:
        Max=a[k]
    k=k+1
print("Minimum number is: ",Min)

print("Maximum number is: ",Max)

abv=0
m=0
while m<len(a):
    if a[m]>avrg:
        abv=abv+1
    m=m+1
print("Number of values above average is: ",abv)
