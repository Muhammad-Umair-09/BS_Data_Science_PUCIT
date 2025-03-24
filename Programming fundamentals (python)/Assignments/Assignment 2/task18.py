n=int(input("size of array: "))
a=[None]*n
i=0
while i<n:
    a[i]=int(input("Number: "))
    i=i+1
i=1
Max=a[0]
Min=a[0]
while i<n:
    if Max<a[i]:
        Max=a[i]
    if Min>a[i]:
        Min=a[i]
    i=i+1
print("Max",Max)
print("Min",Min)

