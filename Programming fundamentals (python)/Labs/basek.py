from math import log
#log(x, base)

def baseK(n, k):
    print("\nComputing", n, "base", k, "is")
    ln = int(log(n,k))
    print("length of base k number is", ln+1)
    print("------------------------------")
    while ln >= 0:
        q = n // k**ln
        r = n % k**ln
        
        print(q, r)

        n = r
        ln = ln-1


baseK(12, 2)

baseK(67, 8)

baseK(48, 5)
