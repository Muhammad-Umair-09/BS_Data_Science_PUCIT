def getabc():
    v1 = 1
    v2 = 2
    v3 = -35
    return v1, v2, v3
    
def calcroots(a,b,c):    
    r1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
    r2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)
    
    return r1, r2
    
def showroots(x1,x2):
    print(x1)
    print(x2)
    return
    
def main():
    a,b,c = getabc()
    r1,r2 = calcroots(a,b,c)
    showroots(r1,r2)
    return
    
main()
