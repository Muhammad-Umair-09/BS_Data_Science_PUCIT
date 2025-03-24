a=int(input())
b=int(input())
c=int(input())
d=int(input())
i=1
while i<=3:
    if a>b:
        temp=a
        a=b
        b=temp
    elif b>c:
        temp=b
        b=c
        c=temp
    elif c>d:
        temp=c
        c=d
        d=temp
    i+=1
print(a,b,c,d)

