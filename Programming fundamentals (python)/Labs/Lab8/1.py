a=[None]*25
i=0
while i<len(a):
    a[i]=int(input())
    i=i+1
print(a)
def arraydis(a,v,s):
    count=0
    j=0
    while j<25:
        if a[j]+v==s:
            count=count+1
        j=j+1
    return count

print(arraydis(a,15,50324))
print(arraydis(a,153,534))
print(arraydis(a,17,37))
print(arraydis(a,45,78))



