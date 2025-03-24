#3DArray
class twoDarray:
    pass

def create3Darray(S1, S2 , S3):
    tda = twoDarray()
    tda.data = [None]*(S1*S2*S3)
    tda.d1size = S1
    tda.d2size = S2
    tda.d3size = S3
    return tda

def get3DarrayElem(ar, i1, i2,i3):
    for i in range(i1):
        print("Page #",i)
        for j in range(i2):
            for k in range(i3):
                print(ar[i*i2*i3+j*i3+k], end="\t")
            print()

def set3DarrayElem(ar, i1, i2, i3, d):
    ar.data[i1*ar.d2size*ar.d3size+i2*ar.d3size+i3] = d

def main():
    a = create3Darray(4, 3, 5)
    set3DarrayElem(a, 0, 1, 1, -99)
    set3DarrayElem(a, 2, 2, 3, -77)
    set3DarrayElem(a, 3, 0, 0, -88)
    get3DarrayElem(a.data,4, 3, 5)


main()
