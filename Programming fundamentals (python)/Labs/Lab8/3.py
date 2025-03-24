def func2(a):
    c=0
    i=0
    while i<len(a):
        j=i+1
        while j<len(a):
            if a[i]>a[j]:
                c=c+1
            j=j+1
        i=i+1
    return c

a=[1,2,3,2,7,6,7,10,9,10]
print(func2(a))
