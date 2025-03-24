n1=int(input())
n2=int(input())
Sum=0
if n1<n2:
    while n1<=n2:
        print(n1)
        Sum=Sum+n1
        n1=n1+1
elif n2<n1:
    while n2<=n1:
        print(n2)
        Sum=Sum+n2
        n2=n2+1
print("Sum is:",Sum)
