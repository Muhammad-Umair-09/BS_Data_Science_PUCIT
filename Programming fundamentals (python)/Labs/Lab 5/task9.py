def isperfectsquare(n):
    i=1
    while i<n:
        s=i*i
        i=i+1
        if s==n:
            return True
    return False

a=isperfectsquare(int(input("Enter a number to check whether is it perfect square or not: ")))
print(a)
