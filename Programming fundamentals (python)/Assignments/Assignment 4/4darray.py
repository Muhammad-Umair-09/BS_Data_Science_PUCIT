class twoDarray:
    pass

def create4Darray(S1, S2 , S3, S4):
    tda = twoDarray()
    tda.data = [None]*(S1*S2*S3*S4)
    tda.d1size = S1
    tda.d2size = S2
    tda.d3size = S3
    tda.d4size = S4
    return tda

def get4DarrayElem(ar, i1, i2,i3,i4):
    for i in range(i1):
        print("Book #",i)
        for j in range(i2):
            print("Page #",j)
            for k in range(i3):
                for l in range(i4):
                    print(ar[i*i2*i3*i4+j*i3*i4+k*i4+l], end="\t")
                print()
            print()
        print()

def set4DarrayElem(ar, i1, i2, i3, i4, d):
    ar.data[(i1*ar.d2size*ar.d3size*ar.d4size)+(i2*ar.d3size*ar.d4size)+(i3*ar.d4size)+i4] = d

def main():
    a = create4Darray(4, 3, 5, 6)
    set4DarrayElem(a, 0, 2, 1, 5, -99)
    set4DarrayElem(a, 1, 1, 2, 3, -77)
    set4DarrayElem(a, 3, 0, 4, 1, -88)
    get4DarrayElem(a.data,4,3,5,6)

main()
