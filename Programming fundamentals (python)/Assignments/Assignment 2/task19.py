n=int(input("Enter the size of array: "))
a=[None]*n
b=[None]*n
i=0
while i<n:
    a[i]=int(input("Number: "))
    i=i+1
i=0
while i<n:
    b[i]=int(input("Number: "))
    i=i+1
p=[None]*n
i=0
while i<n:
    p[i]=a[i]*b[i]
    i=i+1
print("Product is: ",p)
