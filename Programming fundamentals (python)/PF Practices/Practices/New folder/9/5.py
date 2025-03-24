a=int(input())
res = ''
while a>0:
    r=a%10
    res = res + str(r)
    a=a//10
print("Reverse number is",res)
