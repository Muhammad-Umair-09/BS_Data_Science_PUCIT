def LCM(a, b):
    r = None
    j = 0
    while j<=a*b:
        if j%a == 0 and j%b == 0:
            r = j
        j = j+1
    return r
    
def main():
    print(LCM(3,7))
    print(LCM(2,16))
    print(LCM(12, 16))
    
main()
