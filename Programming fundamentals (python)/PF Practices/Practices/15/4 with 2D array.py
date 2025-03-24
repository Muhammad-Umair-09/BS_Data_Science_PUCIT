from random import *
a=[[randint(1,100) for i in range(4)] for j in range(10)]

for i in range(10):
    sm=0
    for j in range(3):
        print(a[i][j],end=" ")
        sm+=a[i][j]
    a[i][3]=round((sm/3),1)
    print("  Avrg is:", a[i][j+1])


mx=a[0][3]
mn=a[0][3]
mx_n=0
mn_n=0
for i in range(1,10):
    if a[i][3]>mx:
        mx=a[i][3]
        mx_n=i
    if a[i][3]<mn:
        mn=a[i][3]
        mn_n=i
print("=========================")
print(f"Set {mx_n+1} has max avrg")
print("Fourth index is the average of first three elements: ",a[mx_n])
print("=========================")
print(f"Set {mn_n+1} has min avrg")
print("Fourth index is the average of first three elements: ",a[mn_n])




