from math import sqrt

class Vector:
    pass

def inputVector():
    rv = Vector()
    rv.x = 2#float(input())
    rv.y = 3#float(input())
    rv.z = 1#float(input())
    return rv

def printVector(vc):
    print("(", vc.x, ",", vc.y, ",", vc.z, ")")

def sumVectors(vc1, vc2):
    rv = Vector()
    rv.x = vc1.x + vc2.x
    rv.y = vc1.y + vc2.y
    rv.z = vc1.z + vc2.z
    return rv

def magnitude(vc):
    return sqrt(vc.x**2 + vc.y**2 + vc.z**2)

def main():
    v1 = Vector()
    v1.x = 2.0
    v1.y = 5.0
    v1.z = 1.0

    print("Enter three number as x, y, z of a vector")
    v2 = inputVector()

    v3 = sumVectors(v1, v2)

    m = round(magnitude(v1), 2)

    u1 = Vector()
    u1.x = round(v1.x / m, 1)
    u1.y = round(v1.y / m, 1)
    u1.z = round(v1.z / m, 1)

    print("Vectors V1, v2, and their sum V3 are")
    printVector(v1)
    printVector(v2)
    printVector(v3)

    print("Magnitude and unit vector of V1 are")
    print(m)
    printVector(u1)


main()


