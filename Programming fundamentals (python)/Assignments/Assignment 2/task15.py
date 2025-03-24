def Fn(n):
    if n<0:
        return None
    a=(2**(2**n))+1
    return a
n=int(input())
print(Fn(n))
