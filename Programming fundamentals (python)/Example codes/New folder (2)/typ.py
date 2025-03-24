from math import sqrt

class Vector:
    pass

def printVector(v):
    print("(", v.x, ",", v.y, ",", v.z,")")

def addVectors(v1, v2):
    r  = Vector()
    r.x = v1.x+v2.x
    r.y = v1.y+v2.y
    r.z = v1.z+v2.z
    return r

def magnitute(v):
    return sqrt(v.x*v.x + v.y*v.y + v.z*v.z)

v1 = Vector()
v1.x = 4
v1.y = 3
v1.z = 0

v2 = Vector()
v2.x = 0
v2.y = 2
v2.z = -6

v3 = addVectors(v1,v2)

printVector(v3)
print(magnitute(v3))
