a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
    if b<c:
        order=(a,b,c)
    else:
        order=(a,c,b)
if b<a and b<c:
    if a<c:
        order=(b,a,c)
    else:
        order=(b,c,a)
if c<a and c<b:
    if a<b:
        order=(c,a,b)
    else:
        order=(c,b,a)
print("Numbers in ascending order are: ",order)
