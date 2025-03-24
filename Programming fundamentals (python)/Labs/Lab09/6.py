def isSorted(a):
    i=0
    r=True
    while i<(len(a)-1):
        if a[i]<a[i+1]:
            r=False
        i=i+1
    return r


a=[32,30,28,22,18]
print(isSorted(a))

a=[32,22,18,30,28]
print(isSorted(a))
