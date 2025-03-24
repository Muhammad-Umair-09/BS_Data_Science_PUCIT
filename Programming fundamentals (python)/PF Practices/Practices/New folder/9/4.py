a=int(input())
i=2
s=0
while a>0:
    q=a//10**i
    s=s+q
    a=a%10**i
    i=i-1
print("Sum is:",s)
