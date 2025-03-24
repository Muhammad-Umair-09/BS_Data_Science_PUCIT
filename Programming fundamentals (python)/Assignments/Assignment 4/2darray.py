class twoDarray:
    pass

def create2Darray(S1, S2):
    tda = twoDarray()
    tda.data = [None]*(S1*S2)
    tda.d1size = S1
    tda.d2size = S2
    return tda

def get2DarrayElem(ar, i1, i2):
    for i in range(i1):
        for j in range(i2):
            print(ar[i*i2+j],end="\t")
        print()

def set2DarrayElem(ar, i1, i2, d):
    ar.data[i1*ar.d2size+i2] = d

def main():
    a = create2Darray(3, 5)
    set2DarrayElem(a, 0, 1, -99)
    set2DarrayElem(a, 2, 2, -77)
    set2DarrayElem(a, 1, 4, -88)
    get2DarrayElem(a.data,3,5)

main()
