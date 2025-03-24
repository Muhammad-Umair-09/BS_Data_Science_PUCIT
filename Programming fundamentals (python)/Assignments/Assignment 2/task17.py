n=int(input("Enter the size of array: "))
a=[None]*n
i=0
while i<n:
    a[i]=int(input("Enter a number: "))
    i=i+1
j=n-1
while j>=0:
    print(a[j], end=" ")
    j=j-1

