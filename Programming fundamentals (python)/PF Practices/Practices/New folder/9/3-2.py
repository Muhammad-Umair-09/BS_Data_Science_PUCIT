a=int(input())
i=2
while a>0:
    q=a//10**i
    print(q)
    a=a%10**i
    i=i-1

