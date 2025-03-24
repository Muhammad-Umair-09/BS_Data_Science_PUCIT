n=int(input("Enter the size of triangle: "))
s=1
for i in range(n-1,-1,-1):
    if i==(n-1):
        print(" "*i+"*")
    elif i==0:
        print("*"*n)
    else:
        print(" "*i+"*"+" "*(s-1)+"*")
        s+=1

