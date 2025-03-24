n = int(input("Enter a number: "))
base = 8
while n>=base:
    r=n%base
    n=n//base
    print(r,end="")
print(n)

