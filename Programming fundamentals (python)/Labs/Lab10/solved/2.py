class Matrix22:
    pass


def DetOfM(m):
    print(m.a11 * m.a22 - m.a12 * m.a21)


def main():
    m1 = Matrix22()
    m1.a11 = 9
    m1.a12 = 2
    m1.a21 = 3
    m1.a22 = 4

    m2 = Matrix22()
    m2.a11 = 7
    m2.a12 = 2
    m2.a21 = 4
    m2.a22 = 9

    DetOfM(m1)
    print()
    DetOfM(m2)


main()
