class Matrix22:
    pass


def PrintMatrix(m):
    print("<", m.a11, m.a12,";", m.a21, m.a22, ">")

def main():
    m1 = Matrix22()
    m1.a11 = 1
    m1.a12 = 2
    m1.a21 = 3
    m1.a22 = 4
    m2 = Matrix22()
    m2.a11 = 5
    m2.a12 = 6
    m2.a21 = 7
    m2.a22 = 8
    PrintMatrix(m1)
    print()
    PrintMatrix(m2)
main()
