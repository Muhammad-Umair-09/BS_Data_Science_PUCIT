class twoDarray:
    pass
    
def create2Darray(S1, S2):
    tda = twoDarray()
    tda.data = [None]*(S1*S2)
    tda.d1size = S1
    tda.d2size = S2
    return tda
        
def get2DarrayElem(ar, i1, i2):
    # if i1 and i2 are in valid range
    return ar.data[i1*ar.d2size+i2]
    
def set2DarrayElem(ar, i1, i2, d):
    # if i1 and i2 are in valid range
    ar.data[i1*ar.d2size+i2] = d

def main():
    a = create2Darray(5, 3)
    set2DarrayElem(a, 0, 1, -99)
    set2DarrayElem(a, 2, 2, -77)
    set2DarrayElem(a, 4, 0, -88)
    print(a.data)
    
main()