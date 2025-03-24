def GS(s,r,n):
    i=1
    p=s
    Sum=p
    while i<n:
        p=p*r
        Sum=Sum+p
        i=i+1
    return Sum
s= int(input("Enter starting point: "))
r= int(input("Enter common ratio: "))
n= int(input("count of numbers to print: "))
print(GS(s,r,n))


