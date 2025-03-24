class Matrix22:
    pass


def SumofM(m1,m2):
    m=Matrix22()
    m.a11=m1.a11+m2.a11
    m.a12=m1.a12+m2.a12
    m.a21=m1.a21+m2.a21
    m.a22=m1.a22+m2.a22
    return m

def PrintMatrix(m):
    print("<", m.a11, m.a12,";", m.a21, m.a22, ">")


def main():
    m1 = Matrix22()
    m1.a11 = 1
    m1.a12 = 2
    m1.a21 = 3
    m1.a22 = 4

    m2 = Matrix22()
    m2.a11 = 1
    m2.a12 = 2
    m2.a21 = 3
    m2.a22 = 4

    PrintMatrix(SumofM(m1,m2))
main()
