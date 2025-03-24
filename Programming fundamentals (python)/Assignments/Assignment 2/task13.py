def GS(s,r,n):
    i=1
    p=s
    while i<=n:
        print(p)
        p=p*r
        i=i+1
s= int(input("Enter starting point: "))
r= int(input("Enter common ratio: "))
n= int(input("count of numbers to print: "))
GS(s,r,n)


