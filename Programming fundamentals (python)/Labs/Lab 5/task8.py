print("enter a series of positive numbers\nand enter a negative number to signal the end of the series: ")
s=0
p=1
c=0
a=int(input())
while a>0:
    s=s+a
    p=p*a
    c=c+1
    a=int(input())
print("Sum:", s)
print("Product:", p)
print("Count:", c)
print("Average:", s/c)
