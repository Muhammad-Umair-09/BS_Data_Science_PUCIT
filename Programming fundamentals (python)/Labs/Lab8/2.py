def func1(a,s):
    i=0
    c=0
    while i<(len(a)-1):
        j=i+1
        while j<len(a):
            if a[i]+a[j]==s:
                c=c+1
            j=j+1
        i=i+1
    return c

a=[3,4,5,4,6,4]


print(func1(a,8))
